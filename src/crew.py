'''
USING PYTHON 3.11.9
'''

from crewai import Agent, Crew, Task, Process, LLM
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from dotenv import load_dotenv
load_dotenv()


# Define the class for the crew
@CrewBase
class ResearchAndBlogCrew():

    # define for the crew method
    agents: list[BaseAgent]
    tasks: list[Task]

    # define the paths of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    ## llm configuration (if required)
    # ollama_llm = LLM(
    #     model="ollama/deepseek-v3.1:671b-cloud",
    #     base_url="http://localhost:11434"
    # )

    # =========== AGENTS ===========

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator"],
            # llm=self.ollama_llm,
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
            # llm=self.ollama_llm,

        )

    # =========== TASKS ===========
    # order of tasks matters

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
            output_file="outputs/research_report.md",
        )

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file="outputs/blog_post.md",
        )

    # =========== CREW ===========

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
