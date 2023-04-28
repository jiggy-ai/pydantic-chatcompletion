from pydantic import BaseModel, Field
from typing import Optional, List
import pydantic_chatcompletion

# Define the pydantic models
class Course(BaseModel):
    title: str = Field(description="The title of the course")
    instructor: str = Field(description="The name of the course's instructor")
    duration_hours: Optional[int] = Field(description="The duration of the course in hours")

class Curriculum(BaseModel):
    curriculum_title: str = Field(description="The title of the curriculum")
    description: Optional[str] = Field(description="A brief description of the curriculum")
    courses: List[Course] = Field(description="A list of the courses included in the curriculum")

# Input unstructured text
unstructured_text = """
The Data Science Bootcamp is a comprehensive curriculum designed to provide students with the fundamental knowledge and practical skills required for a career in data science.
The bootcamp includes the following four courses:

1. Introduction to Python: This course, taught by John Doe, covers the basics of the Python programming language and its applications in data science. It lasts for 20 hours.

2. Data Wrangling and Visualization: Led by Jane Smith, this course teaches students how to clean, manipulate, and visualize data using popular Python libraries like pandas and Matplotlib. The course duration is 30 hours.

3. Machine Learning Foundations: In this 40-hour course, instructor Michael Brown introduces the core concepts and algorithms of machine learning, including supervised and unsupervised learning techniques.

4. Advanced Topics in Data Science: Taught by Sarah Johnson and lasting 35 hours, this course explores advanced data science techniques such as deep learning, natural language processing, and time series analysis.
"""

# Set up messages
messages = [
    {"role": "user", "content": "Extract the curriculum information from the following content:"},
    {"role": "user", "content": unstructured_text},
]

# Use pydantic_chatcompletion to get a structured data class
structured_data = pydantic_chatcompletion.create(messages, Curriculum, model='gpt-3.5-turbo')

# Print the structured data
print(structured_data)

"""
curriculum_title='Data Science Bootcamp' 
description='A comprehensive curriculum designed to provide students with the fundamental knowledge and practical skills required for a career in data science.'
 courses=[
  Course(title='Introduction to Python', instructor='John Doe', duration_hours=20), 
  Course(title='Data Wrangling and Visualization', instructor='Jane Smith', duration_hours=30), 
  Course(title='Machine Learning Foundations', instructor='Michael Brown', duration_hours=40), 
  Course(title='Advanced Topics in Data Science', instructor='Sarah Johnson', duration_hours=35)]
"""
