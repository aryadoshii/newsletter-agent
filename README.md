# 📰 NewsletterAgent

> **Research. Write. Deliver.** — An agentic AI newsletter pipeline built with Google ADK, Qubrid AI, and Composio.

NewsletterAgent automatically researches a topic, filters the most relevant articles, writes a full newsletter, formats it into a beautiful HTML email, and delivers it to your Gmail or Outlook inbox — all with a single click.

---

## ✨ Features

- 🤖 **Multi-Agent Pipeline** — 5 specialized agents: Researcher, Filter, Writer, Formatter, Delivery
- ⚡ **Live Streaming** — Watch agents think and write in real-time (Gemini-style typewriter effect)
- 📧 **Gmail & Outlook** — Send directly or save as draft to either account
- 🎨 **Premium UI** — Beautiful Streamlit frontend with Burnt Sienna design palette
- 📝 **Session History** — All past newsletters saved with metadata in a local SQLite database
- 🔁 **Built on Google ADK** — Fully compatible with Google Agent Development Kit

---

## 🏗️ Architecture

```
┌─────────────┐    ┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│ ResearchTeam│───▶│ContentFilter│───▶│NewsletterWrit│───▶│HTMLFormatter│───▶│DeliveryAgent │
│  (Tavily)   │    │  (LiteLLM)  │    │er (LiteLLM)  │    │ (LiteLLM)   │    │ (Composio)   │
└─────────────┘    └─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
```

**Stack:** Google ADK · LiteLLM (GPT-4.1 & Claude Sonnet 3.5) · Composio · FastAPI · Streamlit · SQLite

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aryadoshii/newsletter-agent.git
cd newsletter-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and fill in:

```env
# Qubrid AI (for LiteLLM models)
QUBRID_API_KEY=your_qubrid_api_key
QUBRID_BASE_URL=https://api.qubrid.com/v1

# Composio (for Gmail & Outlook delivery)
COMPOSIO_API_KEY=your_composio_api_key
COMPOSIO_ENTITY_ID=default

# Tavily (for web research)
TAVILY_API_KEY=your_tavily_api_key
```

Get your keys:
- **Qubrid AI**: [app.qubrid.com](https://app.qubrid.com) → API Keys
- **Composio**: [app.composio.dev](https://app.composio.dev) → Settings → API Keys
- **Tavily**: [app.tavily.com](https://app.tavily.com) → API Keys

---

### 5. Connect Email Accounts via Composio

NewsletterAgent uses **Composio** to send emails via your Gmail and/or Outlook accounts through secure OAuth — no passwords stored.

#### Install Composio CLI (if not already installed)

```bash
pip install composio-core
composio login   # paste your API key when prompted
```

#### Connect Gmail

```bash
composio add gmail
```

Follow the browser URL it prints → sign in with Google → grant permissions.

#### Connect Outlook / Microsoft 365

```bash
composio add outlook
```

Follow the browser URL → sign in with Microsoft → grant permissions.

#### Verify Connections

```bash
composio connections
```

You should see both `gmail` and `outlook` status as `ACTIVE`. Copy their connection IDs into your `.env` if prompted.

> **Tip:** If the Streamlit sidebar shows "Not connected", re-run the `composio add` command for that account.

---

### 6. Run the Application

You need **two terminals** running concurrently:

**Terminal 1 — FastAPI backend:**
```bash
uvicorn main:app --reload --port 8000
```

**Terminal 2 — Streamlit frontend:**
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## 🎮 Usage

1. **Enter a topic** — e.g. `AI in healthcare`, `crypto markets this week`, `climate tech trends`
2. **Choose tone & length** — Professional / Casual / Bold / Analytical × Short / Medium / Long
3. **Click ✨ Generate Newsletter** — Watch the 5-agent pipeline run live with streaming output
4. **Preview** your newsletter — Full rendered HTML preview in the app
5. **Deliver** — Choose:
   - **Action**: Send Email or Create Draft
   - **Platform**: Gmail or Outlook
   - Enter recipient email → confirm → done!

---

## 📁 Project Structure

```
newsletter-agent/
├── agents/              # Google ADK agents (research, filter, writer, formatter, delivery)
├── api/                 # FastAPI routes (pipeline trigger, send, health check)
├── config/              # App settings and constants
├── database/            # SQLite session store
├── frontend/            # Streamlit UI (components.py, styles.py)
├── tools/               # Email tools (Composio), Search tools (Tavily)
├── outputs/             # Generated HTML newsletters (gitignored)
├── app.py               # Streamlit entry point
├── main.py              # FastAPI entry point
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variable template
```

---

## 🔑 Environment Variables Reference

| Variable | Description | Required |
|---|---|---|
| `QUBRID_API_KEY` | Qubrid AI API key for LiteLLM model hosting | ✅ |
| `QUBRID_BASE_URL` | Qubrid AI base URL (e.g. `https://api.qubrid.com/v1`) | ✅ |
| `COMPOSIO_API_KEY` | Composio API key for email delivery | ✅ |
| `COMPOSIO_ENTITY_ID` | Composio entity ID (default: `default`) | ✅ |
| `TAVILY_API_KEY` | Tavily search API for the research agent | ✅ |

---

## 🛠️ Troubleshooting

**Email lands in Spam?**
This is normal for first-time OAuth sends via Composio. Open the email → click "Not Spam". Future emails will go to inbox.

**Composio connection errors?**
Run `composio connections` to verify status. If disconnected, re-run `composio add gmail` or `composio add outlook`.

**Port already in use?**
Change the FastAPI port: `uvicorn main:app --reload --port 8001` and update `API_BASE_URL` in `config/settings.py`.

**Model errors (429 / rate limits)?**
Ensure your `QUBRID_API_KEY` is valid and has sufficient credits at [app.qubrid.com](https://app.qubrid.com).

---

## 👤 Author

**Arya Doshi** — [github.com/aryadoshii](https://github.com/aryadoshii)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
