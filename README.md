# Pydantic ChatCompletion

This repository provides a wrapper around the OpenAI ChatCompletion API that help enables the extraction of structured data (in the form of a Pydantic model) from unstructured text via language model.

This package provide a `pydantic_chatcompletion.create()` function that is similar to the `openai.ChatCompletion.create()` function.

The `pydantic_chatcompletion.create()` function takes an arbitrary pydantic class as an additional argument (in addition to the normal arguments supported by `openai.ChatCompletion.create()`) and tries to return an instance of the supplied pydantic class as return data.

The `create` function in the `pydantic_chatcompletion` package is designed to interact with the OpenAI ChatCompletion API to progressively guide the language model to produce structured data according to a provided Pydantic model. Here's how it accomplishes this task:

1. It starts by appending a system message to the list of messages, instructing the language model to respond with valid JSON that conforms to the Pydantic model's JSON schema. The message also asks the language model not to include any additional text besides the JSON object.

2. If the language model output is not valid json, append the json.loads() exception output as an additional system message and try again.

3. If the lanugage model output is valid json but does not pass pydantic validation, append the pydantic exception output as an additional system message and try again.

In most cases the error remediation of the 2nd and 3rd steps is not required as the language model is usually able to output correct data on the first try.


## Installation

```bash
pip install pydantic_chatcompletion
```

## Usage


```python
import pydantic_chatcompletion
from pydantic import BaseModel


messages = [{"role": "user", "content": "All of your unstructured text to process via language model..."]


class MyPydanticModel(BaseModel)
      """
      The data we extract from the unstructured text via lanugage model.
      """
      some_data: int
      more_data: str

instance_of_my_data =  pydantic_chatcompletion.create(messages, MyPydanticModel, model='gpt-3.5-turbo')

print(instance_of_my_data.some_data, instance_of_my_data.more_data)
```

## Summary of Examples

1. `example/book_info.py`: Extracts structured book information (title, author, publication year, genre, characters, and summary) from a given unstructured text describing the book "Pride and Prejudice".

2. `example/doc_metadata.py`: Extracts metadata (title, author, creation date, and primary language) from an unstructured text related to a document about investment opportunities in Generative AI.

3. `example/list_event_dates.py`: Extracts a list of events, their names, and their relative start and end dates from an unstructured text containing a calendar of events.

4. `example/movie_info.py`: Extracts structured movie information (title, director, release year, cast, genre, duration, plot, and awards) from an unstructured text about the movie "The Godfather".

5. `example/nested.py`: Extracts a nested curriculum structure (curriculum title, description, courses, course titles, instructors, and course durations) from an unstructured text describing a data science bootcamp.

6. `example/user_details.py`: Extracts user details (name, age, email, and country) from an unstructured text about a software engineer named John Doe.
