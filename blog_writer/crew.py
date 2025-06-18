from crewai import Crew, Process
from agent import blog_researcher, blog_writer
from tasks import research_task, writing_task
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LITELLM_PROVIDER"] = "groq/llama3-70b-8192"
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

crew = Crew(
    name="Blog Writer Crew",
    description="A crew that writes blogs based on YouTube channel information.",
    tasks=[research_task, writing_task],
    agents=[blog_researcher, blog_writer],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True,
)
        
result = crew.kickoff(
    inputs={
        "topic": "AI vs ml vs ds",
        "current_year": "2023"
    }
)

print(result)