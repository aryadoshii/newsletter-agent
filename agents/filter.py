"""
agents/filter.py

Content filter agent: selects and ranks the top N stories
from the combined research output for the newsletter.
Model: GPT-4.1 via Qubrid AI (OpenAI-compatible endpoint).
"""

from google.adk.agents import Agent  # type: ignore
from google.adk.models.lite_llm import LiteLlm  # type: ignore

from config.settings import QUBRID_MODEL_GPT41, QUBRID_API_KEY, QUBRID_BASE_URL, FILTER_PROMPT

filter_agent = Agent(
    name="content_filter",
    model=LiteLlm(model=QUBRID_MODEL_GPT41, api_key=QUBRID_API_KEY, api_base=QUBRID_BASE_URL),
    instruction=FILTER_PROMPT,
)
