# file2sql

"""
Programa para ler um ficheiro de texto e carregar numa tabela linha a linha

OK Ler o ficheiro no arg1 linha-a-linha
OK Remover carateres perigosos
OK Voltar a gravar o ficheiro
Ler ficheiro de parametros para ligação ao SQL
Integrar ficheiro no SQL ou
Executar SQLCMD para integrar o ficheiro

@Author: Filipe Santos
@Created: 2017-05-27

@Version: 0.2 b
@Copyright: PSC - Pinto Santos Consultores - 2017

"""

import sys
#import subprocess

#
# TEST AREA
#

#
# END OF TEST AREA
#

sqltable = "TABELA"
sqlcolumn = "COLUNA"

if len(sys.argv) > 1:
    original_file = sys.argv[1]
    tempfile = open("tempfile.sql", 'w')
    file_lines = open(original_file).read().splitlines()
    with open("tempfile.sql", 'w') as tempfile:
        for idx, file_line in enumerate(file_lines):
            sqlvalue = file_line.replace("'", " ")
            new_file_line="insert into %s (%s) values ('%s');\n" % (sqltable, sqlcolumn, sqlvalue)
            tempfile.write(new_file_line)

else:
    print("argument 1 is empty.")
