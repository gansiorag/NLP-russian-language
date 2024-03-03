'''
 This module make
        Args:
            Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
            Starting 2022//
            Ending 2022//
'''

import sqlite3
import os
from termcolor import cprint

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta
# on_cyan on_white
# Attributes: bold dark underline blink reverse concealed


DbPath = os.getcwd().split('NLP-russian-language')[0] +\
    'NLP-russian-language/NLP_gansior/work_with_error/' +\
    'dividing_continuous_stream_characters_into_words/' +\
    'rezultResearch/comBase.db'
cprint(DbPath, 'red')


class DB:
    """AI is creating summary for
    """
    def __init__(self, path: str):
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


def selectDB(fQ):
    def workers(self, *arg):
        ss = fQ(self, *arg)
        with DB(DbPath) as cur:
            cur.execute(ss)
            return cur.fetchall()
    return workers


def insertDB(fQ):
    def ww(self, *arg):
        ss = fQ(self, *arg)
        with DB(DbPath) as cur:
            cur.execute(ss)
    return ww


class WorkDB(DB):
    """_summary_

    Args:
        DB (_type_): _description_
    """

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
    def selectTypeSources(self):
        sql = "SELECT guidtema, name_tema FROM TemasSources;"
        return sql

    @insertDB
    def InsertDataTb_Tema(self, row: dict):
        cprint(str(row), 'red')
        sql = "INSERT INTO TemasSources (guidtema, name_tema)"\
            " VALUES ('{guidtema}', '{name_tema}');".format_map(row)
        cprint(sql, 'red')
        return sql

    @selectDB
    def get_name_file(self, name_file: str):
        """AI is creating summary for getNameFile

        Args:
            nameFile (str): [description]

        Returns:
            [type]: [description]
        """
        sql = "SELECT guidsources, path_sours, data_start, " + \
            "nameFile, guidtema " + \
            "FROM sourcesData " + \
            f"WHERE nameFile = '{name_file}';"
        return sql

    @selectDB
    def get_all_sources(self):
        """AI is creating summary for getNameFile

        Args:
            nameFile (str): [description]

        Returns:
            [type]: [description]
        """
        sql = "SELECT guidsources, path_sours, data_start, " + \
            "nameFile, guidtema " + \
            "FROM sourcesData;"
        return sql


db = WorkDB(DbPath)


# test part
if __name__ == '__main__':
    name = ''
    db = WorkDB(DbPath)

    data_sq = {'guidtema': 'qwfqfqqf23523ef53t35t',
               'name_tema': 'probas tema 1'}
    db.InsertDataTb_Tema(data_sq)
    print()
    FF = db.selectTypeSources()
    print(FF)
    FF = db.get_all_sources()
    print()
    print(FF)
