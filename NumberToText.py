#!/usr/bin/env python3

import re, sys, getopt

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
                1: "mil",
                2: "milhões",
                3: "mil milhões",
                4: "bilhões",
                5: "triliões"
              }

mapping_ord_um = {
                0: "um",
                1: "mil",
                2: "um milhão",
                3: "mil milhões",
                4: "um bilhão",
                5: "um trilião"
              }

mapping_ord_rev = {
                "cem":"00",
                "mil":"000",
                "milhão":"000000",
                "milhões":"000000",
                "bilhão":"000000000000",
                "bilhões":"000000000000",
                "trilião":"000000000000000",
                "triliões":"000000000000000"
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
    if sizeT==1 and text[0]=="0":
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
                div = size // 3
                if sizeT-size-1>=0: 
                    if text[sizeT-size-1] != "1": #se esse valor antes é diferente de 1, de forma a garantir que n entra em conflito com o caso especial das dezenas
                        out += mapping_units[text[sizeT-size]]
                        if div != 0 and text[sizeT-size-1]!="0" and text[sizeT-size]!="0":
                            out += " " + mapping_ord[div]
                    else:
                        out += " " + mapping_ord[div]
                else: #senao, não tem valor antes, é o primeiro algarismo
                    if text[sizeT-size] != "1": #se o algarismo for diferente de 1
                        out += mapping_units[text[sizeT-size]]
                        if div != 0:
                            out += " " + mapping_ord[div]
                    else:
                        out += mapping_ord_um[div]
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

def toNumber(text):
    #valor a devolver com o número
    out = ""
    #separa a string por espaços
    words = text.split()
    #remove e e faz reverse da lista de palavras
    words = [word for word in words if word!="e"][::-1]
    
    #saber se tem vírgula
    haveComma = False
    for word in words:
        if word=="vírgula":
            haveComma = True
    
    #converte palavra para números, os valores são adicionados
    #por ordem inversa visto que estamos a percorrer o número
    #por ordem inversa também
    i=0 # contador geral
    num=0 # contador de números, feito reset quando aparece a vírgula
    for word in words:
        #se é uma virgula coloca uma
        if word=="vírgula":
            out = "," + out
            num = 0
        # senão é uma vígula
        else:
            #boolean pra saber se já encontrou a palavra
            found = False
            #procura nas centenas e coloca no out
            for item in list(mapping_hundreds.items())[1:]:
                if item[1]==word:
                    #se não tem nenhum número após
                    if num % 3 == 0 and len(item[0])==1:
                        out = item[0] + "00" + out
                        num += 3
                    #se só tem um número após
                    elif num % 3 == 1 and len(item[0])==1:
                        out = item[0] + "0" + out
                        num += 2
                    # se tem dois números após
                    else:
                        out = item[0] + out
                        num += len(item[0])
                    found = True
                    break
            # senão estava nas centenas
            if not found:
                #procura nas dezenas
                for item in list(mapping_dozens.items())[1:]:
                    if item[1]==word:
                        #se não tem nenhum número após
                        if num % 3 == 0 and len(item[0])==1:
                            out = item[0] + "0" + out
                            num += 2
                        # se tem um número após
                        else:
                            out = item[0] + out
                            num += len(item[0])
                        found = True
                        break
                # senão estava nas dezenas
                if not found:
                    #procura nas unidades
                    for item in list(mapping_units.items())[2:]:
                        if item[1]==word:
                            out = item[0] + out
                            found = True
                            num += 1
                            break
                    #senao estava nas unidades
                    if not found:
                        # se zero entao coloca um zero
                        if word == "zero":
                            out = "0" + out
                        else:
                            #vê se o número não tem virgula
                            if not haveComma:
                                #se está no fim do número, então coloca os zeros de acordo com a ordem
                                if i==0 or (i==1 and words[0]=="milhões"):
                                    out = mapping_ord_rev[word] + out
                                else:
                                    #colocar o número de zeros necessários
                                    out = "0"*(len(mapping_ord_rev[word])-num) + out
                                    num += len(mapping_ord_rev[word])-num
                                # se é a ultima palavra então coloca um 1
                                if len(words) == i+1:
                                    out = "1" + out
                            # se tem virgula, entao não converte pra número as grandezas
                            else:
                                out = " " + word + out
        i += 1
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

def text_to_number(text):
    #palavras válidas para um número em extenso
    validWords = list(mapping_ord.values())[1:][::-1]
    validWords += list(mapping_ord_um.values())[1:][::-1]
    validWords += list(mapping_hundreds.values())[1:]
    validWords += list(mapping_dozens.values())[1:][::-1]
    validWords += list(mapping_units.values())[1:]
    # primeira palavra
    validWordsF = "(" + "|".join(validWords) + ")"
    # restantes palavras
    validWords = "( " + "| ".join(validWords) + "| e(?= )| vírgula)"
    #sempre que encontrar um número em formato texto, converter para número
    text = re.sub(r"(?<![A-Za-z])"+validWordsF+"(?=[ \n])"+validWords+"*",lambda x: toNumber(x[0]),text)
    return text

def printHelp():
    print("Usage: ./NumberToText.py [OPTIONS] [FILENAME]")
    print("  or:  ./NumberToText.py [OPTIONS]")
    print("Default behaviour: Convert numbers to portuguese text")
    print("\nOptions:")
    print("  -r\tConvert portuguese text to numbers")
    print("  -h\tHelp")
    print("\nExample: ./NumberToText.py text.txt")

#main

try:
    options, remainder = getopt.getopt(sys.argv[1:], 'rh')
    dict_opts = dict(options)
except:
    printHelp()
    sys.exit(1)

reversed = dict_opts.get('-r',None)
help = dict_opts.get('-h',None)

if help!=None:
    printHelp()
    sys.exit(1)
else:
    # read from STDIN if file is not passed as argument
    if remainder:
        try:
            input = open(remainder[0])
        except:
            print("Wrong file path! File doesn't exist?")
            printHelp()
            sys.exit(1)
    else:
        input = sys.stdin

    convertedText = ""
    try:
        content = input.read()
    except:
        print("\nUse CTRL+D instead to get results!")
        sys.exit(1)

    # if -r option passed convert text to number, else convert number to text
    if reversed!=None:
        convertedText = text_to_number(content)
    else:
        convertedText = number_to_text(content)

    print(convertedText)
