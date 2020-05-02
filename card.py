import pymysql
from baseObject import baseObject
class cardList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('Cards')
        

    def verifyNew(self,n=0):
        import re
        if len(self.data[n]['cardName']) == 0:
            self.errorList.append("card name cannont be blank")
       
        if len(self.data[n]['cardPrice']) == 0:
            self.errorList.append("price cannont be blank")
               
        if len(self.errorList) > 0:
            return False
        else:
            return True

        
    def tryLogin(self,email,pw):
        sql = 'SELECT * FROM `' + self.tn + '` WHERE `email` = %s AND `password` = %s;'
        tokens = (email,pw)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        n=0
        for row in cur:
            self.data.append(row)
            n+=1
        if n > 0:
            return True
        else:
            return False
