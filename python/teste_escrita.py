# -*- coding: UTF-8 -*-

#arquivo teste_escrita.py
arquivo = open("teste.txt", "w")
arquivo.write("Python rocks \n")
print(arquivo.mode) #print arquivo.mode
arquivo.close()