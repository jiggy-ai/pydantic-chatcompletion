from pydantic import BaseModel, Field
from typing import Optional, List
import pydantic_chatcompletion

# Define the pydantic model
class MovieInformation(BaseModel):
    title: str = Field(description="The title of the movie")
    director: str = Field(description="The name of the movie's director")
    release_year: Optional[int] = Field(description="The release year of the movie")
    cast: Optional[List[str]] = Field(description="A list of the main actors in the movie")
    genre: Optional[List[str]] = Field(description="The genres of the movie")
    duration_minutes: Optional[int] = Field(description="The duration of the movie in minutes")
    plot: Optional[str] = Field(min_length=10, description="A brief summary of the movie's plot")
    awards: Optional[List[str]] = Field(description="A list of the awards won by the movie")

# Input unstructured text
unstructured_text = """
The Godfather is a 1972 American crime film directed by Francis Ford Coppola, who co-wrote the screenplay with Mario Puzo, based on Puzo's best-selling 1969 novel of the same name.
The film stars Marlon Brando, Al Pacino, and James Caan, and tells the story of the powerful Italian-American crime family of Don Vito Corleone (played by Brando).
When an organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son, Michael Corleone (played by Pacino), a series of events unfold that threatens the stability of the family and the entire criminal underworld.
Set in New York City and spanning the years 1945 to 1955, The Godfather is notable for its realistic depiction of the Mafia and its exploration of themes such as power, loyalty, betrayal, and family dynamics.
The film was met with widespread critical acclaim upon release and is commonly regarded as one of the greatest films in world cinema.
It won three Academy Awards, including Best Picture, Best Actor (Marlon Brando), and Best Adapted Screenplay, and has been selected for preservation in the United States National Film Registry.
The Godfather is a crime drama film and is widely regarded as one of the most influential films in the gangster genre.
Its running time is approximately 175 minutes.
"""

# Set up messages
messages = [
    {"role": "user", "content": "Extract the movie information from the following content:"},
    {"role": "user", "content": unstructured_text},
]

# Use pydantic_chatcompletion to get a structured data class
structured_data = pydantic_chatcompletion.create(messages, MovieInformation, model='gpt-3.5-turbo')

# Print the structured data
print(structured_data)

"""
title='The Godfather' 
director='Francis Ford Coppola' 
release_year=1972 
cast=['Marlon Brando', 'Al Pacino', 'James Caan'] genre=['Crime', 'Drama'] 
duration_minutes=175 
plot='The Godfather tells the story of the powerful Italian-American crime family of Don Vito Corleone, and the series of events that unfold when he transfers control of his empire to his reluctant son Michael Corleone.' 
awards=['Best Picture', 'Best Actor (Marlon Brando)', 'Best Adapted Screenplay']
"""
