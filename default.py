import whisper
model = whisper.load_model("base")
file3="C:/Users/omkar/Downloads/Your_First_Lesson.mp3"
result = model.transcribe(file3)
print(result['text'])
