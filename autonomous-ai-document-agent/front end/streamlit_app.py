"""
Autonomous AI Document Agent
Professional Streamlit Frontend

Author: Gouthum Kharvi
"""

import streamlit as st
import requests
import threading
import time


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Autonomous AI Document Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# Constants
# ==========================================================

API_URL = "http://127.0.0.1:8000/api/v1/generate"

# No timeout — waits as long as the backend needs for multi-agent generation.
TIMEOUT_SECONDS = None

STAGES = ["VALIDATE", "PLAN", "DECIDE", "EXECUTE", "REFLECT", "DOCUMENT", "RESPOND"]

# Seconds to hold on each simulated stage before advancing to the next.
SECONDS_PER_STAGE = 8

# ==========================================================
# Custom CSS — Mission-Control / Telemetry Theme
# ==========================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root{
    --bg:            #0A0C10;
    --surface:       #12151B;
    --surface-alt:   #171B22;
    --border:        #232830;
    --text:          #E8E6E1;
    --text-dim:      #8B92A0;
    --amber:         #E8A33D;
    --amber-dim:     #8A6A2F;
    --green:         #4FD1A5;
    --red:           #E8604A;
}

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

.stApp{
    background:
        radial-gradient(circle at 15% 0%, rgba(232,163,61,0.06), transparent 40%),
        var(--bg);
}

.block-container{
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* ---------- Hero ---------- */

.eyebrow{
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 3px;
    font-size: 12px;
    color: var(--amber);
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.title{
    text-align: center;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 44px;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.5px;
    margin: 0;
}

.subtitle{
    text-align: center;
    color: var(--text-dim);
    font-size: 15px;
    font-family: 'JetBrains Mono', monospace;
    margin-top: 12px;
    margin-bottom: 8px;
}

.hero-rule{
    height: 2px;
    width: 120px;
    margin: 22px auto 0 auto;
    background: linear-gradient(90deg, transparent, var(--amber), transparent);
}

/* ---------- Telemetry Metric Cards ---------- */

.telemetry-row{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin: 28px 0;
}

.telemetry-card{
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--amber);
    border-radius: 10px;
    padding: 16px 18px;
}

.telemetry-label{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--text-dim);
    margin-bottom: 6px;
}

.telemetry-value{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 20px;
    font-weight: 600;
    color: var(--text);
}

/* ---------- Section Headers ---------- */

.section-label{
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--amber);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

h3{
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
}

/* ---------- Pipeline Track (Main Page) ---------- */

.pipeline{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px 20px;
    margin: 10px 0 6px 0;
    overflow-x: auto;
}

.pipe-node{
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 78px;
}

.pipe-dot{
    width: 34px;
    height: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 600;
    border: 1.5px solid var(--amber-dim);
    background: var(--surface-alt);
    color: var(--text-dim);
    transition: all 0.3s ease;
}

.pipe-label{
    font-size: 11px;
    color: var(--text-dim);
    margin-top: 8px;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.5px;
    text-align: center;
}

.pipe-line{
    flex: 1;
    height: 1.5px;
    background: repeating-linear-gradient(90deg, var(--amber-dim), var(--amber-dim) 4px, transparent 4px, transparent 8px);
    margin: 0 4px;
    margin-bottom: 22px;
    transition: background 0.4s ease;
}

.pipe-line-complete{
    background: var(--green) !important;
}

/* node states */
.pipe-dot-pending{
    opacity: 0.5;
}

.pipe-dot-active{
    border-color: var(--amber);
    background: rgba(232,163,61,0.14);
    color: var(--amber);
    animation: pulse-amber 1.3s infinite;
}

.pipe-dot-complete{
    border-color: var(--green);
    background: rgba(79,209,165,0.14);
    color: var(--green);
}

.pipe-dot-error{
    border-color: var(--red);
    background: rgba(232,96,74,0.16);
    color: var(--red);
    animation: pulse-red 1.1s infinite;
}

@keyframes pulse-amber{
    0%   { box-shadow: 0 0 0 0 rgba(232,163,61,0.45); }
    70%  { box-shadow: 0 0 0 9px rgba(232,163,61,0); }
    100% { box-shadow: 0 0 0 0 rgba(232,163,61,0); }
}

@keyframes pulse-red{
    0%   { box-shadow: 0 0 0 0 rgba(232,96,74,0.45); }
    70%  { box-shadow: 0 0 0 9px rgba(232,96,74,0); }
    100% { box-shadow: 0 0 0 0 rgba(232,96,74,0); }
}

.run-status-row{
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--text-dim);
    margin-bottom: 18px;
    padding: 0 2px;
}

.run-status-badge-running{ color: var(--amber); }
.run-status-badge-success{ color: var(--green); }
.run-status-badge-error{ color: var(--red); }

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"]{
    background: var(--surface);
    border-right: 1px solid var(--border);
}

.side-heading{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 15px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 4px;
}

.status-pill{
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--green);
    background: rgba(79,209,165,0.1);
    border: 1px solid rgba(79,209,165,0.3);
    padding: 4px 10px;
    border-radius: 20px;
    margin: 6px 0 14px 0;
}

.tech-chip{
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11.5px;
    color: var(--text);
    background: var(--surface-alt);
    border: 1px solid var(--border);
    padding: 5px 10px;
    border-radius: 6px;
    margin: 3px 4px 3px 0;
}

.stepper{
    margin-top: 4px;
}

.step-item{
    display: flex;
    align-items: flex-start;
    gap: 10px;
    position: relative;
    padding-bottom: 18px;
}

.step-item:last-child{
    padding-bottom: 0;
}

.step-item::before{
    content: "";
    position: absolute;
    left: 9px;
    top: 20px;
    bottom: 0;
    width: 1px;
    background: var(--border);
    transition: background 0.4s ease;
}

.step-item:last-child::before{
    display: none;
}

.step-item.line-complete::before{
    background: var(--green);
}

.step-dot{
    width: 20px;
    height: 20px;
    min-width: 20px;
    border-radius: 50%;
    background: var(--surface-alt);
    border: 1.5px solid var(--amber-dim);
    color: var(--text-dim);
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
    transition: all 0.3s ease;
}

.step-dot-pending{
    opacity: 0.6;
}

.step-dot-active{
    border-color: var(--amber);
    background: rgba(232,163,61,0.16);
    color: var(--amber);
    animation: pulse-amber 1.3s infinite;
}

.step-dot-complete{
    border-color: var(--green);
    background: rgba(79,209,165,0.16);
    color: var(--green);
}

.step-dot-error{
    border-color: var(--red);
    background: rgba(232,96,74,0.18);
    color: var(--red);
    animation: pulse-red 1.1s infinite;
}

.step-text{
    font-size: 13px;
    color: var(--text);
    padding-top: 1px;
}

/* ---------- Inputs ---------- */

.stTextArea textarea{
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'Inter', sans-serif !important;
}

.stTextArea textarea:focus{
    border: 1px solid var(--amber) !important;
    box-shadow: 0 0 0 1px var(--amber) !important;
}

/* ---------- Button ---------- */

div.stButton > button{
    background: linear-gradient(135deg, #E8A33D, #C9832A);
    color: #14100A;
    border: none;
    border-radius: 10px;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 15px;
    padding: 0.6rem 1rem;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

div.stButton > button:hover{
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(232,163,61,0.28);
    color: #14100A;
}

/* ---------- Alerts / Expanders / Misc ---------- */

[data-testid="stAlert"]{
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
}

.streamlit-expanderHeader{
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

hr{
    border-color: var(--border) !important;
}

code{
    font-family: 'JetBrains Mono', monospace !important;
}

</style>
""",
    unsafe_allow_html=True,
)

# ==========================================================
# Pipeline rendering helpers
# ==========================================================
# status: "idle" | "running" | "success" | "error"
# active_index: index (0-based) of the current / errored stage


def _node_state(i, active_index, status):
    if status == "success":
        return "complete"
    if status == "error":
        if i < active_index:
            return "complete"
        if i == active_index:
            return "error"
        return "pending"
    if status == "running":
        if i < active_index:
            return "complete"
        if i == active_index:
            return "active"
        return "pending"
    return "pending"


def render_main_pipeline(active_index=0, status="idle"):
    nodes_html = []
    for i, name in enumerate(STAGES):
        state = _node_state(i, active_index, status)
        nodes_html.append(
            f'<div class="pipe-node">'
            f'<div class="pipe-dot pipe-dot-{state}">{i + 1}</div>'
            f'<div class="pipe-label">{name}</div>'
            f'</div>'
        )
        if i < len(STAGES) - 1:
            line_state = "complete" if _node_state(i, active_index, status) == "complete" else "pending"
            line_cls = "pipe-line-complete" if line_state == "complete" else ""
            nodes_html.append(f'<div class="pipe-line {line_cls}"></div>')

    return f'<div class="pipeline">{"".join(nodes_html)}</div>'


def render_sidebar_stepper(active_index=0, status="idle"):
    items_html = []
    for i, name in enumerate(STAGES):
        state = _node_state(i, active_index, status)
        line_cls = "line-complete" if state == "complete" else ""
        items_html.append(
            f'<div class="step-item {line_cls}">'
            f'<div class="step-dot step-dot-{state}">{i + 1}</div>'
            f'<div class="step-text">{name.title()}</div>'
            f'</div>'
        )
    return f'<div class="stepper">{"".join(items_html)}</div>'


def run_status_caption(status, elapsed, active_index):
    if status == "running":
        return (
            f'<div class="run-status-row">'
            f'<span class="run-status-badge-running">● running · {STAGES[active_index]}</span>'
            f'<span>elapsed {elapsed:.0f}s</span>'
            f'</div>'
        )
    if status == "success":
        return (
            f'<div class="run-status-row">'
            f'<span class="run-status-badge-success">✓ completed</span>'
            f'<span>finished in {elapsed:.0f}s</span>'
            f'</div>'
        )
    if status == "error":
        return (
            f'<div class="run-status-row">'
            f'<span class="run-status-badge-error">✕ failed at {STAGES[active_index]}</span>'
            f'<span>after {elapsed:.0f}s</span>'
            f'</div>'
        )
    return '<div class="run-status-row"><span>idle · waiting for a request</span><span></span></div>'


# ==========================================================
# Header
# ==========================================================

st.markdown(
    """
<div class="eyebrow">Multi-Agent Document Generation System</div>
<div class="title">🤖 Autonomous AI Document Agent</div>
<div class="subtitle">FastAPI &nbsp;·&nbsp; LangGraph &nbsp;·&nbsp; Gemini &nbsp;·&nbsp; Streamlit</div>
<div class="hero-rule"></div>
""",
    unsafe_allow_html=True,
)

# ==========================================================
# Dashboard Metrics
# ==========================================================

st.markdown(
    """
<div class="telemetry-row">
    <div class="telemetry-card">
        <div class="telemetry-label">Agents</div>
        <div class="telemetry-value">6</div>
    </div>
    <div class="telemetry-card">
        <div class="telemetry-label">Workflow Nodes</div>
        <div class="telemetry-value">7</div>
    </div>
    <div class="telemetry-card">
        <div class="telemetry-label">LLM</div>
        <div class="telemetry-value">Gemini 2.5 Flash</div>
    </div>
    <div class="telemetry-card">
        <div class="telemetry-label">Output</div>
        <div class="telemetry-value">.DOCX</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.markdown('<div class="side-heading">⚙️ System Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-pill">● Backend Online</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#8B92A0; font-size:13px; margin-bottom:18px;">FastAPI + LangGraph runtime</div>', unsafe_allow_html=True)

    st.markdown('<div class="side-heading">🧠 Technologies</div>', unsafe_allow_html=True)
    st.markdown(
        """
<div style="margin: 10px 0 20px 0;">
<span class="tech-chip">FastAPI</span>
<span class="tech-chip">LangGraph</span>
<span class="tech-chip">Gemini 2.5 Flash</span>
<span class="tech-chip">Python</span>
<span class="tech-chip">Streamlit</span>
<span class="tech-chip">python-docx</span>
<span class="tech-chip">Pydantic</span>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="side-heading">📊 Autonomous Workflow</div>', unsafe_allow_html=True)

    # Live-updating placeholder — reused by the run loop below.
    sidebar_stepper_placeholder = st.empty()
    sidebar_stepper_placeholder.markdown(
        render_sidebar_stepper(active_index=0, status="idle"),
        unsafe_allow_html=True,
    )

# ==========================================================
# Workflow Overview
# ==========================================================

st.markdown('<div class="section-label">System Architecture</div>', unsafe_allow_html=True)
st.subheader("Autonomous Workflow")

main_pipeline_placeholder = st.empty()
main_pipeline_placeholder.markdown(
    render_main_pipeline(active_index=0, status="idle"),
    unsafe_allow_html=True,
)

run_status_placeholder = st.empty()
run_status_placeholder.markdown(
    run_status_caption("idle", 0, 0),
    unsafe_allow_html=True,
)


# ==========================================================
# User Request
# ==========================================================

st.markdown('<div class="section-label">Input</div>', unsafe_allow_html=True)
st.subheader("Business Request")

st.write(
    "Enter your business requirement below. "
    "The Autonomous AI Agent will analyze the request, "
    "plan the workflow, make assumptions where necessary, "
    "generate a professional document, and export it as a Microsoft Word file."
)

request = st.text_area(
    label="Business Requirement",
    value="",
    height=250,
    placeholder="Type your request here...",
)

generate = st.button(
    "🚀 Generate Document",
    use_container_width=True,
)

st.divider()


# ==========================================================
# Backend call (runs in a background thread so the pipeline
# can keep animating live instead of freezing on a spinner)
# ==========================================================

def call_backend(payload, result_box):
    try:
        resp = requests.post(API_URL, json=payload, timeout=TIMEOUT_SECONDS)
        result_box["response"] = resp
    except requests.exceptions.ConnectionError as e:
        result_box["error"] = ("connection", e)
    except requests.exceptions.Timeout as e:
        result_box["error"] = ("timeout", e)
    except Exception as e:
        result_box["error"] = ("other", e)


# ==========================================================
# Backend Integration
# ==========================================================

if generate:

    if not request.strip():

        st.warning("⚠️ Please enter a business request.")

        st.stop()

    result_box = {}
    worker = threading.Thread(
        target=call_backend,
        args=({"request": request}, result_box),
        daemon=True,
    )

    start_time = time.time()
    worker.start()

    active_index = 0
    max_index_while_running = len(STAGES) - 2  # hold just before RESPOND until the real answer lands

    # ---- live progress loop -------------------------------
    while worker.is_alive():

        elapsed = time.time() - start_time
        active_index = min(int(elapsed // SECONDS_PER_STAGE), max_index_while_running)

        main_pipeline_placeholder.markdown(
            render_main_pipeline(active_index=active_index, status="running"),
            unsafe_allow_html=True,
        )
        sidebar_stepper_placeholder.markdown(
            render_sidebar_stepper(active_index=active_index, status="running"),
            unsafe_allow_html=True,
        )
        run_status_placeholder.markdown(
            run_status_caption("running", elapsed, active_index),
            unsafe_allow_html=True,
        )

        time.sleep(0.5)

    worker.join()
    total_elapsed = time.time() - start_time

    # ---- resolve final pipeline state ----------------------
    if "error" in result_box:

        main_pipeline_placeholder.markdown(
            render_main_pipeline(active_index=active_index, status="error"),
            unsafe_allow_html=True,
        )
        sidebar_stepper_placeholder.markdown(
            render_sidebar_stepper(active_index=active_index, status="error"),
            unsafe_allow_html=True,
        )
        run_status_placeholder.markdown(
            run_status_caption("error", total_elapsed, active_index),
            unsafe_allow_html=True,
        )

        kind, e = result_box["error"]

        if kind == "connection":

            st.error(
                """
🚫 Unable to connect to FastAPI.

Please start the backend first.

Command:

python -m uvicorn main:app --reload
"""
            )

        elif kind == "timeout":

            st.error(
                f"⌛ Request timed out after {TIMEOUT_SECONDS}s. "
                "If the backend genuinely needs longer than this, raise TIMEOUT_SECONDS at the top of this file."
            )

        else:

            st.exception(e)

    else:

        main_pipeline_placeholder.markdown(
            render_main_pipeline(active_index=len(STAGES) - 1, status="success"),
            unsafe_allow_html=True,
        )
        sidebar_stepper_placeholder.markdown(
            render_sidebar_stepper(active_index=len(STAGES) - 1, status="success"),
            unsafe_allow_html=True,
        )
        run_status_placeholder.markdown(
            run_status_caption("success", total_elapsed, len(STAGES) - 1),
            unsafe_allow_html=True,
        )

        response = result_box["response"]

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Document Generated Successfully!")

            st.divider()

            # ==========================================
            # Full JSON Response
            # ==========================================

            st.subheader("📦 API Response")

            st.json(result)

            st.divider()

            # ==========================================
            # Success Message
            # ==========================================

            if isinstance(result, dict):

                if result.get("message"):

                    st.subheader("💬 Response Message")

                    st.success(result["message"])

                # --------------------------------------

                if result.get("output_file"):

                    st.subheader("📄 Generated Word Document")

                    st.code(result["output_file"])

                # --------------------------------------

                if result.get("generated_content"):

                    st.subheader("📝 Generated Content")

                    st.markdown(result["generated_content"])

                # --------------------------------------

                if result.get("execution_plan"):

                    with st.expander(
                        "📋 Execution Plan",
                        expanded=True,
                    ):

                        for step in result["execution_plan"]:

                            st.write(f"✅ {step}")

                # --------------------------------------

                if result.get("assumptions"):

                    with st.expander(
                        "🧠 Assumptions",
                        expanded=True,
                    ):

                        for assumption in result["assumptions"]:

                            st.write(f"• {assumption}")

                # --------------------------------------

                if result.get("reflection_feedback"):

                    with st.expander(
                        "🔍 Reflection Feedback",
                        expanded=True,
                    ):

                        st.write(
                            result["reflection_feedback"]
                        )

        else:

            st.error(
                f"❌ Backend Error ({response.status_code})"
            )

            try:

                st.json(response.json())

            except Exception:

                st.text(response.text)