import json

import mysql.connector as MC
import requests


class Database:
    """class used to connect to the database and make modifications"""

    def __init__(self):
        """Connection to the database"""
        try:
            self.conn = MC.connect(user='root', password='', host='localhost', database='pur_beurre')
            self.cursor = self.conn.cursor()

            #sql = "INSERT INTO store(Name_store, Adress_store, Lien_store) VALUES(%s, %s, %s)"
            #infos = ("magasin2", "fass", "fass.com")
            #cursor.execute(sql, infos)
            #self.conn.commit()

            #sql1 = "SELECT * FROM store"
            #cursor.execute(sql1)

            #result = cursor.fetchall()

            #for rs in result:
                #print('Nom : {}'.format(rs[1]))

        except MC.Error as error:
            print(error)
        finally:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()

    def get_category(self):
        """get categories from the URL API"""
        url = 'https://fr.openfoodfacts.org/categories&json=1'
        headers = {'with': 'name'}
        r = requests.get(url, headers=headers)
        text_json = json.loads(r.text)
        i = 1
        for name in text_json['tags']:
            while i < 11:
                add_category = "INSERT INTO category(Name_category) VALUES(%s)"
                category_infos = name['name']
                self.cursor.execute(add_category, category_infos)
                self.conn.commit()
                i = i + 1
