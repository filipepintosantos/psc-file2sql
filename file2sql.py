# file2sql

"""
Program to read text file and insert each line in a SQL Server database table as one column

@Author: Filipe Santos
@Created: 2017-05-27
@LastUpdate: 2017-05-28

@Version: 1.0
@Copyright: PSC - Pinto Santos Consultores - 2017

"""

import sys
import imp
import pypyodbc

# Se o argv[1] não estiver preenchido não faz nada
if len(sys.argv) > 1:
    # ler o ficheiro de parametros file2sql.ini para carregar diversas variaveis
    with open("file2sql.ini", 'r') as parm_file:
        parm = imp.load_source('data', '', parm_file)
        if parm.sql_server == ".":
            parm.sql_server = "localhost"
        # argv[1] é o nome do ficheiro a importar para o sql
        original_file = sys.argv[1]
        file_lines = open(original_file).read().splitlines()
        with open("query.sql", 'w') as query_file:
            for idx, file_line in enumerate(file_lines):
                sqlvalue = file_line.replace("'", " ")
                new_file_line = "insert into %s (%s) values ('%s');\n" % (parm.sql_table, parm.sql_column, sqlvalue)
                query_file.write(new_file_line)
        if parm.sql_auth == "windows":
            conn_str = 'Driver={SQL Server Native Client 11.0}; Server=%s; Database=%s; Trusted_Connection=yes;' % (parm.sql_server, parm.sql_catalog)
        else:
            conn_str = 'Driver={SQL Server Native Client 11.0}; Server=%s; Database=%s; uid=%s; pwd=%s' % (parm.sql_server, parm.sql_catalog, parm.sql_user, parm.sql_password)
        connection = pypyodbc.connect(conn_str)
        query_lines = open("query.sql", 'r').read().splitlines()
        for idx, query_line in enumerate(query_lines):
            connection.cursor().execute(query_line)
        connection.commit()
        connection.close()
else:
    print("Argument 1 is empty. Exited")
