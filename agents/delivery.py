"""
agents/delivery.py

Delivery agent: validates that the formatted HTML newsletter is ready
for manual send confirmation in the UI. Actual sending is via Composio
through the /api/send endpoint — this agent only confirms readiness.
Model: GPT-4.1 via Qubrid AI (OpenAI-compatible endpoint).
"""

from google.adk.agents import Agent  # type: ignore
from google.adk.models.lite_llm import LiteLlm  # type: ignore

from config.settings import QUBRID_MODEL_GPT41, QUBRID_API_KEY, QUBRID_BASE_URL, DELIVERY_PROMPT

delivery_agent = Agent(
    name="email_delivery",
    model=LiteLlm(model=QUBRID_MODEL_GPT41, api_key=QUBRID_API_KEY, api_base=QUBRID_BASE_URL),
    instruction=DELIVERY_PROMPT,
)
