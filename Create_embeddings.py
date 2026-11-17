
import requests
import json
import pandas as pd
import os
import joblib

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


newjsons = os.listdir('newjsons')

print(newjsons)

my_dicts = []

BATCH_SIZE = 10

for json_file in newjsons:

    with open(f'newjsons/{json_file}', encoding='utf-8') as f:
        content = json.load(f)

    print(f'Creating embeddings for {json_file}')

    chunks = content['chunks']

    texts = [c['text'] for c in chunks]

    all_embeddings = []

    # Create batches
    for i in range(0, len(texts), BATCH_SIZE):

        batch = texts[i:i + BATCH_SIZE]

        print(f'Processing batch {i // BATCH_SIZE + 1}')

        embeddings = create_embedding(batch)

        all_embeddings.extend(embeddings)

    # Attach embeddings to original chunks
    for chunk, embedding in zip(chunks, all_embeddings):

        chunk['embedding'] = embedding

        my_dicts.append(chunk)

    print(f'Completed {json_file}')

df = pd.DataFrame.from_records(my_dicts)

print(df)

joblib.dump(df , 'embeddings.joblib')
