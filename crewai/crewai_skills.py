from crewai import Crew, Agent, Task
from pathlib import Path
from crewai.tools import BaseTool

class ReadFileTool(BaseTool):
    name: str = "read_file"
    description: str = "Reads the content of a file and returns it as a string."
    
    def _run(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")

agent = Agent(
    role='AI Assistant',
    goal='Perform task given by the user, providing accurate and helpful responses.',
    backstory='I am an AI assistant designed to help users with a variety of tasks, from answering questions to providing recommendations and performing specific actions. I have been trained on a diverse range of topics and can adapt to different contexts to assist users effectively.',
    tools=[ReadFileTool()]
)

task = Task(
    description='Assist the user with their requests: {request}',
    expected_output='The user receives accurate and helpful responses to their queries.',
    agent = agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    # verbose=True,
    # planning=True,
    skills=["./skills"]
)

# result = crew.kickoff(inputs={"request": "create a diagram to plan the project?"})
result = crew.kickoff(inputs={"request": "create a workflow diagram for learning AI?"})

print(result)