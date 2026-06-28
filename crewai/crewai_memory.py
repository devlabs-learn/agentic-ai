from crewai import Crew, Agent, Task

topic_researcher_agent = Agent(
    role = 'Research Analyst',
    goal = 'Research on {topic} and return a summary of you findings',
    backstory="""
        You are an expert research of any subject
    """
)

research_task = Task(
    description = "Research on {topic}",
    expected_output = "A list of important points",
    agent = topic_researcher_agent
)

crew = Crew(
    agents=[topic_researcher_agent],
    tasks = [research_task],
    memory=True,
    verbose=True
)

results = crew.kickoff(inputs={"topic": "AI Agent Memory"})

print(results)