import funcoes
from funcoes import *

saudar()
ouvir()
try:
    reconhecer()
    if funcoes.reconhecido == "Olá":
        resposta_saudar()
        ouvir()
        try:
            reconhecer()
            pergunta_idade()
        except:
            erro()
        ouvir()
        try:
            reconhecer()
            resposta_idade()
            menu()
            ouvir()
            try:
                reconhecer()
                assunto()
                continuar()
                ouvir()
                decisao()
            except:
                erro()
        except:
            erro()
except:
    erro()
