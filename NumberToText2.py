#!/usr/bin/env python3

import re, sys, getopt

def numberToText(text):
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

def textToNumber(text):
    text = replacerToNumber(text)
    text2 = aggregate(text)
    return text2

def replacerToNumber(text):
    text = re.sub(r"([a-z]+) vírgula ([a-z]+)",r"\1,\2",text)

#   MILHÕES
    text = re.sub(r"(\w)milhões ([a-z]+)([%€.!?\n\r])", r"\1\2\3",text)
    text = re.sub("um milhão","1 000 000",text)

#   MILHARES
    text = re.sub(r"(\w)mil ([a-z]+)([.!?\n\r%€])", r"\1\2\3",text)
    text = re.sub(r"mil([^h])",r"1000\1",text)

#   CENTENAS
#   3 regras base para os 3 casos possíveis 
#   (em função do número de zeros)
    text = re.sub(r"cento e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"10\1",text)
    text = re.sub(r"cento e ([a-z])|cento e ([a-z]+[ ][a-z]+)", r"1\1\2",text)
    text = re.sub("cem","100",text)
    text = re.sub(r"duzentos e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"20\1",text)
    text = re.sub(r"duzentos e ([a-z])|duzentos e ([a-z]+[ ][a-z]+)", r"2\1\2",text)
    text = re.sub("duzentos","200",text)
    text = re.sub(r"trezentos e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"30\1",text)
    text = re.sub(r"trezentos e ([a-z])|trezentos e ([a-z]+[ ][a-z]+)", r"3\1\2",text)
    text = re.sub("trezentos","300",text)
    text = re.sub(r"quatrocentos e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"40\1",text)
    text = re.sub(r"quatrocentos e ([a-z])|quatrocentos e ([a-z]+[ ][a-z]+)", r"4\1\2",text)
    text = re.sub("quatrocentos","400",text)
    text = re.sub(r"quinhentos e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"50\1",text)
    text = re.sub(r"quinhentos e ([a-z])|quinhentos e ([a-z]+[ ][a-z]+)", r"5\1\2",text)
    text = re.sub("quinhentos","500",text)
    text = re.sub(r"seiscentos e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"60\1",text)
    text = re.sub(r"seiscentos e ([a-z])|seiscentos e ([a-z]+[ ][a-z]+)", r"6\1\2",text)
    text = re.sub("seiscentos","600",text)
    text = re.sub(r"setecentos e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"70\1",text)
    text = re.sub(r"setecentos e ([a-z])|setecentos e ([a-z]+[ ][a-z]+)", r"7\1\2",text)
    text = re.sub("setecentos","700",text)
    text = re.sub(r"oitocentos e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"80\1",text)
    text = re.sub(r"oitocentos e ([a-z])|oitocentos e ([a-z]+[ ][a-z]+)", r"8\1\2",text)
    text = re.sub("oitocentos","800",text)
    text = re.sub(r"novecentos e (um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"90\1",text)
    text = re.sub(r"novecentos e ([a-z])|novecentos e ([a-z]+[ e]*[a-z]+)", r"9\1\2",text)
    text = re.sub("novecentos","900",text)

#   DEZENAS
    text = re.sub(r"0?vinte e ([a-z]+)",r"2\1",text)
    text = re.sub(r"0?vinte","20",text)
    text = re.sub(r"0?trinta e ([a-z]+)",r"3\1",text)
    text = re.sub(r"0?trinta","30",text)
    text = re.sub(r"0?quarenta e ([a-z]+)",r"4\1",text)
    text = re.sub(r"0?quarenta","40",text)
    text = re.sub(r"0?cinquenta e ([a-z]+)",r"5\1",text)
    text = re.sub(r"0?cinquenta","50",text)
    text = re.sub(r"0?sessenta e ([a-z]+)",r"6\1",text)
    text = re.sub(r"0?sessenta","60",text)
    text = re.sub(r"0?setenta e ([a-z]+)",r"7\1",text)
    text = re.sub(r"0?setenta","70",text)
    text = re.sub(r"0?oitenta e ([a-z]+)",r"8\1",text)
    text = re.sub(r"0?oitenta","80",text)
    text = re.sub(r"0?noventa e ([a-z]+)",r"9\1",text)
    text = re.sub(r"0?noventa","90",text)

#   10-19
    text = re.sub(r"0?onze","11",text)
    text = re.sub(r"0?doze","12",text)
    text = re.sub(r"0?treze","13",text)
    text = re.sub(r"0?catorze","14",text)
    text = re.sub(r"0?quinze","15",text)
    text = re.sub(r"0?dezasseis","16",text)
    text = re.sub(r"0?dezassete","17",text)
    text = re.sub(r"0?dezoito","18",text)
    text = re.sub(r"0?dezanove","19",text)
    text = re.sub(r"0?dez","10",text)

#   UNIDADES
    text = re.sub("um","1",text)
    text = re.sub("dois","2",text)
    text = re.sub("três","3",text)
    text = re.sub("quatro","4",text)
    text = re.sub("cinco","5",text)
    text = re.sub("seis","6",text)
    text = re.sub("sete","7",text)
    text = re.sub("oito","8",text)
    text = re.sub("nove","9",text)
    return text

#   função que remata as substituições feitas anteriormente
#   tem em atenção vários casos
#   nomeadamente as variâncias no número de zeros
def aggregate(text):
    text = re.sub(r"1000 e ([0-9]{3})",r"1\1",text)
    text = re.sub(r"1000 ([0-9]{3})",r"1\1",text)
    text = re.sub(r"1000 e ([0-9]{2})",r"10\1",text)
    text = re.sub(r"1000 ([0-9]{2})",r"10\1",text)
    text = re.sub(r"1000 e ([0-9])",r"100\1",text)
    text = re.sub(r"1000 ([0-9])",r"100\1",text)
    text = re.sub(r"([0-9]{3})[ ]1([0-9]{3})",r"\1\2",text)
    text = re.sub(r"([0-9]{2})[ ]1([0-9]{3})",r"\1\2",text)
    text = re.sub(r"([0-9])[ ]1([0-9]{3})",r"\1\2",text)
    
    text = re.sub(r"([0-9]+)[ ]milhões[ e]*([0-9]{6})",r"\1\2",text)
    text = re.sub(r"([0-9]+)[ ]milhões[ e]*([0-9]{5})",r"\1 \2",text)
    text = re.sub(r"([0-9]+)[ ]milhões[ e]*([0-9]{4})",r"\1 00\2",text)
    text = re.sub(r"([0-9]+)[ ]milhões[ e]*([0-9]{3})",r"\1 000\2",text)
    text = re.sub(r"([0-9]+)[ ]milhões[ e]*([0-9]{2})",r"\1 0000\2",text)
    text = re.sub(r"([0-9]+)[ ]milhões[ e]*([0-9])",r"\1 00000\2",text)
    text = re.sub(r"([0-9]+)[ ]milhões",r"\1 000000",text)
    text = re.sub(r"([0-9])[ ]([0-9])",r"\1\2",text)
    return text

def printHelp():
    print("Usage: ./NumberToText2.py [OPTIONS] [FILENAME]")
    print("  or:  ./NumberToText2.py [OPTIONS]")
    print("Default behaviour: Convert numbers to portuguese text")
    print("\nOptions:")
    print("  -r\tConvert portuguese text to numbers")
    print("  -h\tHelp")
    print("\nExample: ./NumberToText2.py text.txt")

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
        convertedText = textToNumber(content)
    else:
        convertedText = numberToText(content)

    print(convertedText)
