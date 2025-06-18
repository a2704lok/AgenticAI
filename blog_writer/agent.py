from crewai import Agent
from tools import yt_tool
import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")
assert groq_key, "Missing GROQ_API_KEY in environment"
os.environ["GROQ_API_KEY"] = groq_key


def litellm_wrapper(prompt):
    response = completion(
        model="groq/llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

blog_researcher = Agent(
    name="Blog Researcher",
    description="A blog researcher that finds relevant information and sources for blog posts.",
    role="Blog Researcher from youtube videos",
    goal='get the relevant video content for the topic from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding youtube videos for Machine learning and AI topics and providing suggestions"
    ),
    tool=[yt_tool],
    allow_delegation=True,
    llm=litellm_wrapper
)




blog_writer = Agent(
    name="Blog writing agent",
    description="Write tech story about the {topic} based on the information provided by the blog researcher.",
    role="Blog writer",
    goal='get the relevant video content for the topic from youtube channel',
    verbose=True,
    memory=True,
    backstory=("Expert in breaking down complex topics into simple and easy-to-understand blog posts"),
    tool=[yt_tool],
    allow_delegation=False,
    llm = litellm_wrapper
)
