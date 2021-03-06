import pymysql
from baseObject import baseObject
class customerList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('grinnecw_customers')
        
    def verifyNew(self,n=0):
        import re
        if len(self.data[n]['fname']) == 0:
            self.errorList.append("First name cannont be blank")
       
        if len(self.data[n]['lname']) == 0:
            self.errorList.append("Last name cannont be blank")
       
        if len(self.data[n]['email']) == 0:
            self.errorList.append("Email cannont be blank")

        elif re.match('[^@]+@[^@]+\.[^@]+',self.data[n]['email']):
            pass
        else:
            self.errorList.append("Email address invalid, check for @ and TLD (i.e. .com, .edu, .gov, etc.")

        if len(self.data[n]['password']) == 0:
            self.errorList.append("Password cannont be blank")
        elif len(self.data[n]['password']) < 4:
            self.errorList.append("Password must be longer than 4 characters")
       
        if len(self.data[n]['subscribed']) == 0:
            self.errorList.append("Subscription cannont be blank")
        elif self.data[n]['subscribed'] != 'True':
            if self.data[n]['subscribed'] != 'False':
                self.errorList.append("Subscription must be True or False")
        
        if len(self.errorList) > 0:
            return False
        else:
            return True

    def verifyChange(self,n=0):
        self.errorList = []
        
        c = customerList()
        c.getByField('email',self.data[n]['email'])
        #print(c.data)
        if len(c.data) > 0:
            print(self.data[n])
            print(c.data[0])
            if str(self.data[n]['id']) != str(c.data[0]['id']):
                self.errorList.append("Email address is already registered.")
        
        
        if len(self.data[n]['fname']) == 0:
            self.errorList.append("First name cannot be blank.")
        if len(self.data[n]['lname']) == 0:
            self.errorList.append("Last name cannot be blank.")
        
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
