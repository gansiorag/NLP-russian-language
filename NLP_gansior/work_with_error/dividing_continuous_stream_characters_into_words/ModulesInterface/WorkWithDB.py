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
    
    def queryDB(fQuery):
        def workers(*args):
            with DB(DbPath) as db:
                ss =fQuery()
                db.execute(ss)
        return workers  
        
    @classmethod
    @queryDB
    def createrTb():
        sql = "CREATE TABLE IF NOT EXISTS sourcesData ("\
            "guidsources text NOT NULL,"\
            "path_sours TEXT NOT NULL, "\
            "data_start TEXT NOT NULL "\
            ");"
        return sql
    
    @classmethod
    @queryDB
    def InsertDataTb_sourcesData():
        sql = "INSERT INTO sourcesData ("\
            "guidsources,"\
            "path_sours, "\
            "data_start"\
            ")"\
            " VALUES ('1', 'sdfgsdfg', 'sdfgsdfg'),"\
            "('2', 'sdfgsdfg', 'sdfgsdfg'),"\
            "('3', 'sdfgsdfg', 'sdfgsdfg'"\
            ");"
        return sql
    
    
def prog1():
   #WorkDB.createrTb() 
   WorkDB.InsertDataTb_sourcesData() 
    
if __name__ == '__main__':
    name=''
    # sql = "CREATE TABLE IF NOT EXISTS sourcesData (guidsources text NOT NULL, "\
    # "path_sours TEXT NOT NULL, data_start TEXT NOT NULL );"
    # print(sql)
    # with DB(DbPath) as cur:
    #     cur.execute(sql)
    prog1()
