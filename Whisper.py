import os
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])


#import library from whiper github and openai , fmpeg numy and audio to the file
#this is without secret key
