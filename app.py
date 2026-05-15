# app.py

import streamlit as st
from pipeline import run_research_pipeline
import time

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #0B1120;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.main-title {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #22D3EE, #A855F7, #EC4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #94A3B8;
    margin-bottom: 40px;
    font-size: 1.1rem;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.agent-card {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 15px;
    backdrop-filter: blur(10px);
}

.report-box {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
}

.stTextArea textarea {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 15px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    padding: 15px !important;
}

.stButton button {
    width: 100%;
    height: 3.2rem;
    border-radius: 15px;
    border: none;
    font-size: 1rem;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #06B6D4, #8B5CF6, #EC4899);
    transition: 0.3s ease;
}

.stButton button:hover {
    transform: scale(1.02);
    opacity: 0.95;
}

.sidebar .sidebar-content {
    background-color: #111827;
}

hr {
    border-color: rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:
    st.markdown("## ⚡ Research Workspace")
    st.markdown("---")

    st.markdown("""
### Features
- Multi-Agent Pipeline
- AI Report Generation
- Web Research
- Critic Review
- Smart Summaries
""")

    st.markdown("---")

    st.markdown("""
### Agents
Search Agent  
Reader Agent  
Writer Chain  
Critic Chain  
""")

# ---------------- HEADER ---------------- #

st.markdown(
    '<div class="main-title">Multi-Agent AI Research Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Research any topic using AI agents, web scraping, report generation, and critique workflows.</div>',
    unsafe_allow_html=True
)

# ---------------- INPUT AREA ---------------- #

topic = st.text_area(
    "Research Topic",
    placeholder="Example: Future of AI Agents in Healthcare"
)

start = st.button(" Start Research")

# ---------------- MAIN WORKFLOW ---------------- #

if start:

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    # Progress UI

    st.markdown("## Agent Workflow")

    search_box = st.empty()
    reader_box = st.empty()
    writer_box = st.empty()
    critic_box = st.empty()

    result_container = st.container()

    try:

        # SEARCH AGENT

        search_box.markdown("""
        <div class="agent-card">
         <b>Search Agent</b><br>
        Searching reliable sources...
        </div>
        """, unsafe_allow_html=True)

        time.sleep(1)

        # READER AGENT

        reader_box.markdown("""
        <div class="agent-card">
        <b>Reader Agent</b><br>
        Scraping and extracting important content...
        </div>
        """, unsafe_allow_html=True)

        time.sleep(1)

        # WRITER AGENT

        writer_box.markdown("""
        <div class="agent-card">
         <b>Writer Chain</b><br>
        Generating structured research report...
        </div>
        """, unsafe_allow_html=True)

        time.sleep(1)

        # CRITIC AGENT

        critic_box.markdown("""
        <div class="agent-card">
         <b>Critic Chain</b><br>
        Reviewing report quality and consistency...
        </div>
        """, unsafe_allow_html=True)

        # RUN PIPELINE

        result = run_research_pipeline(topic)

        # SUCCESS STATES

        search_box.markdown("""
        <div class="agent-card">
        <b>Search Agent Completed</b>
        </div>
        """, unsafe_allow_html=True)

        reader_box.markdown("""
        <div class="agent-card">
        <b>Reader Agent Completed</b>
        </div>
        """, unsafe_allow_html=True)

        writer_box.markdown("""
        <div class="agent-card">
        <b>Writer Chain Completed</b>
        </div>
        """, unsafe_allow_html=True)

        critic_box.markdown("""
        <div class="agent-card">
         <b>Critic Chain Completed</b>
        </div>
        """, unsafe_allow_html=True)

        # ---------------- RESULTS ---------------- #

        st.markdown("##  Research Results")

        tab1, tab2, tab3 = st.tabs([
            "Final Report",
            "Research Data",
            "Critic Feedback"
        ])

        # REPORT TAB

        with tab1:
            st.markdown(f"""
            <div class="report-box">
            {result['report']}
            </div>
            """, unsafe_allow_html=True)

        # RESEARCH TAB

        with tab2:

            st.markdown("### Search Results")

            st.markdown(f"""
            <div class="report-box">
            {result['search_result']}
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Scraped Content")

            st.markdown(f"""
            <div class="report-box">
            {result['reader_result']}
            </div>
            """, unsafe_allow_html=True)

        # FEEDBACK TAB

        with tab3:

            st.markdown(f"""
            <div class="report-box">
            {result['feedback']}
            </div>
            """, unsafe_allow_html=True)

        # DOWNLOAD BUTTON

        st.download_button(
            label=" Download Report",
            data=result['report'],
            file_name="research_report.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")