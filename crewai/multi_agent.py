from crewai import Agent, Task, Crew, LLM

# llm = LLM(
#     model = "openai/gpt-4o",
# )

# Agent 1
stock_analyst_agent = Agent(
    # llm = "openai/gpt-4o",
    role = "Stock Trading Analyst",
    goal = "Analyse the stock - {stock} and return a summary of your analysis",
    backstory = """
        You are an expert stock analyst, good at anlysing stock fundamentals, technical analysis and market sentiment
    """,
    verbose = True
)

stock_analysis_task = Task(
    description="Analyse stock {stock}",
    expected_output="Summarize your analysis and return a list of important points",
    agent=stock_analyst_agent
)


# Agent 2
advisor_agent = Agent(
    # llm = "openai/gpt-4o",
    role = "Stock Adviser",
    goal = "Advise based on research summary to BUY, SELL or HOLD",
    backstory = """
        You are a stock adviser good at providing recommendations on taking market actions BUY, SELL, HOLD
    """,
    verbose = True
)

adviser_task = Task(
    description="Provide recommendation to BUY, SELL or HOLD based on stock analysis summary",
    expected_output="Return only SELL, BUY or HOLD",
    agent=advisor_agent,
    context=[stock_analysis_task]
)

crew = Crew(
    agents=[stock_analyst_agent, advisor_agent],
    tasks=[stock_analysis_task, adviser_task],
)

result = crew.kickoff(inputs={
    "stock": "APPL"
})

print(result)