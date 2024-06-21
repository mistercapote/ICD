# import string
# import re
# import json

def cleanNum(numero):
    numero = numero.replace("ou ", "").replace("R$\xa0", "").replace(",",".")
    numero = float(numero.split(" ")[0])
    return numero

def cleanData(data):
    if "esse" in data:
        return (0, 0)
    elif "ano" in data and ("mês" in data or "meses" in data):
        data = data.split(" ")
        return (int(data[0]), int(data[3]))
    elif "ano" in data:
        data = data.split(" ")
        return (int(data[0]), 0)
    else:
        data = data.split(" ")
        return (0, int(data[0]))

