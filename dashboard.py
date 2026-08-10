import os
import streamlit as st
import requests

# Set page configuration and professional styling
st.set_page_config(
    page_title="CALL-E Agentic Command Center",
    page_icon="[Phone]",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTextInput > div > div > input { background-color: #161b22; color: #ffffff; border: 1px solid #30363d; }
    .stTextArea > div > div > textarea { background-color: #161b22; color: #ffffff; border: 1px solid #30363d; }
    .metric-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; }
</style>
""", unsafe_allow_html=True)

# Retrieve API key securely from Streamlit Secrets or environment
API_KEY = st.secrets.get("CALLE_API_KEY") or os.environ.get("CALLE_API_KEY", "")

st.title("CALL-E Agentic Command Center")
st.markdown("Enterprise-grade autonomous voice agent dashboard for live task dispatch and real-time telemetry.")

# Sidebar Configuration
st.sidebar.header("Agent Dispatch Control")
phone_number = st.sidebar.text_input("Target Phone Number (E.164)", placeholder="+14155552671")
task_prompt = st.sidebar.text_area("Agent Goal / Prompt", placeholder="Call to confirm the appointment scheduled for tomorrow at 3 PM.")
dispatch_button = st.sidebar.button("Dispatch Agent Call", type="primary")

# Main Dashboard Tabs
tab1, tab2, tab3 = st.tabs(["Live Telemetry", "Transcript & Dialogues", "Raw Payload Inspector"])

# Initialize session state for tracking responses
if "last_response" not in st.session_state:
    st.session_state.last_response = None

if dispatch_button:
    if not API_KEY:
        st.error("Missing API Key. Please configure `CALLE_API_KEY` in your Streamlit Secrets.")
    elif not phone_number or not task_prompt:
        st.warning("Please provide both a target phone number and an agent task prompt.")
    else:
      with st.spinner("Dispatching live autonomous voice agent call via CALL-E..."):
        try:
          url = "https://api.calle.ai/v1/calls"
          headers = {
              "Authorization": f"Bearer {API_KEY}",
              "Content-Type": "application/json",
          }
          payload = {
              "phone_number": phone_number,
              "prompt": task_prompt
          }
          response = requests.post(url, json=payload, headers=headers)
          
          if response.status_code == 200:
              st.session_state.last_response = response.json()
              st.success("Live call dispatched successfully.")
          else:
              # Fallback to handle error details or test status gracefully if endpoint differs
              st.session_state.last_response = {
                  "status": "error",
                  "status_code": response.status_code,
                  "message": response.text,
                  "phone_number": phone_number,
                  "goal": task_prompt
              }
              st.warning(f"Received response status {response.status_code}. Check payload inspector for details.")
        except Exception as e:
          st.error(f"Connection error: {e}")

with tab1:
  st.subheader("Execution Status & Telemetry")
  if st.session_state.last_response:
    res = st.session_state.last_response
    col1, col2, col3 = st.columns(3)
    with col1:
      st.metric(
          label="Execution Status",
          value=str(res.get("status", "Completed")).capitalize(),
      )
    with col2:
      st.metric(
          label="Task Completed",
          value=str(res.get("task_completed", False)),
      )
    with col3:
      st.metric(label="Duration", value=f"{res.get('duration', '0')}s")
  else:
    st.info(
        "No active execution recorded yet. Configure parameters and dispatch"
        " an agent from the sidebar."
    )

with tab2:
  st.subheader("Call Dialogue Transcript")
  if st.session_state.last_response:
    transcript = st.session_state.last_response.get("transcript", [])
    if transcript:
      for turn in transcript:
        speaker_label = (
            "**Agent**" if turn.get("speaker") == "Agent" else "**Recipient**"
        )
        st.markdown(f"{speaker_label}: {turn.get('text')}")
    else:
      st.info("No transcript dialogue returned in the live payload yet.")
  else:
    st.write("Transcript logs will appear here post-call execution.")

with tab3:
  st.subheader("Low-Level JSON Payload Inspector")
  if st.session_state.last_response:
    st.json(st.session_state.last_response)
  else:
    st.code(
        '{\n  "status": "idle",\n  "message": "Awaiting execution payload..."\n}',
        language="json",
    )
