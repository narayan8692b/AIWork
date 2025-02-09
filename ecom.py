#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:39:25 2025

@author: NarayanB
"""

import os
from crewai import Agent, Task, Crew, Process
from langchain.tools import Tool
from langchain.tools import DuckDuckGoSearchRun 

# Set environment variables for OpenAI API
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
os.environ["OPENAI_BASE_URL"] = "http://192.0.0.2:1234/v1"

# Define a search tool for product research
search_tool = Tool(
    name="DuckDuckGo Search",
    func=DuckDuckGoSearchRun().run,
    description="Performs a web search using DuckDuckGo and retrieves the latest product trends and insights."
)

# Define AI agents
product_research_agent = Agent(
    role='Product Research Analyst',
    goal='Identify trending e-commerce products and gather market insights.',
    backstory="You are an expert market researcher who specializes in finding trending products, analyzing market demand, and gathering competitive insights.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

seo_content_writer_agent = Agent(
    role='SEO Content Writer',
    goal='Write compelling and SEO-optimized product descriptions.',
    backstory="You are an expert content writer with a deep understanding of SEO. You create engaging and optimized product descriptions that boost search rankings.",
    verbose=True,
    allow_delegation=False
)

ad_copy_generator_agent = Agent(
    role='Ad Copy Specialist',
    goal='Generate high-converting ad copy for social media marketing.',
    backstory="You specialize in crafting compelling ad copies for social media campaigns, driving customer engagement and conversions.",
    verbose=True,
    allow_delegation=False
)

# Define tasks
product_research_task = Task(
    description="Conduct research on the latest trending products in e-commerce and compile insights on market demand and competition.",
    agent=product_research_agent,
    expected_output="A detailed market research report on trending products."
)

seo_content_task = Task(
    description="Using the product research report, create SEO-optimized product descriptions that appeal to online shoppers.",
    agent=seo_content_writer_agent,
    expected_output="A set of SEO-optimized product descriptions."
)

ad_copy_task = Task(
    description="Write engaging and persuasive ad copy for social media campaigns, based on the product descriptions.",
    agent=ad_copy_generator_agent,
    expected_output="A set of high-converting ad copies for Facebook, Instagram, and Google Ads."
)

# Define AI Crew
content_creation_crew = Crew(
    agents=[product_research_agent, seo_content_writer_agent, ad_copy_generator_agent],
    tasks=[product_research_task, seo_content_task, ad_copy_task],
    verbose=True,
    process=Process.sequential
)

# Execute AI workflow
result = content_creation_crew.kickoff()

print("######################")
print(result)
