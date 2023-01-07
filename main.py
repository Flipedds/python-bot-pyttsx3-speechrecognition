import speech_recognition as sr
import pyttsx3

'''instalar pacotes Speech pyttsx3 e pyaudio'''
r = sr.Recognizer()
engine = pyttsx3.init()


def saudar():
    engine.say("olá, como vai?")
    engine.say("bem vindo ao primeiro teste")
    engine.runAndWait()



def resposta_saudar():
    engine.say("oi, que bom falar com você")
    engine.say("como se chama?")
    engine.runAndWait()


def pergunta_idade():
    engine.say(f"olá{nome}")
    engine.say("quantos anos você tem?")
    engine.runAndWait()


def resposta_idade():
    engine.say(f"que legal você tem {idade} anos")
    engine.say(f"o que você quer saber?")
    print("como se chama")
    print("qual o seu número")
    print("qual a sua idade")
    engine.runAndWait()


def assunto(assunto):
    if assunto == '1':
        engine.say("meu nome é lambda")
        engine.runAndWait()

    if assunto == '2':
        engine.say("meu número é 957486578845")
        engine.runAndWait()

    if assunto == '3':
        engine.say("nunca se pergunta a idade á uma mulher")
        engine.runAndWait()


def fale_agora():
    print("fale agora")
    return 0


def erro():
    print("erro")


saudar()
with sr.Microphone(device_index=0) as mic:
    fale_agora()
    audio = r.listen(mic)
try:
    intro = r.recognize_google(audio, language="pt-BR")
    if intro == "Olá":
        resposta_saudar()
        with sr.Microphone(device_index=1) as mic:
            fale_agora()
            audio = r.listen(mic)
        try:
            nome = r.recognize_google(audio, language="pt-BR")
            pergunta_idade()
        except:
            erro()
        with sr.Microphone(device_index=1) as mic:
            fale_agora()
            audio = r.listen(mic)
        try:
            idade = r.recognize_google(audio, language="pt-BR")
            resposta_idade()
            with sr.Microphone(device_index=1) as mic:
                fale_agora()
                audio = r.listen(mic)
            try:
                assunto = r.recognize_google(audio, language="pt-BR")
                assunto(assunto)
            except:
                erro()
        except:
            erro()

except sr.UnknownValueError:
    print("não entendi o que você disse")

except sr.RequestError as e:
    print(f"ocorreu um erro ao chamar o serviço de reconhecimento de voz:{e}")
