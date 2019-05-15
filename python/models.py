# -*- coding: UTF-8 -*-

class Perfil(object):
    "Classe padrão para perfis de usuários"

    def __init__(self, nome, telefone, empresa):
        if(len(nome) < 3):
            raise ArgumentoInvalidoError("Nome deve ter pelo menos 3 caracteres")

        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        #print "Nome : %s, Telefone: %s, Empresa: %s, Curtidas: %s" % (self.nome, self.telefone, self.empresa, self.__curtidas)   
        print("Nome : %s, Telefone: %s, Empresa: %s, Curtidas: %s" % (self.nome, self.telefone, self.empresa, self.__curtidas))

    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

    #@staticmethod
    @classmethod
    def gerar_perfis(classe, nome_do_arquivo):
        arquivo = open(nome_do_arquivo, "r")
        perfis = []

        for linha in arquivo:
            valores = linha.split(",")

            if(len(valores) is not 3):
                raise Perfil_Error("Um linha do arquivo %s deve ter 3 valores" % nome_do_arquivo)

            perfis.append(Perfil(*valores))

        arquivo.close()

        return perfis


class Perfil_Vip(Perfil):
    "Classe padrão para perfis de usuários vips"

    def __init__(self, nome, telefone, apelido=""):
        super(Perfil_Vip, self).__init__(nome, telefone, apelido)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0


class ArgumentoInvalidoError(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)


class Perfil_Error(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)


class Data(object):
   def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano

   def imprime(self):
      print("%s/%s/%s" % (self.dia, self.mes, self.ano)) #print '%s/%s/%s' % (self.dia, self.mes, self.ano)


class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprime(self):
        imc = self.peso / (self.altura **2)
        print("O IMC de %s é: %s " %(self.nome, imc)) #print 'O IMC de %s é: %s ' %(self.nome, imc)