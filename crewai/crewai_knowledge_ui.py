from crewai import Crew, Agent, Task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

import streamlit as st

st.title("CrewAI Knowledge UI")

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

file_paths = []
files = st.sidebar.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
if files:
    for file in files:
        file_path = f"knowledge/docs/{file.name}"
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        file_paths.append(file_path.replace("knowledge/", "/"))  # Ensure consistent path format

    docs = PDFKnowledgeSource(
        chunk_size=4000,
        chunk_overlap=500,
        file_paths = file_paths
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        knowledge_sources=[docs],
        # embedder = EmbedderConfig(
                # 'provider': 'openai',
                # 'config': {
                #     'model': 'text-embedding-3-large',
                #     'api_key': st.secrets["OPENAI_API_KEY"]}
        # )
    )

    query = st.chat_input("Ask your question:")
    if query:
        result = crew.kickoff(inputs={"query": query})
        st.chat_message("assistant").write(result.raw)

