#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:14:44 2025

@author: SFN
"""

import os
from crewai import Agent, Task, Crew, Process
from langchain.tools import Tool
from langchain.tools import DuckDuckGoSearchRun 

# Set environment variables for OpenAI API
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
os.environ["OPENAI_BASE_URL"] = "http://192.0.0.2:1234/v1"

# Define AI agents
script_writer_agent = Agent(
    role='Script Writer',
    goal='Generate engaging short video scripts.',
    backstory="You are a skilled scriptwriter who creates concise and compelling scripts for short-form videos.",
    verbose=True,
    allow_delegation=False
)

voiceover_generator_agent = Agent(
    role='Voiceover Generator',
    goal='Generate voiceovers from scripts.',
    backstory="You use text-to-speech technology to convert scripts into high-quality voiceovers.",
    verbose=True,
    allow_delegation=False
)

video_editor_agent = Agent(
    role='Video Editor',
    goal='Create short videos by combining visuals, text, and voiceovers.',
    backstory="You are an AI-powered video editor that assembles clips, overlays text, and syncs voiceovers for engaging videos.",
    verbose=True,
    allow_delegation=False
)

# Define tasks
script_writing_task = Task(
    description="Generate a short video script based on a given topic.",
    agent=script_writer_agent,
    expected_output="A concise and engaging video script."
)

voiceover_task = Task(
    description="Convert the generated script into a natural-sounding voiceover.",
    agent=voiceover_generator_agent,
    expected_output="A high-quality voiceover for the video."
)

video_editing_task = Task(
    description="Create a short video by integrating the script, visuals, and voiceover.",
    agent=video_editor_agent,
    expected_output="A complete short-form video ready for distribution."
)

# Define AI Crew
short_video_crew = Crew(
    agents=[script_writer_agent, voiceover_generator_agent, video_editor_agent],
    tasks=[script_writing_task, voiceover_task, video_editing_task],
    verbose=True,
    process=Process.sequential
)

# Execute AI workflow
result = short_video_crew.kickoff()

print("######################")
print(result)
