"""
tools/search_tools.py

Web search tool for NewsletterAgent research agents.
Uses DuckDuckGo (no API key required) so it works with any LLM backend,
including Qubrid-hosted models via LiteLLM.
"""

import json
try:
    from ddgs import DDGS  # type: ignore  # new package name
except ImportError:
    from duckduckgo_search import DDGS  # type: ignore  # fallback
from google.adk.tools import FunctionTool  # type: ignore


def web_search(query: str, max_results: int = 5) -> str:
    """Search the web for recent news and return structured results.

    Args:
        query: Search query string.
        max_results: Maximum number of results to return (default 5).

    Returns:
        JSON string with a list of results, each containing
        title, url, body (snippet), and published date.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.news(query, max_results=max_results))
            if not results:
                # Fall back to text search if no news results
                results = list(ddgs.text(query, max_results=max_results))
            simplified = [
                {
                    "title": r.get("title", ""),
                    "url": r.get("url", r.get("href", "")),
                    "summary": r.get("body", r.get("snippet", "")),
                    "date": r.get("date", r.get("published", "recent")),
                    "source": r.get("source", r.get("url", "")),
                }
                for r in results
            ]
            return json.dumps(simplified, ensure_ascii=False, indent=2)
    except Exception as exc:
        return json.dumps({"error": str(exc)})


web_search_tool = FunctionTool(web_search)
