import re

def parsear_linha(linha):

    padrao = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.+)\] "([^ ]+) (\S+) HTTP\/1\.1" (\d+) (\d+)'

    dic_parser = re.search(padrao, linha)
    
    if dic_parser is None:
        return None

    resultado = {
        "ip": dic_parser.group(1),
        "data": dic_parser.group(2),
        "metodo": dic_parser.group(3),
        "caminho": dic_parser.group(4),
        "status": dic_parser.group(5),
        "tamanho": dic_parser.group(6)
    }
    return resultado

def ler_arquivo(logs):
    with open(logs, "r") as arquivo:

        dic_log = []

        for linha in arquivo:
            resultado = parsear_linha(linha.strip())

            if resultado is not None:
                dic_log.append(resultado) 

    return dic_log


def detectao(dic_log):

#PROJETO PAUSADO INDETERMINADAMENTE!!!
