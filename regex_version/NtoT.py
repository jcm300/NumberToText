#!/usr/bin/env python3

from collections import Counter
import re
import unidecode

def numberToText(file):
    text = open(file).read()
    text = replacer(text)
    return text

def replacer(text):
    text = re.sub(r"([0-9]+)\,([0-9]+)",r"\1 vírgula \2",text)

#   MILHÕES
#	substituição relativas aos números >= a 1 milhão
#	extrai dígitos != 0 para futura transformação
    text = re.sub(r"(\D)1[ ]000[ ]000([ ,.?!\r\n€$%])|(\D)1000000([ ,.?!\r\n€$%])",r"\1\3um milhão\2\4",text)
    text = re.sub(r"(\D)([0-9]{1,3})[ ]000[ ]000([ ,.?!\r\n€$%])|(\D)([0-9]{1,3})000000([ ,.?!\r\n€$%])",r"\1\2\4\5 milhões\3\6",text)
    text = re.sub(r"(\D)([0-9]{1,3})[ ]000[ ]([0-9]00)([ ,.?!\r\n€$%])|(\D)([0-9]{1,3})[ ]000[ ](0[0-9]{2})([ ,.?!\r\n€$%])",r"\1\2\5\6 milhões e \3\4\7\8",text)
    text = re.sub(r"(\D)([0-9]{1,3})000([0-9]00)([ ,.?!\r\n€$%])|(\D)([0-9]{1,3})000(0[0-9]{2})([ ,.?!\r\n€$%])",r"\1\2\5\6 milhões e \3\4\7\8",text)
    text = re.sub(r"(\D)([0-9]{1,3})[ ]([0-9]{3}[ ][0-9]{3})([ ,.?!\r\n€$%])|(\D)([0-9]{1,3})([0-9]{6})([ ,.?!\r\n€$%])",r"\1\2\5\6 milhões \3\4\7\8",text)


#   MILHARES
#	substituição relativas aos números >= a 1 milhar
#	extrai dígitos != 0 para futura transformação
#	regras para os diferentes casos
#	xx mil e ... vs xx mil ...
    text = re.sub(r"(\D)1[ ]?000([ ,.?!\r\n€$%])",r"\1mil\2 ",text) #1000
    text = re.sub(r"(\D)1[ ]?([0-9]00)([ ,.?!\r\n€$%])|(\D)1[ ]?(0[0-9]{2})([ ,.?!\r\n€$%])",r"\1\4mil e \2\3\5\6 ",text) #1xxx -> mil e ... em vez de "1 mil e ..."
    text = re.sub(r"(\D)1[ ]?([0-9]{3})([ ,.?!\r\n€$%])",r"\1mil \2\3 ",text) #1xxx -> mil e ... em vez de "1 mil e ..."

    text = re.sub(r"(0*[0-9]{1,3})[ ]?000([ ,.?!\r\n€$%])",r"\1 mil\2",text) #2000, 3000, 217000, ...
    text = re.sub(r"(0*[0-9]00)[ ]?000([ ,.?!\r\n€$%])|0*([0-9]{2}0)[ ]?000([ ,.?!\r\n€$%])|0*([0-9]{3})[ ]?000([ ,.?!\r\n€$%])",r"\1\3\5 mil\2\4\6 ",text) #2000, 3000, 217000, ...
    text = re.sub(r"(0*[1-9][0-9]{0,2})[ ]?([0-9]00)([ ,.?!\r\n€$%])|0*([0-9]{1,3})[ ]?(0[0-9]{2})([ ,.?!\r\n€$%])",r"\1\4 mil e \2\3\5\6 ",text)
    text = re.sub(r"(0*[1-9][0-9]{0,2})[ ]?([0-9]{3})([ ,.?!\r\n€$%])",r"\1 mil \2\3",text) #31400, 234200, ...

    #CENTENAS
    text = re.sub(r"0*100",r"cem",text)
    text = re.sub(r"0*1([0-9]{2})",r"cento e \1",text)
    text = re.sub(r"0*200",r"duzentos",text)
    text = re.sub(r"0*2([0-9]{2})",r"duzentos e \1",text)
    text = re.sub(r"0*300",r"trezentos",text)
    text = re.sub(r"0*3([0-9]{2})",r"trezentos e \1",text)
    text = re.sub(r"0*400",r"quatrocentos",text)
    text = re.sub(r"0*4([0-9]{2})",r"quatrocentos e \1",text)
    text = re.sub(r"0*500",r"quinhentos",text)
    text = re.sub(r"0*5([0-9]{2})",r"quinhentos e \1",text)
    text = re.sub(r"0*600",r"seiscentos",text)
    text = re.sub(r"0*6([0-9]{2})",r"seiscentos e \1",text)
    text = re.sub(r"0*700",r"setecentos",text)
    text = re.sub(r"0*7([0-9]{2})",r"setecentos e \1",text)
    text = re.sub(r"0*800",r"oitocentos",text)
    text = re.sub(r"0*8([0-9]{2})",r"oitocentos e \1",text)
    text = re.sub(r"0*900",r"novecentos",text)
    text = re.sub(r"0*9([0-9]{2})",r"novecentos e \1",text)

    #DEZENAS
    text = re.sub(r"0*20",r"vinte",text)
    text = re.sub(r"0*2([0-9])",r"vinte e \1",text)
    text = re.sub(r"0*30",r"trinta",text)
    text = re.sub(r"0*3([0-9])",r"trinta e \1",text)
    text = re.sub(r"0*40",r"quarenta",text)
    text = re.sub(r"0*4([0-9])",r"quarenta e \1",text)
    text = re.sub(r"0*50",r"cinquenta",text)
    text = re.sub(r"0*5([0-9])",r"cinquenta e \1",text)
    text = re.sub(r"0*60",r"sessenta",text)
    text = re.sub(r"0*6([0-9])",r"sessenta e \1",text)
    text = re.sub(r"0*70",r"setenta",text)
    text = re.sub(r"0*7([0-9])",r"setenta e \1",text)
    text = re.sub(r"0*80",r"oitenta",text)
    text = re.sub(r"0*8([0-9])",r"oitenta e \1",text)
    text = re.sub(r"0*90",r"noventa",text)
    text = re.sub(r"0*9([0-9])",r"noventa e \1",text)

#	10-19
    text = re.sub(r"0*10","dez",text)
    text = re.sub(r"0*11","onze",text)
    text = re.sub(r"0*12","doze",text)
    text = re.sub(r"0*13","treze",text)
    text = re.sub(r"0*14","catorze",text)
    text = re.sub(r"0*15","quinze",text)
    text = re.sub(r"0*16","dezasseis",text)
    text = re.sub(r"0*17","dezassete",text)
    text = re.sub(r"0*18","dezoito",text)
    text = re.sub(r"0*19","dezanove",text)

#	UNIDADES
    text = re.sub(r"0*1","um",text)
    text = re.sub(r"0*2","dois",text)
    text = re.sub(r"0*3","três",text)
    text = re.sub(r"0*4","quatro",text)
    text = re.sub(r"0*5","cinco",text)
    text = re.sub(r"0*6","seis",text)
    text = re.sub(r"0*7","sete",text)
    text = re.sub(r"0*8","oito",text)
    text = re.sub(r"0*9","nove",text)
    return text

print(numberToText("../testFiles/test.txt"))
