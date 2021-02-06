import pyttsx3

def initialize_speaker():
	engine= pyttsx3.init()
	voices= engine.getProperty('voices')
	engine.setProperty('rate',150)
	engine.setProperty('voice',voices[1].id)
	return engine

def speaker(sentence):
	engine= initialize_speaker()
	engine.say(sentence)
	engine.runAndWait()



