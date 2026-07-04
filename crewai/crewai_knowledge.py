from crewai import Crew, Agent, Task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

docs = PDFKnowledgeSource(
    chunk_size=4000,
    chunk_overlap=500,
    file_paths = [
        "docs/FA1_syllabus.pdf",
        "docs/elevate.pdf",
    ]
)

# Create agent instance
agent = Agent(
    role="Personal Assistant",
    goal="Assist the user with various tasks and provide helpful information.",
    backstory="A highly skilled and knowledgeable personal assistant designed to help users with their daily tasks and provide accurate information on a wide range of topics." 
)


task = Task(
    description="Assist user in answering query: {query}",
    expected_output="User receives accurate and helpful information in response to their queries.",
    agent = agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    knowledge_sources=[docs],
    # memory = True,
)

result = crew.kickoff(inputs={"query": "when is ICT exam?"})

print(result)