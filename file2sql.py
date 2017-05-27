# file2sql

"""
 Programa para ler um ficheiro de texto e carregar numa tabela linha a linha

 Ler o ficheiro no arg1 linha-a-linha
 Remover carateres perigosos
 Voltar a gravar o ficheiro ou inserir no SQL

 @Author: Filipe Santos
 @Created: 2017-05-27

"""

import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    print (filename)
else:
    print ("argument 1 is empty.")