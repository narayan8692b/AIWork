#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:00:21 2025

@author: NarayanB
"""

import os
from crewai import Agent, Task, Crew, Process
from langchain.tools import Tool
from langchain.tools import DuckDuckGoSearchRun 

# Set environment variables for OpenAI API
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
os.environ["OPENAI_BASE_URL"] = "http://192.0.0.2:1234/v1"

# Define AI agents
query_classifier_agent = Agent(
    role='Query Classifier',
    goal='Identify the type of user request (billing, technical issue, general inquiry).',
    backstory="You are an AI-powered classifier that analyzes customer queries and categorizes them accurately.",
    verbose=True,
    allow_delegation=False
)

troubleshooting_agent = Agent(
    role='Troubleshooting Expert',
    goal='Provide step-by-step solutions for common issues.',
    backstory="You specialize in diagnosing and resolving common technical and billing-related issues.",
    verbose=True,
    allow_delegation=False
)

escalation_agent = Agent(
    role='Escalation Handler',
    goal='Route unresolved queries to human agents or prioritize urgent issues.',
    backstory="You determine when an issue needs human intervention and escalate accordingly.",
    verbose=True,
    allow_delegation=False
)

# Define tasks
query_classification_task = Task(
    description="Analyze incoming customer queries and classify them into predefined categories.",
    agent=query_classifier_agent,
    expected_output="A categorized list of customer queries."
)

troubleshooting_task = Task(
    description="Provide detailed troubleshooting steps for classified customer issues.",
    agent=troubleshooting_agent,
    expected_output="A structured guide for resolving common customer issues."
)

escalation_task = Task(
    description="Determine if a query requires human intervention and escalate if necessary.",
    agent=escalation_agent,
    expected_output="A prioritized list of escalated customer issues."
)

# Define AI Crew
customer_support_crew = Crew(
    agents=[query_classifier_agent, troubleshooting_agent, escalation_agent],
    tasks=[query_classification_task, troubleshooting_task, escalation_task],
    verbose=True,
    process=Process.sequential
)

# Execute AI workflow
result = customer_support_crew.kickoff()

print("######################")
print(result)
