#!/usr/bin/python3

import re, sys

mapping_units = {
                    "0":"",
                    "zero":"zero",
                    "1":"um",
                    "2":"dois",
                    "3":"três",
                    "4":"quatro",
                    "5":"cinco",
                    "6":"seis",
                    "7":"sete",
                    "8":"oito",
                    "9":"nove"
                }

mapping_dozens = {
                    "0":"",
                    "10":"dez",
                    "11":"onze",
                    "12":"doze",
                    "13":"treze",
                    "14":"catorze",
                    "15":"quinze",
                    "16":"dezasseis",
                    "17":"dezassete",
                    "18":"dezoito",
                    "19":"dezanove",
                    "2":"vinte",
                    "3":"trinta",
                    "4":"quarenta",
                    "5":"cinquenta",
                    "6":"sessenta",
                    "7":"setenta",
                    "8":"oitenta",
                    "9":"noventa"
                }

mapping_hundreds = {
                    "0":"",
                    "100":"cem",
                    "1":"cento",
                    "2":"duzentos",
                    "3":"trezentos",
                    "4":"quatrocentos",
                    "5":"quinhentos",
                    "6":"seiscentos",
                    "7":"setecentos",
                    "8":"oitocentos",
                    "9":"novecentos"
                }

mapping_ord = {
                0: "",
                1: " mil",
                2: " milhões",
                3: " mil milhões",
                4: " bilhões",
                5: " triliões"
              }

mapping_ord_um = {
                0: "um",
                1: "mil",
                2: "um milhão",
                3: "mil milhões",
                4: "um bilhão",
                5: "um trilião"
              }

def toString(text):
    # String a devolver
    out = ""
    if text[0]==",": #se começar por uma virgula colocar já no resultado final
        out += " vírgula " 
    # remover espaços e virgulas
    text = [t for t in text if t!=" " and t!=","]
    #tamanho do número recebido
    sizeT = size = len(text)
    # Se for apenas 0
    if text=="0":
        out += mapping_units["zero"];    
    else:
        #percorre-se o número do mais signficativo para o menos significativo
        #contudo por forma a saber a grandeza é necessário que o contador vá do tamanho total do número para 0
        #por forma a saber a posição de cada número
        #o resto será a ordem dentro de centenas(0), dezenas(2) e unidades(1)
        #a divisão inteira dará o número de vezes que há 3 algarismos, ou seja centenas, dezenas, unidades
        while size>0:
            rest = size % 3 #calcular a ordem
            if rest == 1: #ordem das unidades
                if sizeT-size-1>=0: 
                    if text[sizeT-size-1] != "1": #se esse valor antes é diferente de 1, de forma a garantir que n entra em conflito com o caso especial das dezenas
                        out += mapping_units[text[sizeT-size]]
                        out += mapping_ord[size // 3]
                else: #senao, não tem valor antes, é o primeiro algarismo
                    if text[sizeT-size] != "1": #se o algarismo for diferente de 1
                        out += mapping_units[text[sizeT-size]]
                        out += mapping_ord[size // 3]
                    else:
                        out += mapping_ord_um[size // 3]
                if sizeT-size+1 < sizeT and text[sizeT-size+1]!="0": #se existe um número|,|espaço a seguir e é diferente de 0
                    out += " e "
            elif rest == 2: #ordem das dezenas
                if text[sizeT-size] == "1": #se o algarismo das dezenas é 1 então a forma como é escrito é especial
                    out += mapping_dozens[text[sizeT-size]+text[sizeT-size+1]]
                else: #senão
                    out += mapping_dozens[text[sizeT-size]]
                    if text[sizeT-size+1]!="0": #se o algarismo das unidades é diferente de 0
                        out += " e "
            else: #rest == 0, ordem das centenas
                if text[sizeT-size]+text[sizeT-size+1]+text[sizeT-size+2]=="100":
                    out += mapping_hundreds["100"]
                else:
                    out += mapping_hundreds[text[sizeT-size]]
                    if text[sizeT-size+1]!="0": #se o algarismo das dezenas é diferente de 0
                        out += " e "
            size -= 1
    
    return out

def number_to_text(text):
    #adicionar um espaço entre números e simbolos especiais 
    text = re.sub(r"([0-9]+)([€%$])",r"\1 \2",text)
    #match com a parte decimal do número
    text = re.sub(r" ?,([0-9 ]+)?[0-9]",lambda x: toString(x[0]),text)
    #match com a parte inteira do número que tem de começar e acabar num número podendo ter espaços pelo meio
    text = re.sub(r"[0-9]([0-9 ]+)?[0-9]",lambda x: toString(x[0]),text)
    #match com números com apenas unidade, os casos que não foram apanhados pelo caso anterior
    text = re.sub(r"[0-9]",lambda x: toString(x[0]),text)
    return text

def number_to_text_file(f):
    content = f.read()
    return number_to_text(content)

if len(sys.argv)==2:
    input = open(sys.argv[1])
else:
    input = sys.stdin

convertedText = number_to_text_file(input)
print(convertedText)
