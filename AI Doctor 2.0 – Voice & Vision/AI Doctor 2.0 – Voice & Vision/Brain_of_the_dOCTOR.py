import os
import base64
from groq import Groq

# Load API Key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Encode Image to Base64
image_path = "acne.jpg"
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)  # Keep only one instance

# Model Name
model = "llama-3.2-90b-vision-preview"

# User Query
query = "Is there something wrong with my face?"

# Messages List (Fixed Structure)
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": query},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
        ]
    }
]

# API Call
chat_completion = client.chat.completions.create(
    messages=messages,
    model=model
)

# Print Response
print(chat_completion.choices[0].message.content)



