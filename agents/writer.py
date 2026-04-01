"""
agents/writer.py

Newsletter writer agent: drafts full newsletter copy — headlines, summaries, closing.
Model: Claude Sonnet 3.5 via Qubrid AI (forced through OpenAI-compatible endpoint).
custom_llm_provider="openai" makes LiteLLM use OpenAI format so Qubrid receives
the model name "anthropic/claude-3-5-sonnet-20241022" correctly.
"""

from google.adk.agents import Agent  # type: ignore
from google.adk.models.lite_llm import LiteLlm  # type: ignore

from config.settings import QUBRID_MODEL_CLAUDE35, QUBRID_API_KEY, QUBRID_BASE_URL, WRITER_PROMPT

writer_agent = Agent(
    name="newsletter_writer",
    model=LiteLlm(
        model=QUBRID_MODEL_CLAUDE35,
        api_key=QUBRID_API_KEY,
        api_base=QUBRID_BASE_URL,
        custom_llm_provider="openai",
    ),
    instruction=(
        WRITER_PROMPT + "\n\nUse the requested user tone from the conversation "
        "and transform the filtered stories into final newsletter copy."
    ),
)
