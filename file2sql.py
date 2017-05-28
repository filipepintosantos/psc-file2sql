# file2sql

"""
Programa para ler um ficheiro de texto e carregar numa tabela linha a linha

Ler o ficheiro no arg1 linha-a-linha
Remover carateres perigosos
Voltar a gravar o ficheiro
Ler ficheiro de parametros para ligação ao SQL
Integrar ficheiro no SQL ou
Executar SQLCMD para integrar o ficheiro

@Author: Filipe Santos
@Created: 2017-05-27

@Version: 0.1 b
@Copyright: PSC - Pinto Santos Consultores - 2017

"""

import sys
#import subprocess

if len(sys.argv) > 1:
    originalfile = sys.argv[1]
    print(originalfile)
else:
    print("argument 1 is empty.")
