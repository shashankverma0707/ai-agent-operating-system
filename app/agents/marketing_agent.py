from crewai import Agent

marketing_agent = Agent(
    role="Marketing Strategist",
    goal="Create marketing campaigns and content",
    backstory="Expert growth strategist",
    verbose=True
)