from pydantic import BaseModel, Field
from typing import Optional
import pydantic_chatcompletion

# The data class we wish to extract from the unstructured text
class UserDetails(BaseModel):
    name: str = Field(description="The name of the user")
    age: Optional[int] = Field(description="The age of the user")
    email: Optional[str] = Field(description="The email address of the user")
    country: str = Field(description="The country the user resides in")


# Example unstructured text from which to extract the UserDetails
unstructured_text = """
John Doe, a software engineer from San Francisco, California, started his career in the tech industry in the United States in 2010.
He initially worked for a small startup before joining a larger multinational company in 2014.
John, currently 30 years old, is passionate about programming and solving complex problems.
He has attended multiple conferences across the world and has collaborated with colleagues from various countries on numerous projects.
Despite his busy work life, John finds time for his hobbies, such as photography and hiking.
He enjoys traveling to different countries, and one of his favorite trips was to Japan in 2019.
Do you need to get in touch with John? Feel free to reach out to him at john.doe@example.com.
"""


# Set up messages as we normally would for a ChatCompletion.create()
messages = [
    {"role": "user", "content": "Extract the user details from the following content:"},
    {"role": "user", "content": unstructured_text},
]


# Use pydantic_chatcompletion to get a structured data class
structured_data = pydantic_chatcompletion.create(messages, UserDetails, model='gpt-3.5-turbo')

# Print the structured data
print(structured_data)

"""
name='John Doe' 
age=30 
email='john.doe@example.com' 
country='United States'
"""
