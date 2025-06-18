from crewai import Task
from tools import yt_tool
from blog_writer.agent import blog_researcher, blog_writer
# Task for the blog researcher to find relevant information from YouTube

research_task = Task(
    name="Research Topic",
    description=("identify the video {topic}."
    "Get details infromation about the video from the channel."),
    expected_output = "Relevant information about the topic from YouTube channel in 3 paragraph based on the {topic}.",
    agent=blog_researcher,
    tool=[yt_tool]
)


writing_task = Task(
    name="Write Topic",
    description=("get the inf for the youtube channel on the topic {topic}."
    "Gt details infromation about the video from the channel."),
    expected_output = "Summaize the info from the youtube channel video on the topic {topic}.",
    agent=blog_writer,
    tool=[yt_tool],
    async_execution=False,
    output_file = 'blogpost.md' 
)