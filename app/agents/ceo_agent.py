from crewai import Agent

ceo_agent = Agent(
    role="CEO",
    goal="Manage company operations and delegate tasks",
    backstory="Expert AI executive leading an autonomous AI company",
    verbose=True
)