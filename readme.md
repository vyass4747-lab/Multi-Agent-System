#  Multi-Agent AI Research Assistant

A powerful AI research system built using LangChain, Mistral AI, Tavily Search, and Streamlit.

This project uses multiple AI agents to:

* search the web
* scrape relevant resources
* generate detailed reports
* review output quality
* provide structured AI-powered research

---

#  Features

✅ Multi-Agent Workflow
✅ AI-Powered Research Reports
✅ Web Search Integration
✅ Intelligent Content Scraping
✅ Critic Feedback System
✅ Beautiful Streamlit UI
✅ Modular Architecture
✅ Resume-Ready Project

---

#  Tech Stack

| Technology             | Usage               |
| ---------------------- | ------------------- |
| Python                 | Backend Logic       |
| LangChain              | Agent Orchestration |
| Mistral AI             | LLM                 |
| Tavily API             | Web Search          |
| Streamlit              | Frontend UI         |
| BeautifulSoup          | Web Scraping        |
| ChromaDB               | Vector Database     |
| HuggingFace Embeddings | Semantic Search     |

---

#  Project Architecture

```bash
User Query
   ↓
Search Agent
   ↓
Reader Agent
   ↓
Writer Chain
   ↓
Critic Chain
   ↓
Final Research Report
```


#

#  Screenshots

##  Home Interface

<img width="100%" alt="home-ui" src="D:\Multi Agent System\screenshots\Screenshot (176).png">

---

##  Agent Workflow

<img width="100%" alt="workflow" src="D:\Multi Agent System\screenshots\Screenshot (179).png">

---

##  Generated Research Report

<img width="100%" alt="report" src="D:\Multi Agent System\screenshots\Screenshot (180).png">

---

##  Critic Feedback System

<img width="100%" alt="critic" src="D:\Multi Agent System\screenshots\Screenshot (181).png">

---

#  Installation

## 1️ Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
cd AIResearchAssistant
```

---

## 2️ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3️ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️ Add Environment Variables

Create `.env` file:

```env
MISTRAL_API_KEY=your_key
TAVILY_API_KEY=your_key
```

---

#  Run Project

```bash
streamlit run app.py
```

---

#  How It Works

##  Search Agent

Searches the internet for reliable information related to the user query.

##  Reader Agent

Selects the best resources and extracts detailed content.

## Writer Chain

Generates a structured AI research report.

##  Critic Chain

Reviews the generated report and gives feedback for improvement.

---

#  Future Improvements

* PDF export
* Chat history
* Authentication
* Real-time streaming responses
* React frontend
* Multi-document research
* RAG integration
* Agent memory

---

#  Key Learnings

This project helped in understanding:

* Multi-Agent Systems
* LLM Orchestration
* LangChain Workflows
* Prompt Engineering
* Streamlit UI Development
* API Integration
* AI Product Architecture

---

# Deployment

Deploy easily using:

* Streamlit Community Cloud
* Render
* Railway
* HuggingFace Spaces

---

#  Author
Suhani Vyas 
Built with passion for AI Engineering and real-world AI systems.

---

#  Support

If you found this project useful, consider giving it a star on GitHub.
