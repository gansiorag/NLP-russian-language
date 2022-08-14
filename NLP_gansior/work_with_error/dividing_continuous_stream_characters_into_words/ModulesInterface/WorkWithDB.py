'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
    
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
'''

import os
import sqlite3

DbPath = os.getcwd().split('NLP-russian-language')[0] + 'NLP-russian-language/NLP_gansior/work_with_error/dividing_continuous_stream_characters_into_words/rezultResearch/comBase.db'
cprint(DbPath, 'red')
    
class DB:
    def __init__(self, path:str):
        self.path = path
        
    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()
        return self.cur
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        
 
class WorkDB:

    
    def selectDB(fQ):
        def workers(*arg):
            ss = fQ(*arg)
            with DB(DbPath) as cur:
                cur.execute(ss)
                return cur.fetchall()
        return workers 
        
    # @classmethod
    # @queryDB
    # def createrTb():
    #     sql = "CREATE TABLE IF NOT EXISTS sourcesData ("\
    #         "guidsources text NOT NULL,"\
    #         "path_sours TEXT NOT NULL, "\
    #         "data_start TEXT NOT NULL "\
    #         ");"
    #     return sql
    
    @selectDB
    def selectTypeSources():
        sql = "SELECT guidtema, name_tema FROM TemasSources;"
        return sql
    
    def insertDB(fQ):
        def ww(*arg):
            ss = fQ(*arg)
            with DB(DbPath) as cur:
                cur.execute(ss)
        return ww
        
    @insertDB
    def InsertDataTb_Tema(self, row:dict):
        cprint(row, 'red')
        sql = "INSERT INTO TemasSources (guidtema, name_tema)"\
            " VALUES ('{guidtema}', '{name_tema}');".format_map(row)
        cprint(sql, 'red')
        return sql
    
    
    
    
# def prog1():
#    #WorkDB.createrTb() 
#    WorkDB.InsertDataTb_sourcesData()
    
# if __name__ == '__main__':
#     name=''
#     # sql = "CREATE TABLE IF NOT EXISTS sourcesData (guidsources text NOT NULL, "\
#     # "path_sours TEXT NOT NULL, data_start TEXT NOT NULL );"
#     # print(sql)
#     # with DB(DbPath) as cur:
#     #     cur.execute(sql)
#     prog1()
