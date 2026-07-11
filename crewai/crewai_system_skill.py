from crewai import Crew, Agent, Task
from crewai.tools import BaseTool

import subprocess

class TaskExecutorTool(BaseTool):
    name: str = 'execute'
    description: str = 'Execute system commands'

    def _run(self, command: str):
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False,
        )

        return result.stdout if result.stdout else result.stderr


agent = Agent(
    role='System Administator',
    goal='Execute system commands as per user instructions.',
    backstory='You are an expert system administatror',
    tools = [TaskExecutorTool()]
)

task = Task(
    description='Perform task: {task}',
    expected_output='Return task console logs.',
    agent = agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    skills=["./skills"]
)

result = crew.kickoff(inputs={"task": "List of md files current file"})

print(result)