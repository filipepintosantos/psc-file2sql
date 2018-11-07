# psc-file2sql v1.0.2 - 2017-06-30
Pinto Santos Consultores - File2SQL

Program to read text file and insert each line in a SQL Server database table as one column

ini options:
log_level = "INFO" / "DEBUG"
sql_driver = "{SQL Server Native Client 11.0}" - Check available driver
sql_server = "." - Server name (. = localhost)
sql_catalog = "DBforTests" - database name
sql_auth = "windows" / "native"
sql_user = "sa" - only used with sql_auth = native
sql_password = "sa_Passw0rd" - only used with sql_auth = native
sql_table = "TestTable1"
sql_column = "full_row"
sql_filename = "INCLUDE" / "NO"
path_in = "."
path_out = "."
