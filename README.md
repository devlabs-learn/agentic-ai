# Agentic AI Training Sessions
This repository contains materials and guidance for hands-on training sessions to build Agentic AI solutions using tools such as crewai, LangGraph, AutoGen, and related libraries.
## Objective
Run practical workshops that teach participants how to design, implement, and evaluate agentic systems (multi-agent workflows, orchestration, task planning, memory, tools integration, and evaluation) using modern agent frameworks.
## Audience
- Developers and engineers familiar with Python and basic ML/LLM concepts.
- AI researchers and practitioners interested in agent orchestration and tool-augmented LLMs.
## Prerequisites
- Python 3.10+ installed
- Git
- Basic familiarity with Large Language Models (LLMs) and REST APIs
## Recommended Tools & Libraries
- crewai — agent orchestration and workflow patterns
- LangGraph — graph-based orchestration and dataflow for agents
- AutoGen — multi-agent simulation and coordination utilities
- OpenAI / local LLM runtime (e.g., vLLM, Llama) for model-backed agents
- Docker (optional, for environment isolation)
## Setup
1. Clone the repo:
```bash
git clone https://github.com/devlabs-learn/agentic-ai.git
cd agentic-ai
```

2. Create virtual environment and install core dependencies (example):
```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure credentials (e.g., OPENAI_API_KEY) in your environment or a .env file.
## Training Session Outline
Each session is designed for 60–120 minutes, combining short lectures, demos, and hands-on labs.

Session 1 — Introduction & Foundations
- Overview of agentic AI: concepts, use-cases, and system architecture
- Introduction to crewai, LangGraph, and AutoGen
- Simple single-agent demo (LLM prompt + tool)

Session 2 — Agent Design Patterns
- Task decomposition and planner patterns
- Memory and state management for agents
- Hands-on: build a planner agent that decomposes tasks

Session 3 — Multi-Agent Coordination
- Communication patterns, roles, and emergent behavior
- Use AutoGen to simulate role-based agents
- Hands-on: implement a coordinator + worker agents

Session 4 — Orchestration & Graph Workflows
- Build and visualize dataflows with LangGraph
- Integrate crewai orchestrations with LangGraph pipelines
- Hands-on: create an end-to-end pipeline connecting tools and LLMs

Session 5 — Tools, Connectors & Safety
- Integrating external tools (APIs, databases, search)
- Safety, guardrails, and human-in-the-loop design
- Hands-on: attach a search or retrieval tool and implement guardrails

Session 6 — Evaluation & Deployment
- Metrics for agentic systems (task success, efficiency, reliability)
- Lightweight deployment strategies and monitoring
- Final lab: end-to-end agentic application and evaluation

## Example Labs and Exercises
- Build a task-planner that converts user goals into subtasks and assigns them to worker agents.
- Create a retrieval-augmented agent that uses LangGraph to manage context and memory.
- Simulate multiple agents with AutoGen and measure throughput and task completion.
- Integrate a web API tool and secure calls with rate limits and error handling.

## Best Practices
- Modularize agents: separate planner, executor, and memory layers.
- Use small, testable components and unit tests for agent logic.
- Implement reproducible prompts and prompt-version control.
- Add observability: logs, traces, and metrics to understand agent behavior.

## Resources
- crewai docs: https://github.com/crewai (or official docs)
- LangGraph: https://github.com/langgraph
- AutoGen: https://github.com/microsoft/autogen
- Papers and articles on multi-agent systems, retrieval-augmented generation, and tool use with LLMs.

## Contributing
Contributions are welcome: add session materials, labs, slides, or demos. Open a PR with changes to this repository.

## License
Use the repository license that fits your organization. Add LICENSE file if needed.

```
