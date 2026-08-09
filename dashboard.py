import os
from dotenv import load_dotenv
import streamlit as st
from calle import CalleClient

# Load environment variables
load_dotenv()
client = CalleClient(api_key=os.environ.get("CALLE_API_KEY"))

# Page Config
st.set_page_config(
    page_title="CALL-E | Enterprise Agentic Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Elite Design System & Custom CSS Injection (No Emojis, Clean Professional Look)
st.markdown(
    """
    <style>
    /* Global Theme Overrides */
    .stApp {
        background-color: #090a0f;
        color: #f3f4f6;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Hide Streamlit Default Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0d111a;
        border-right: 1px solid #1f293d;
    }

    /* Hero Banner */
    .hero-card {
        background: linear-gradient(135deg, #13182e 0%, #1a103c 100%);
        border: 1px solid rgba(139, 92, 246, 0.25);
        padding: 32px;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 10px 10px -5px rgba(0, 0, 0, 0.4);
    }
    .hero-title {
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.025em;
        color: #ffffff;
        margin-bottom: 6px;
    }
    .hero-subtitle {
        color: #9ca3af;
        font-size: 0.95rem;
    }

    /* Inputs Styling */
    .stTextInput input, .stTextArea textarea {
        background-color: #090a0f !important;
        color: #ffffff !important;
        border: 1px solid #374151 !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        font-size: 0.9rem !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important;
    }

    /* Elite Primary Button */
    .stButton button {
        background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        width: 100% !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #6d28d9 0%, #4338ca 100%) !important;
        box-shadow: 0 0 20px rgba(124, 58, 237, 0.4);
        border-color: rgba(255, 255, 255, 0.2) !important;
    }

    /* Status Badges */
    .badge-live {
        display: inline-flex;
        align-items: center;
        background-color: rgba(16, 185, 129, 0.1);
        color: #34d399;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(16, 185, 129, 0.2);
    }
    .pulse-dot {
        height: 6px;
        width: 6px;
        background-color: #34d399;
        border-radius: 50%;
        display: inline-block;
        margin-right: 6px;
        box-shadow: 0 0 8px #34d399;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar System Architecture Panel
with st.sidebar:
  st.markdown("### System Diagnostics")
  st.markdown(
      "<span class='badge-live'><span class='pulse-dot'></span>SDK"
      " Connected</span>",
      unsafe_allow_html=True,
  )
  st.markdown("<br>", unsafe_allow_html=True)

  st.markdown("**Environment:** `Production / Sandbox`")
  st.markdown("**Active Model:** `CALL-E Voice Agent v1.2`")
  st.markdown("**Security:** `OAuth2 + API Key Authenticated`")

  st.divider()
  st.markdown("### Quick Metrics")
  st.metric(label="Available Credits", value="20 Calls", delta="Active Tier")
  st.metric(label="Latency Avg.", value="420ms", delta="-12ms")

  st.divider()
  st.markdown(
      "<p style='font-size:0.75rem; color:#6b7280;'>CALL-E Hackathon Developer"
      " Build</p>",
      unsafe_allow_html=True,
  )

# Main Hero Header
st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">CALL-E Agentic Command Center</div>
        <div class="hero-subtitle">Deploy enterprise-grade autonomous phone agents to manage schedules, verify leads, and complete real-world operational workflows.</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Professional Multi-Tab Layout
tab1, tab2 = st.tabs(["Execution Dashboard", "System Inspector & Logs"])

with tab1:
  col_left, col_right = st.columns([1.2, 0.8], gap="large")

  with col_left:
    st.markdown("#### Task Parameters")
    with st.container():
      customer_name = st.text_input("Customer Name", value="Jane Doe")
      phone_number = st.text_input(
          "Recipient Phone Number (E.164 Format)",
          value="+14155552671",
          help="Must start with '+' and country code (e.g., +971...).",
      )
      appointment_time = st.text_input(
          "Target Appointment Time", value="Tomorrow at 10:00 AM"
      )

      st.markdown("<br>", unsafe_allow_html=True)
      trigger_call = st.button("Dispatch Autonomous AI Agent")

  with col_right:
    st.markdown("#### Real-Time Telemetry & Transcript")
    telemetry_placeholder = st.empty()

    if not trigger_call:
      telemetry_placeholder.markdown(
          """
            <div style="background-color: #111827; border: 1px dashed #374151; padding: 40px 20px; border-radius: 12px; text-align: center; color: #6b7280;">
                <p style="font-weight: 500; color: #9ca3af; margin-bottom: 4px;">Awaiting Task Dispatch</p>
                <p style="font-size: 0.8rem;">Configure parameters on the left and trigger the agent to initiate live execution.</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  if trigger_call:
    if not phone_number or not phone_number.startswith("+"):
      st.error(
          "Please specify a valid E.164 phone number starting with '+' (e.g.,"
          " +971...)."
      )
    else:
      with st.spinner(
          f"Establishing secure runtime connection to {phone_number}..."
      ):
        try:
          # Explicitly format task payload with the phone number upfront for the SDK parser
          clean_phone = phone_number.strip()
          task_payload = (
              f"Call {clean_phone}. You are a professional, polite scheduling"
              f" assistant. Speak with {customer_name} and confirm their"
              f" appointment scheduled for {appointment_time}. If they say no"
              " or seem unsure, ask if a different day or time would work"
              " better, and ensure you capture a definitive response."
          )

          response = client.calls.create_and_wait(task=task_payload)

          # Render telemetry card and transcript turns
          with telemetry_placeholder.container():
            st.markdown(
                """
                            <div style="background-color: #111827; border: 1px solid #1f293d; padding: 20px; border-radius: 12px; margin-bottom: 15px;">
                                <p style="color: #34d399; font-weight: 600; font-size: 0.85rem; margin-bottom: 12px;">EXECUTION COMPLETE</p>
                            """,
                unsafe_allow_html=True,
            )

            m1, m2 = st.columns(2)
            with m1:
              st.metric(
                  label="Status", value=response.get("status", "Unknown")
              )
            with m2:
              st.metric(
                  label="Task Completed",
                  value=str(response.get("task_completed", False)),
              )

            st.info(f"**Agent Summary:** {response.get('summary')}")
            st.markdown("</div>", unsafe_allow_html=True)

            # Parse and display transcript turns
            st.markdown("#### Call Dialogue Transcript")
            recipients = response.get("recipients", [])
            transcript_found = False

            if recipients:
              for rec in recipients:
                for att in rec.get("attempts", []):
                  turns = att.get("transcript_turns", [])
                  if turns:
                    transcript_found = True
                    for turn in turns:
                      speaker = turn.get("speaker", "Participant")
                      text = turn.get("text", "")
                      st.markdown(
                          f"> **{speaker}**: `{text}`", unsafe_allow_html=True
                      )

            if not transcript_found:
              st.info(
                  "No spoken dialogue turns recorded (call may have been"
                  " declined or ended with 0 duration)."
              )

          # Store session in session state for tab 2
          st.session_state["last_response"] = response

        except Exception as e:
          st.error(f"Runtime Exception: {e}")

with tab2:
  st.markdown("#### Low-Level Payload & Audit Inspector")
  if "last_response" in st.session_state:
    st.markdown(
        "Inspect the complete structural payload returned by the CALL-E SDK"
        " execution engine."
    )
    st.json(st.session_state["last_response"])
  else:
    st.info(
        "No execution logs found in current session memory. Run an agent task"
        " from the Execution Dashboard first."
    )