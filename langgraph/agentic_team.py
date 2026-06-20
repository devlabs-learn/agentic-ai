from __future__ import annotations

import os

from groq import Groq
from typing import Optional
from openai import OpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file if present

def call_openai(prompt: str, system: Optional[str] = None) -> str:
    """Call OpenAI ChatCompletion (simple wrapper) or return a mock response.
    Keeps behaviour deterministic when `OPENAI_API_KEY` is not set.
    """
    client = OpenAI()
    
    messages = []
    if system:
        messages.append({"role": "system", "content": system})

    messages.append({"role": "user", "content": prompt})

    resp = client.chat.completions.create(
        model="gpt-4.1-mini", 
        messages=messages, 
        temperature=0.7
    )

    return resp.choices[0].message.content.strip()

def call_groq_ai(prompt: str, system: Optional[str] = None) -> str:
    client = Groq()

    messages = []
    if system:
        messages.append({"role": "system", "content": system})

    messages.append({"role": "user", "content": prompt})

    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=messages, 
        temperature=0.7
    )

    return resp.choices[0].message.content.strip()


class TeamState(dict):
    task: str = ""
    requirements: str = ""
    implementation_plan: str = ""
    code_snippet: str = ""
    review_comments: str = ""
    test_plan: str = ""
    review_decision: str = ""
    bugs: str = ""
    review_count: int = 0


def analyst_agent(state: TeamState) -> TeamState:

    print(f"Analyst Agent: Analyzing task: {state['task']}")

    prompt = (
        f"You are a business analyst. Given the user goal: {state['task']}, "
        "extract a concise set of functional requirements and acceptance criteria. "
        "Return as short bullet points."
    )

    state["requirements"] = call_groq_ai(prompt)
    return state


def developer_agent(state: TeamState) -> TeamState:
    prompt = (
        "You are a pragmatic software engineer. Given these requirements:\n"
        f"{state['requirements']}\n\n"
        "Produce a short implementation plan (steps) and a small example code snippet "
        "that demonstrates a core function or API for the feature."
    )
    out = call_groq_ai(prompt)
    # naive split between plan and code for display purposes
    state["implementation_plan"] = out
    return state


def reviewer_agent(state: TeamState) -> TeamState:
    prompt = (
        "You are a senior reviewer. Review the implementation plan and snippet "
        "below for correctness, edge-cases, and maintainability. Provide short "
        "review comments and suggested changes.\n\n"
        f"Plan:\n{state['implementation_plan']}\n"
    )
    state["review_comments"] = call_groq_ai(prompt)
    # state["review_decision"] = "changes requested" if "changes" in state["review_comments"].lower() else "approved"
    state["review_decision"] = "approved"  # For simplicity, we approve all plans in this example
    state["review_count"] += 1

    return state


def tester_agent(state: TeamState) -> TeamState:
    prompt = (
        "You are a QA engineer. Based on the requirements and the implementation plan, "
        "write a concise test plan and list likely bugs or edge-cases to validate.\n\n"
        f"Requirements:\n{state['requirements']}\n\nPlan:\n{state['implementation_plan']}"
    )
    out = call_groq_ai(prompt)
    # naive split: store as test_plan and bugs concatenated
    state["test_plan"] = out
    return state

def decide_next_node(state: TeamState) -> str:
    # MAX REVIEW condition to terminate review loop
    if state.get('review_count') > 3:
        return "tester"
    
    if state.get("review_decision") == "approved":
        return "tester"
    else:
        return "developer"

def build_agentic_team_graph() -> StateGraph:
    graph = StateGraph(TeamState)

    graph.add_node("analyst", analyst_agent)
    graph.add_node("developer", developer_agent)
    graph.add_node("reviewer", reviewer_agent)
    graph.add_node("tester", tester_agent)

    graph.add_edge(START, "analyst")
    graph.add_edge("analyst", "developer")
    graph.add_edge("developer", "reviewer")

    # Conditional edges based on review decision
    # The second argument must be a callable that returns the next node name.
    graph.add_conditional_edges("reviewer", decide_next_node)

    graph.add_edge("tester", END)

    return graph.compile()


def main() -> int:
    initial_task = "Design a feature that allows users to save their favorite items in a shopping app, and implement it with an agentic team of an analyst, developer, reviewer, and tester."

    graph = build_agentic_team_graph()

    result = graph.invoke(
        TeamState(task=initial_task)
    )

    print("\n--- Agentic Team Run ---\n")
    print("Task:", result.get("task"))
    print("\nRequirements:\n", result.get("requirements"))
    print("\nImplementation Plan:\n", result.get("implementation_plan"))
    print("\nReview Comments:\n", result.get("review_comments"))
    print("\nTest Plan & Bugs:\n", result.get("test_plan"))

    with open("agentic_team_output.md", "w") as f:
        f.write("--- Agentic Team Run ---\n\n")
        f.write(f"Task: {result.get('task')}\n\n")
        f.write(f"Requirements:\n{result.get('requirements')}\n\n")
        f.write(f"Implementation Plan:\n{result.get('implementation_plan')}\n\n")
        f.write(f"Review Comments:\n{result.get('review_comments')}\n\n")
        f.write(f"Test Plan & Bugs:\n{result.get('test_plan')}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
