"""
agents/research.py

Sequential research team: two ADK Agents run one after another.
Each searches from a different angle — latest news and expert analysis/trends.
Uses DuckDuckGo web search (works with any LLM, no extra API key needed).
Model: GPT-4.1 via Qubrid AI (OpenAI-compatible endpoint).
"""

from google.adk.agents import Agent, SequentialAgent  # type: ignore
from google.adk.models.lite_llm import LiteLlm  # type: ignore

from config.settings import QUBRID_MODEL_GPT41, QUBRID_API_KEY, QUBRID_BASE_URL, RESEARCH_PROMPT
from tools.search_tools import web_search_tool

_model = LiteLlm(model=QUBRID_MODEL_GPT41, api_key=QUBRID_API_KEY, api_base=QUBRID_BASE_URL)

# ── Individual searchers ───────────────────────────────────────────────────────

news_agent_1 = Agent(
    name="news_searcher_1",
    model=_model,
    instruction=RESEARCH_PROMPT + "\n\nFocus on: latest news and breaking announcements.",
    tools=[web_search_tool],
)

news_agent_2 = Agent(
    name="news_searcher_2",
    model=_model,
    instruction=RESEARCH_PROMPT + "\n\nFocus on: expert analysis, opinions, and future trends.",
    tools=[web_search_tool],
)

# ── SequentialAgent — avoids rate-limit bursts ────────────────────────────────

research_agent = SequentialAgent(
    name="research_team",
    sub_agents=[news_agent_1, news_agent_2],
)
