#!/usr/bin/python3

from collections import Counter
import re
import unidecode

def textToNumber(file):
    text = open(file).read()
    text = replacer(text)
    text2 = aggregate(text)
    print(text2)

def replacer(text):
    text = re.sub(r"([a-z]+) vírgula ([a-z]+)",r"\1,\2",text)

    text = re.sub(r"(\w)milhões ([a-z]+)([%€.!?\n\r])", r"\1\2\3",text)
    text = re.sub("um milhão","1 000 000",text)

    text = re.sub(r"(\w)mil ([a-z]+)([.!?\n\r%€])", r"\1\2\3",text)
    text = re.sub(r"mil([^h])",r"1000\1",text)

    text = re.sub(r"cento e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"10\1",text)
    text = re.sub(r"cento e ([a-z])|cento e ([a-z]+[ ][a-z]+)", r"1\1\2",text)
    text = re.sub("cem","100",text)

    text = re.sub(r"duzentos e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"20\1",text)
    text = re.sub(r"duzentos e ([a-z])|duzentos e ([a-z]+[ ][a-z]+)", r"2\1\2",text)
    text = re.sub("duzentos","200",text)

    text = re.sub(r"trezentos e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"30\1",text)
    text = re.sub(r"trezentos e ([a-z])|trezentos e ([a-z]+[ ][a-z]+)", r"3\1\2",text)
    text = re.sub("trezentos","300",text)

    text = re.sub(r"quatrocentos e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"40\1",text)
    text = re.sub(r"quatrocentos e ([a-z])|quatrocentos e ([a-z]+[ ][a-z]+)", r"4\1\2",text)
    text = re.sub("quatrocentos","400",text)

    text = re.sub(r"quinhentos e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"50\1",text)
    text = re.sub(r"quinhentos e ([a-z])|quinhentos e ([a-z]+[ ][a-z]+)", r"5\1\2",text)
    text = re.sub("quinhentos","500",text)

    text = re.sub(r"seiscentos e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"60\1",text)
    text = re.sub(r"seiscentos e ([a-z])|seiscentos e ([a-z]+[ ][a-z]+)", r"6\1\2",text)
    text = re.sub("seiscentos","600",text)

    text = re.sub(r"setecentos e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"70\1",text)
    text = re.sub(r"setecentos e ([a-z])|setecentos e ([a-z]+[ ][a-z]+)", r"7\1\2",text)
    text = re.sub("setecentos","700",text)

    text = re.sub(r"oitocentos e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"80\1",text)
    text = re.sub(r"oitocentos e ([a-z])|oitocentos e ([a-z]+[ ][a-z]+)", r"8\1\2",text)
    text = re.sub("oitocentos","800",text)

    text = re.sub(r"novecentos e "+r"(um|dois|três|quatro|cinco|seis|sete|oito|nove)", r"90\1",text)
    text = re.sub(r"novecentos e ([a-z])|novecentos e ([a-z]+[ e]*[a-z]+)", r"9\1\2",text)
    text = re.sub("novecentos","900",text)

    text = re.sub(r"vinte e ([a-z]+)",r"2\1",text)
    text = re.sub("vinte","20",text)

    text = re.sub(r"trinta e ([a-z]+)",r"3\1",text)
    text = re.sub("trinta","30",text)

    text = re.sub(r"quarenta e ([a-z]+)",r"4\1",text)
    text = re.sub("quarenta","40",text)

    text = re.sub(r"cinquenta e ([a-z]+)",r"5\1",text)
    text = re.sub("cinquenta","50",text)

    text = re.sub(r"sessenta e ([a-z]+)",r"6\1",text)
    text = re.sub("sessenta","60",text)

    text = re.sub(r"setenta e ([a-z]+)",r"7\1",text)
    text = re.sub("setenta","70",text)

    text = re.sub(r"oitenta e ([a-z]+)",r"8\1",text)
    text = re.sub("oitenta","80",text)

    text = re.sub(r"noventa e ([a-z]+)",r"9\1",text)
    text = re.sub("noventa","90",text)

    text = re.sub("onze","11",text)
    text = re.sub("doze","12",text)
    text = re.sub("treze","13",text)
    text = re.sub("catorze","14",text)
    text = re.sub("quinze","15",text)
    text = re.sub("dezasseis","16",text)
    text = re.sub("dezassete","17",text)
    text = re.sub("dezoito","18",text)
    text = re.sub("dezanove","19",text)
    text = re.sub("dez","10",text)

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
    text = re.sub(r"([0-9]+)[ ]milhões",r"\1 00000",text)
    text = re.sub(r"([0-9])[ ]([0-9])",r"\1\2",text)
    return text

print(textToNumber("../testFiles/test.txt"))
