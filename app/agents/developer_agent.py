from crewai import Agent

developer_agent = Agent(
    role="Software Developer",
    goal="Write clean scalable code",
    backstory="Senior AI software engineer",
    verbose=True
)