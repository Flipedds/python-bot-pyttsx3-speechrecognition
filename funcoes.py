import speech_recognition as sr
import pyttsx3

'''instalar pacotes SpeechRecognition, pyttsx3 e pyaudio'''

r = sr.Recognizer()
engine = pyttsx3.init()
audio = ''
reconhecido = ''


def saudar():
    engine.say("olá, como vai?")
    engine.say("bem vindo ao centésimo segundo teste")
    engine.runAndWait()


def ouvir():
    with sr.Microphone(device_index=0) as mic:
        fale_agora()
        global audio
        audio = r.listen(mic)
        return audio


def resposta_saudar():
    engine.say("oi, que bom falar com você")
    engine.say("como se chama?")
    engine.runAndWait()


def pergunta_idade():
    engine.say(f"olá{reconhecido}")
    engine.say("quantos anos você tem?")
    engine.runAndWait()


def resposta_idade():
    engine.say(f"que legal você tem {reconhecido} anos")


def menu():
    engine.say("o que você quer saber?")
    engine.say("1 - como me chamo?")
    engine.say("2 - qual o meu número?")
    engine.say("3 - qual a minha idade?")
    engine.runAndWait()


def assunto():
    if reconhecido == "um" or reconhecido == "1":
        engine.say("meu nome é lambda")
        engine.runAndWait()

    elif reconhecido == "dois" or reconhecido == '2':
        engine.say("meu número é 957486578845")
        engine.runAndWait()

    elif reconhecido == "três" or reconhecido == "3":
        engine.say("nunca se pergunta a idade á uma mulher")
        engine.runAndWait()
    else:
        engine.say("opcão inválida")
        engine.runAndWait()


def fale_agora():
    print("fale agora")


def continuar():
    engine.say("Deseja saber mais alguma coisa?")
    engine.say("sim ou não ?")
    engine.runAndWait()


def erro():
    engine.say("Não entendi, o que você disse!")
    engine.runAndWait()


def reconhecer(): #reconhecimento do google
    global reconhecido
    reconhecido = r.recognize_google(audio, language="pt-BR")
    return reconhecido

def decisao(): #decisao de continuar
    if reconhecido == "sim":
        return menu()
    elif reconhecido == "não":
        return 0
