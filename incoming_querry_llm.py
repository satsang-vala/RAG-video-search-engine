
import requests
import json
import pandas as pd
import os
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# create the user input querry into the embeddings by using the 'beg-m3'
df = joblib.load('embeddings.joblib')

def create_embedding(text_list):
    result = requests.post(
        'http://localhost:11434/api/embed',
        json={
            'model': 'bge-m3',
            'input': text_list
        },
        timeout=300
    )
    result.raise_for_status()
    return result.json()['embeddings']

# this was the other model that work without the api key by pulling it to your device
# def inference(prompt):
#     r = requests.post("http://localhost:11434/api/generate", json={
#         # "model": "deepseek-r1",
#         "model": "qwen2.5:3b",
#         "prompt": prompt,
#         "stream": False
#     })
#     response = r.json()
#     return response



# usint groq for the last output through the llm
def inference_groq(prompt):

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=1024
    )

    return completion.choices[0].message.content

incoming_qerry = input('Ask a Question :')
question_embedding = create_embedding([incoming_qerry])[0]

# using the cosine similarity for the embeddings

similarities = cosine_similarity(np.vstack(df['embedding']) , [question_embedding]).flatten()

top_idx = 3
max_indx_similarity = similarities.argsort()[::-1][:top_idx]

new_df = df.iloc[max_indx_similarity].copy()
new_df["similarity"] = similarities[max_indx_similarity]


# this was the prompt for llm
prompt = f'''
You are an AI video navigation assistant for a web development course.

Video subtitle chunks:
{new_df[['video', 'text', 'start', 'end']].to_json(orient='records')}

User Question:
{incoming_qerry}

Instructions:
1. Find all video segments that contain information relevant to the question.
2. Prioritize direct answers but include useful partial mentions.
3. Return the exact video name, start time, end time and original transcript text.
4. Convert seconds into MM:SS format.
5. Use ONLY the provided transcripts. Never guess or invent information.
6. If no relevant segment exists, say:
   "This topic was not found in the provided course videos."
7. Keep the response concise and prioritize timestamp accuracy.

Output Format:
Video: [Video name]
Time: [Start] - [End]
Transcript: [Relevant original text]
'''

with open('prompt.txt' ,'w')as f:
    f.write(prompt)


# Generate response using Groq API
try:
    response = inference_groq(prompt)

    if response is None:
        print("Could not generate an answer. Please try again.")

    else:
        print(response)

        # Save response into response.txt
        with open("response.txt", "w", encoding="utf-8") as f:
            f.write(response)

except Exception as e:
    print(f"Groq API Error: {e}")

