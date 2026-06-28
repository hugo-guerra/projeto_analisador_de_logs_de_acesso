import re

def parsear_linha(linha):

    padrao = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.+)\] "([^ ]+) (\S+) HTTP\/1\.1" (\d+) (\d+)'

    dic_parser = re.search(padrao, linha)

    resultado = {
        "ip": dic_parser.group(1),
        "data": dic_parser.group(2),
        "metodo": dic_parser.group(3),
        "caminho": dic_parser.group(4),
        "status": dic_parser.group(5),
        "tamanho": dic_parser.group(6)
    }
    return resultado

linha = '192.168.1.5 - - [26/Jun/2026:10:24:01 +0000] "POST /login HTTP/1.1" 401 512'
print(parsear_linha(linha))