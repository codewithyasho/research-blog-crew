'''
USING PYTHON 3.11.9
'''

from src.crew import ResearchAndBlogCrew


"""Run the Crew"""

inputs = {
    "topic": "Electric Vehicles",
}

ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
