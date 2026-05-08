from crewai import Crew, Task

from app.agents.ceo_agent import ceo_agent
from app.agents.research_agent import research_agent
from app.agents.developer_agent import developer_agent
from app.agents.qa_agent import qa_agent
from app.agents.marketing_agent import marketing_agent


def run_company(goal: str):
    research_task = Task(
        description=f"Research the following request: {goal}",
        agent=research_agent
    )
    development_task = Task(
        description=f"Develop solution for: {goal}",
        agent=developer_agent
    )

    qa_task = Task(
        description="Validate the generated solution",
        agent=qa_agent
    )

    marketing_task = Task(
        description="Generate marketing strategy",
        agent=marketing_agent
    )
    company = Crew(
        agents=[
            ceo_agent,
            research_agent,
            developer_agent,
            qa_agent,
            marketing_agent
        ],
        tasks=[
            research_task,
            development_task,
            qa_task,
            marketing_task
        ],
        verbose=True
    )

    result = company.kickoff()

    return result