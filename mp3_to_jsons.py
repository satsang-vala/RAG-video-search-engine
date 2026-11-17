import whisper
import torch
import json
import os

# Load the smallest Whisper model
model = whisper.load_model("large-v2",device="cuda")

# all audios  that i want to transcribe
audios = os.listdir('audios')

for audio in audios:
    print(audio)

    # Transcribe an audio file
    result = model.transcribe(audio = f'audios/{audio}',
                             language = 'hi',
                             task = 'translate',
                             word_timestamps= False,
                             fp16=True)



    chunks=[]
    for segment in result['segments']:
        chunks.append({'video':audio,'id':segment['id'], 'start': segment['start'] , 'end':segment['end'] , 'text':segment['text']})

    chunks_with_matadata = {'chunks' : chunks , 'text': result['text']}

    with open(f"jsons/{audio}.json" , "w") as f:
        json.dump(chunks_with_matadata , f)