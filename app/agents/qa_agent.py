from crewai import Agent

qa_agent = Agent(
    role="QA Engineer",
    goal="Verify quality and detect issues",
    backstory="Expert software tester",
    verbose=True
)