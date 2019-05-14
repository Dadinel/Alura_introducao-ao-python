def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    #print '%s %s' % (parte1, parte2)
    return parte1 + " " + parte2

def envia_convite(nome_convidado):
    print("Enviando convite para %s" %(nome_convidado)) #print "Enviando convite para %s" %(nome_convidado)

def processa_convite(nome_convidado):
    nome_formatado = gera_nome_convite(nome_convidado)
    envia_convite(nome_formatado)

def cadastrar(nomes):
   print("Digite o nome:") #print "Digite o nome:"
   nome = input() #raw_input()
   nomes.append(nome)

def remover(nomes):
   print("Qual nome gostaria de remover?") #print "Qual nome gostaria de remover?""
   nome = input() #raw_input()
   nomes.remove(nome)