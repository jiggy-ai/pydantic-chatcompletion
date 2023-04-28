from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional, List
from datetime import date
import pydantic_chatcompletion

# Define the pydantic model
class Event(BaseModel):
    event_name: str = Field(description="The name of the event")
    start_date: date = Field(description="The start date of the event")
    end_date: date = Field(description="The end date of the event")

    @validator('end_date')
    def start_date_must_be_prior_to_end_date(cls, end_date, values):
        start_date = values.get('start_date')
        if start_date and end_date <= start_date:
            raise ValidationError(f"End date ({end_date}) must be after start date ({start_date})")
        return end_date

class EventList(BaseModel):
    events: List[Event] = Field(description="A list of events")

# Input unstructured text
unstructured_text = """
Calendar Update
Tuesday, April 27, 2023
We have a series of exciting events happening over the next few weeks!

1. Next Monday, the Annual AI Conference will kick off, ending on Wednesday. The event will focus on the latest advancements in artificial intelligence and machine learning, with discussions led by industry experts.

2. In two weeks, the three-day Startup Showcase will take place, where new tech startups will demonstrate their innovative products and services. The event aims to foster collaboration and investment opportunities.

3. The following week, we are hosting a Blockchain Summit, running from Tuesday to Thursday. The summit will explore the potential applications of blockchain technology across various industries, featuring engaging panel discussions and presentations.

4. Finally, at the end of the month, a four-day Virtual Reality Festival will commence. This event celebrates the rapid progress of virtual and augmented reality technologies, with immersive exhibits and experiences available for all attendees.

Make sure to mark your calendars for these thrilling events and seize the opportunity to learn more about the ever-evolving world of technology!
"""

# Set up messages
messages = [
    {"role": "user", "content": "Extract the list of events, including their names and relative start and end dates, from the following content:"},
    {"role": "user", "content": unstructured_text},
]

# Use pydantic_chatcompletion to get a structured data class
structured_data = pydantic_chatcompletion.create(messages, EventList, model='gpt-3.5-turbo')


# Print the structured data
print(structured_data)

"""
events=[
Event(event_name='Annual AI Conference', start_date=datetime.date(2023, 5, 1), end_date=datetime.date(2023, 5, 3)), 
Event(event_name='Startup Showcase', start_date=datetime.date(2023, 5, 15), end_date=datetime.date(2023, 5, 17)), 
Event(event_name='Blockchain Summit', start_date=datetime.date(2023, 5, 23), end_date=datetime.date(2023, 5, 25)), 
Event(event_name='Virtual Reality Festival', start_date=datetime.date(2023, 5, 29), end_date=datetime.date(2023, 6, 1))
]
"""
