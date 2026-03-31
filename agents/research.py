"""
agents/research.py

Parallel research team: three ADK Agents run simultaneously, each using a
different Qubrid-hosted model to spread load across separate rate-limit buckets.
Each agent searches from a different angle — latest news, expert analysis, trends.
Uses DuckDuckGo web search (works with any LLM, no extra API key needed).
"""

from google.adk.agents import Agent, SequentialAgent  # type: ignore
from google.adk.models.lite_llm import LiteLlm  # type: ignore

from config.settings import QUBRID_MODEL_GPT, QUBRID_API_KEY, QUBRID_BASE_URL, RESEARCH_PROMPT
from tools.search_tools import web_search_tool

qubrid_gpt = LiteLlm(
    model=QUBRID_MODEL_GPT,
    api_key=QUBRID_API_KEY,
    api_base=QUBRID_BASE_URL
)

# ── Individual searchers ───────────────────────────────────────────────────────

news_agent_1 = Agent(
    name="news_searcher_1",
    model=qubrid_gpt,
    instruction=RESEARCH_PROMPT + "\n\nFocus on: latest news and announcements.",
    tools=[web_search_tool],
)

news_agent_2 = Agent(
    name="news_searcher_2",
    model=qubrid_gpt,
    instruction=RESEARCH_PROMPT + "\n\nFocus on: expert analysis and opinions.",
    tools=[web_search_tool],
)

news_agent_3 = Agent(
    name="news_searcher_3",
    model=qubrid_gpt,
    instruction=RESEARCH_PROMPT + "\n\nFocus on: trends and future outlook.",
    tools=[web_search_tool],
)

# ── SequentialAgent — space out requests to avoid rate limits ─────────────────

research_agent = SequentialAgent(
    name="research_team",
    sub_agents=[news_agent_1, news_agent_2, news_agent_3],
)
