from pydantic import BaseModel, Field
from typing import Optional
import pydantic_chatcompletion


class DocumentMetadata(BaseModel):
    title      : Optional[str] = Field(description='The title of the content')
    author     : Optional[str] = Field(description='The author of the content')
    created_at : Optional[str] = Field(description='The date in the format YYYY-MM-DD that the content was created if it appears in the content')
    language   : str           = Field(description='The 2 character ISO 639-1 language code of the primary language of the content')



text = """Updated 24th March 2023
Generative AI - Chapter 1: Establishing the Investment Framework
BlackLake Equity Research
The advent of cloud computing paved the way for new investment opportunities by facilitating the provision of software as a service. Generative AI takes this a step further, offering additional tools to boost end-user productivity. While traditional AI has proven useful in predicting outcomes, Generative AI specializes in creating content such as text, video, images, or computer code - a feat previously unachievable. Large Language Models (LLMs) play a crucial role as enablers of GAI, displaying an unprecedented level of expertise and intelligence. AI holds the potential to give rise to new enterprises and furnish existing players with fresh growth opportunities by greatly enhancing end-user productivity."""


messages = [{"role":   "user",
             "content": "Extract metadata from the following content:"},
            {"role":   "user",
             "content": text}]
            

data = pydantic_chatcompletion.create(messages, DocumentMetadata, model='gpt-3.5-turbo')

print(data)

"""
title='Generative AI - Chapter 1: Establishing the Investment Framework'
author='BlackLake Equity Research' 
created_at='2023-03-24' 
language='en'
"""
