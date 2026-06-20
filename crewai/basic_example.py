import streamlit as st

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

search_tool = SerperDevTool()
web_scrapper = ScrapeWebsiteTool()

research_agent = Agent(
    role = "You are a topic researcher",
    goal = "Research on {topic}, use tools to get latest content",
    backstory = """
        You're a seasoned researcher with a knack for uncovering the latest
        developments in {topic}. Known for your ability to find the most relevant
        information and present it in a clear and concise manner.
    """,
    tools = [search_tool, web_scrapper]
)

research_task = Task(
    description="Find latest development on {topic}",
    expected_output="Create a summary list of important developments",
    agent = research_agent
)

crew = Crew(
    agents = [research_agent],
    tasks = [research_task]
)

st.title("Topic Researcher Agent")
topic = st.chat_input("Your topic")
if topic:
    result = crew.kickoff(inputs = { "topic": topic})

    with st.chat_message("assistant"):
        st.markdown(str(result))

