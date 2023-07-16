import ChatGPTFunctions as CGF
import speech_recognition as SR

# Use the default microphone as the audio source
with SR.Microphone() as source:
    CGF.listen_for_wake_word(source)

