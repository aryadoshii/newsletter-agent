"""
agents/formatter.py

HTML formatter agent: converts written newsletter copy into a
Summer Breeze-themed, email-client-compatible HTML document.
Model: Claude Sonnet 3.5 via Qubrid AI (OpenAI-compatible endpoint).
"""

from google.adk.agents import Agent  # type: ignore
from google.adk.models.lite_llm import LiteLlm  # type: ignore

from config.settings import QUBRID_MODEL_CLAUDE35, QUBRID_API_KEY, QUBRID_BASE_URL, FORMATTER_PROMPT

formatter_agent = Agent(
    name="html_formatter",
    model=LiteLlm(
        model=QUBRID_MODEL_CLAUDE35,
        api_key=QUBRID_API_KEY,
        api_base=QUBRID_BASE_URL,
        custom_llm_provider="openai",
    ),
    instruction=FORMATTER_PROMPT,
)
