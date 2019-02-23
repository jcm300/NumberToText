#!/usr/bin/python3

import re, sys

mapping_units = {
                    "0":"zero",
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
                0: " ",
                1: " mil ",
                2: " milhões ",
                3: " mil milhões ",
                4: " bilhões ",
                5: " triliões "
              }

def toString(text):
    out = ""
    sizeT = size = len(text)
    while size>0:
        rest = size % 3
        if rest == 1:
            if sizeT-size-1 < sizeT:
                if text[sizeT-size-1] != "1":
                    out += mapping_units[text[sizeT-size]]
                    out += mapping_ord[size // 3]
            else:
                out += mapping_units[text[sizeT-size]]
                out += mapping_ord[size // 3]
                out += " e "
        elif rest == 2:
            if text[sizeT-size] == "1":
                out += mapping_dozens[text[sizeT-size]+text[sizeT-size+1]]
            else:
                out += mapping_dozens[text[sizeT-size]]
                out += " e "
        else: #rest == 0
            out += mapping_hundreds[text[sizeT-size]] + " e "
        size -= 1
    
    return out

def number_to_text(text):
    text = re.sub(r"[0-9]+",lambda x: toString(x[0]),text)
    text = re.sub(r",","vírgula ",text)
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
