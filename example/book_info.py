from pydantic import BaseModel, Field
from typing import Optional, List
import pydantic_chatcompletion

# Define the pydantic model
class BookInformation(BaseModel):
    title: str = Field(description="The title of the book")
    author: str = Field(description="The name of the book's author")
    publication_year: Optional[int] = Field(description="The publication year of the book")
    genre: Optional[str] = Field(description="The genre of the book")
    characters: Optional[List[str]] = Field(description="A list of the main characters in the book")
    summary: Optional[str] = Field(min_length=10, description="A brief summary of the book's plot")

# Input unstructured text
unstructured_text = """
Pride and Prejudice is a novel by Jane Austen, published in 1813.
This classic novel follows the story of Elizabeth Bennet, the protagonist, as she navigates issues of manners, morality, education, and marriage in the society of the landed gentry of early 19th-century England.
The story revolves primarily around Elizabeth and her relationship with the haughty yet enigmatic Mr. Darcy.
The book is set in rural England, and it is notable for its wit and humor as well as its commentary on class distinctions, social norms, and values.
Some of the main characters in the novel include Elizabeth Bennet, Mr. Darcy, Jane Bennet, Mr. Bingley, Lydia Bennet, and Mr. Wickham.
Pride and Prejudice is considered a classic work of English literature and has been adapted numerous times for television, film, and stage.
It is often categorized as a romantic novel, but it also has elements of satire and social commentary.
"""

# Set up messages
messages = [
    {"role": "user", "content": "Extract the book information from the following content:"},
    {"role": "user", "content": unstructured_text},
]

# Use pydantic_chatcompletion to get a structured data class
structured_data = pydantic_chatcompletion.create(messages, BookInformation, model='gpt-3.5-turbo')

# Print the structured data
print(structured_data)

"""
title='Pride and Prejudice' 
author='Jane Austen' 
publication_year=1813 
genre='Romantic novel' 
characters=['Elizabeth Bennet', 'Mr. Darcy', 'Jane Bennet', 'Mr. Bingley', 'Lydia Bennet', 'Mr. Wickham'] 
summary='Pride and Prejudice is a classic novel by Jane Austen that follows the story of Elizabeth Bennet as she navigates issues of manners, morality, education, and marriage in the society of the landed gentry of early 19th-century England. The story revolves primarily around Elizabeth and her relationship with the haughty yet enigmatic Mr. Darcy. The book is set in rural England, and it is notable for its wit and humor as well as its commentary on class distinctions, social norms, and values.'
"""
