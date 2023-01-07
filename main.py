import speech_recognition as sr
import pyttsx3

'''instalar pacotes SpeechRecognition, pyttsx3 e pyaudio'''
r = sr.Recognizer()
engine = pyttsx3.init()
audio = ''


def saudar():
    engine.say("olá, como vai?")
    engine.say("bem vindo ao primeiro teste")
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
    engine.say(f"olá{nome}")
    engine.say("quantos anos você tem?")
    engine.runAndWait()


def resposta_idade():
    engine.say(f"que legal você tem {idade} anos")


def menu():
    engine.say("o que você quer saber?")
    engine.say("1 - como me chamo?")
    engine.say("2 - qual o meu número?")
    engine.say("3 - qual a minha idade?")
    engine.runAndWait()


def assunto(opcao):

    if opcao == "um" or opcao == "1":
        engine.say("meu nome é lambda")
        engine.runAndWait()

    elif opcao == "dois" or opcao == '2':
        engine.say("meu número é 957486578845")
        engine.runAndWait()

    elif opcao == "três" or opcao == "3":
        engine.say("nunca se pergunta a idade á uma mulher")
        engine.runAndWait()


def fale_agora():
    print("fale agora")


def erro():
    engine.say("Não entendi, o que você disse!")
    engine.runAndWait()


saudar()
ouvir()
try:
    intro = r.recognize_google(audio, language="pt-BR")
    if intro == "Olá":
        resposta_saudar()
        ouvir()
        try:
            nome = r.recognize_google(audio, language="pt-BR")
            pergunta_idade()
        except:
            erro()
        ouvir()
        try:
            idade = r.recognize_google(audio, language="pt-BR")
            resposta_idade()
            menu()
            ouvir()
            try:
                opcao = r.recognize_google(audio, language="pt-BR")
                assunto(opcao)
            except:
                erro()
        except:
            erro()
except:
    erro()
