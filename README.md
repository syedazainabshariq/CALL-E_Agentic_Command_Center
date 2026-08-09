# CALL-E Agentic Command Center

An enterprise-grade autonomous voice agent platform built for the CALL-E Hackathon. This application provides a sleek, dark-themed command center interface using Streamlit to deploy, monitor, and inspect goal-driven AI phone agents in real time.

## ✨ Features

* **Execution Dashboard**: Configure task parameters, target schedules, and E.164 phone numbers with instant agent dispatch.
* **Live Telemetry & Transcript Viewer**: Real-time parsing and structured rendering of call dialogue turns, execution status, and agent summaries.
* **Low-Level Payload Inspector**: Dedicated JSON audit logs for inspecting raw response payloads returned by the CALL-E SDK execution engine.
* **Elite UI Design**: Custom dark-mode styling inspired by modern developer platforms, featuring a clean layout and system diagnostics.

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* A valid CALL-E API Key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/calle-agentic-command-center.git
cd calle-agentic-command-center

```


2. Install dependencies:
```bash
pip install streamlit python-dotenv calle

```


3. Configure your environment variables:
Create a `.env` file in the root directory and add your API key:
```env
CALLE_API_KEY=your_actual_api_key_here

```



### Running the App

Launch the Streamlit dashboard locally:

```bash
python -m streamlit run dashboard.py

```

## 🛠️ Tech Stack

* **Frontend & UI**: Streamlit
* **Agent Core**: CALL-E SDK (`CalleClient`)
* **Styling**: Custom CSS Injection & Responsive Layouts
