from crewai import Agent

research_agent = Agent(
    role="Research Analyst",
    goal="Research internet data and provide reports",
    backstory="Expert internet researcher and analyst",
    verbose=True
)