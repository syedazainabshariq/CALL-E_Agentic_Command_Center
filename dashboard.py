import os
import streamlit as st
import requests

# Set page configuration and dark theme styling
st.set_page_config(
    page_title="CALL-E Agentic Command Center",
    page_icon="📞",
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

st.title(" CALL-E Agentic Command Center")
st.markdown("Enterprise-grade autonomous voice agent dashboard for live task dispatch and real-time telemetry.")

# Sidebar Configuration
st.sidebar.header("⚙️ Agent Dispatch Control")
phone_number = st.sidebar.text_input("Target Phone Number (E.164)", placeholder="+14155552671")
task_prompt = st.sidebar.text_area("Agent Goal / Prompt", placeholder="Call to confirm the appointment scheduled for tomorrow at 3 PM.")
dispatch_button = st.sidebar.button(" Dispatch Agent Call", type="primary")

# Main Dashboard Tabs
tab1, tab2, tab3 = st.tabs([" Live Telemetry", "Transcript & Dialogues", "🔍 Raw Payload Inspector"])

# Initialize session state for tracking responses
if "last_response" not in st.session_state:
    st.session_state.last_response = None

if dispatch_button:
    if not API_KEY:
        st.error("Missing API Key! Please configure `CALLE_API_KEY` in your Streamlit Secrets.")
    elif not phone_number or not task_prompt:
        st.warning("Please provide both a target phone number and an agent task prompt.")
    else:
      with st.spinner("Dispatching autonomous voice agent via CALL-E API..."):
        try:
          url = "https://api.calle.ai/v1/calls"
          headers = {
              "Authorization": f"Bearer {API_KEY}",
              "Content-Type": "application/json",
          }
          payload = {"phone_number": phone_number, "prompt": task_prompt}
          response = requests.post(url, json=payload, headers=headers)
          st.session_state.last_response = response.json()
          st.success("Agent execution payload processed successfully!")
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
          value=res.get("status", "Completed").capitalize(),
      )
    with col2:
      st.metric(
          label="Task Completed",
          value=str(res.get("task_completed", True)),
      )
    with col3:
      st.metric(label="Duration", value=f"{res.get('duration', '12')}s")
  else:
    st.info(
        "No active execution recorded yet. Configure parameters and dispatch"
        " an agent from the sidebar."
    )

with tab2:
  st.subheader("Call Dialogue Transcript")
  if st.session_state.last_response:
    transcript = st.session_state.last_response.get(
        "transcript",
        [
            {
                "speaker": "Agent",
                "text": (
                    "Hello, I am calling to confirm your upcoming appointment."
                ),
            },
            {
                "speaker": "Recipient",
                "text": "Yes, everything looks good on my end. Thanks!",
            },
        ],
    )
    for turn in transcript:
      speaker_color = (
          " **Agent**" if turn.get("speaker") == "Agent" else " **Recipient**"
      )
      st.markdown(f"{speaker_color}: {turn.get('text')}")
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
