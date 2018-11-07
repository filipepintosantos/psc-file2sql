# file2sql

"""
Program to read text file and insert each line in a SQL Server database table as one column

## Develoment plan
logging to everything

@Author: Filipe Santos
@Created: 2017-05-27
@LastUpdate: 2018-11-07

@Version: 1.1.0
@Copyright: PSC - Pinto Santos Consultores - (2017, 2018)

"""

import logging
import sys
import imp
import importlib
import pypyodbc

logging.basicConfig(filename='file2sql.log', format='%(asctime)s : %(levelname)-8s : %(name)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("#"*80)
logger.info("file2sql start program log.")
logger.info("Logging level set to INFO.")

if len(sys.argv) < 1:
    logger.info("Argument 1 is empty. Exited")
    sys.exit()

try:
    logger.info("Opening ini file to read parameters.")
    with open("file2sql.ini", 'r') as parm_file:
        parm = imp.load_source('data', '', parm_file) #imp is deprecated
        if parm.log_level != "INFO":
            logger.setLevel(logging.getLevelName(parm.log_level))
            logger.info("Logging level changed to %s.", parm.log_level)
        if parm.sql_server == ".":
            parm.sql_server = "localhost"
        original_file = sys.argv[1]
        logger.info("Opening data file: %s", original_file)
        file_lines = open(original_file).read().splitlines()
        logger.info("Creating file with prepared SQL Statements.")
        with open("file2sql.sql", 'w') as query_file:
            for idx, file_line in enumerate(file_lines):
                logger.debug("Preparing line %s.", idx)
                if parm.sql_filename == "INCLUDE":
                    logger.info("Include file name in column line value.")
                    sqlvalue = original_file + ":" + file_line.replace("'", " ")
                else:
                    logger.info("Don't include file name in column line value.")
                    sqlvalue = file_line.replace("'", " ")
                new_file_line = "insert into %s (%s) values ('%s');\n" % (parm.sql_table, parm.sql_column, sqlvalue)
                query_file.write(new_file_line)
        conn_str = 'Driver=%s; Server=%s; Database=%s;' % (parm.sql_driver, parm.sql_server, parm.sql_catalog)
        if parm.sql_auth == "windows":
            conn_str += ' Trusted_Connection=yes;'
        else:
            conn_str += ' uid=%s; pwd=%s' % (parm.sql_user, parm.sql_password)
        logger.info("SQL Connection string used: %s", conn_str)
        connection = pypyodbc.connect(conn_str)
        query_lines = open("file2sql.sql", 'r').read().splitlines()
        for idx, query_line in enumerate(query_lines):
            logger.debug("Inserting to SQL: line %s.", idx)
            logger.debug("Line: %s", query_line)
            connection.cursor().execute(query_line)
        connection.commit()
        connection.close()
    logger.info("Processing finished. Exited")
except Exception:
    logging.exception("")
