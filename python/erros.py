from models import *

arquivo = None

try:
    arquivo = open("nao_existe.txt", "r")
    valores = arquivo.readline().split(":")
    Perfil(*valores)
    print("Arquivo foi aberto")
    arquivo.close()
except (IOError, TypeError) as erro:
    print("Deu Erro %s" % erro)
finally:
    if(arquivo is not None):
        print("Fechando arquivo")
        arquivo.close()

# try:
#     with open("nao_existe.txt", "r") as arquivo:
#         for linha in arquivo:
#             print(linha) #print linha
# except:
#     print("Erro")

# except IOError as erro:
#     print("Deu IOError %s" % erro)
# except TypeError as erro:
#     print("Deu TypeError %s" % erro)