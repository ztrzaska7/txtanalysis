import pyttsx3 as pyttsx3
engine=pyttsx3.init()
engine.setProperty("voice",'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0')
rate=engine.getProperty('rate')
engine.setProperty('rate',400)
print(rate)
engine.say("Cześć mordo")


engine.runAndWait()
voices = engine.getProperty("voices")
# for voice in voices:
#     print("Voice ", voice.name)
#     print("Voice Id ", voice.id)
#     print("Voice languages ", str(voice.languages))
#     print("Gender: ", voice.gender)
#     print("Age: ", str(voice.age))
#     print("\n")









