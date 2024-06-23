"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="add your api key here")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 1000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="remember all this when asked question you will answer from this data.\n"
                     "be concise only answer in max 5 words, average of 2 words, min of 1 word\n, "
                     "if it is a multi option question only give the index number of the answer",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "{\n  \"name\": \"john  doe\",\n  \"contact\": {\n    \"phone\": \"1234567898\",\n    \"email\": \"mail@live.com\",\n    \"stackoverflow\": \"Stackoverflow\",\n    \"github\": \"Github\"\n  },\n  \]\n    }\n  ],\n  \"education\": [\n    {\n      \"degree\": \"\",\n      \"institution\": \"\",\n      \"startDate\": \"\",\n      \"endDate\": \"\"\n    },\n    {\n      \"degree\": \"\",\n      \"institution\": \"\",\n      \"startDate\": \"\",\n      \"endDate\": \"April 2017\"\n    }\n  ],\n  \"codingProjects\": [\n    {\n      \"name\": \"Amazon Price Alert\",\n      \"githubLink\": \"Github\",\n      \"technologies\": [\n        \"Flask\",\n        \"Python\",\n        \"SQLite\",\n        \"HTML\",\n        \"CSS\",\n        \"JavaScript\"\n      ],\n      \"date\": \"Nov 2023\",\n      \"description\": \"\\\"Amazon Price Alert\\\" is a web application designed to notify users about anticipated prices set by the user. Users might input Amazon URLs or product IDs to track specific items. Users can define the price points at which they would like to be notified.\"\n    },\n    {\n      \"name\": \"Image Watermarking Web App\",\n      \"githubLink\": \"Github\",\n      \"technologies\": [\n        \"Python\",\n        \"Flask\",\n        \"Pillow\",\n        \"HTML\",\n        \"CSS\",\n        \"JavaScript\"\n      ],},\n    {\n      \"name\": \"Prevent Closure\",\n      \"hostedLink\": \"Hosted Link\",\n      \"githubLink\": \"Github\",\n      \"technologies\": [\n        \"HTML\",\n        \"CSS\",\n        \"JavaScript\"\n      ],\n      \"date\": \"Sep 2023\",\n      \"description\": \"An application designed to prevent accidental closure of browsers, created using HTML, CSS, and JavaScript to enhance the user experience.\"\n    },\n    {\n      \"name\": \"Spotify Playlist Generator\",\n      \"hostedLink\": \"Hosted Link\",\n      \"githubLink\": \"Github\",\n      \"technologies\": [\n        \"Python\",\n        \"Flask\",\n        \"HTML\",\n        \"Beautiful Soup\",\n        \"Spotify API\",\n        \"Bootstrap\"\n      ]  }\n  ]\n}",
      ],
    },
    {
      "role": "model",
      "parts": [
        "This is a well-structured JSON object representing a resume. It contains a wealth of information about a person named John Doe, covering:\n\n**Personal Details:**\n\n* Full Name\n* Last Name\n* Email\n* LinkedIn Profile\n* Mobile Number\n\n**Education:**\n\n* Details of two degrees, including:\n    * Institution\n    * Location\n    * Degree Name\n    * GPA\n    * Start Date\n    * End Date\n\n**Skills:**\n\n* Categorized into:\n    * Languages\n    * Frameworks\n    * Tools\n    * Platforms\n    * Soft Skills\n\n**Work Experience:**\n\n* One entry with:\n    * Position\n    * Company\n    * Start Date\n    * End Date\n    * Responsibilities (list of bullet points)\n    * Tech Experience (duration of specific skills used)\n    * Joining Date\n    * Notice Period\n\n**Projects:**\n\n* Two entries with:\n    * Name\n    * Type (Personal/Academic)\n    * Start Date\n    * End Date\n    * Description (list of bullet points)\n    * Tech Experience (duration of specific skills used)\n\n**Certifications:**\n\n* Two entries with:\n    * Name\n    * Date\n\n**Additional Information:**\n\n* List of bullet points providing additional insights.\n\n**Strengths of this JSON:**\n\n* **Well-organized:** Data is grouped logically and clearly.\n* **Structured:** Consistent use of key-value pairs and arrays for easy parsing.\n* **Comprehensive:** Covers important resume sections.\n* **Detailed:** Provides sufficient information about each item.\n\n**Possible Enhancements:**\n\n* **Job Descriptions:**  Add more details to the \"responsibilities\" section, highlighting achievements and quantifiable results.\n* **Project Links:** Include links to live projects or repositories on platforms like GitHub.\n* **",
      ],
    },
    {
      "role": "user",
      "parts": [
        "remember all this when asked question you will answer from this data.\nyou will answer using this data min 1 word, average 3 words , and max 5 words",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Understood. I will use the provided JSON data to answer your questions. I will aim for a minimum of one word, an average of three words, and a maximum of five words in my responses. \n",
      ],
    },
  ]
)


def bard_flash_response(question) -> str:
    try:
      response = chat_session.send_message(question)
      return response.text
    except Exception as e:
      print(f"An error occurred: {e}")
      return 0

