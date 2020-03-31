import pymysql
from baseObject import baseObject
class productList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('grinnecw_product')
        
    def verifyNew(self,n=0):
        import re
        if len(self.data[n]['pid']) == 0:
            self.errorList.append("PID cannont be blank")
        
        if len(self.data[n]['sku']) == 0:
            self.errorList.append("sku cannont be blank")
        
        if len(self.data[n]['name']) == 0:
            self.errorList.append("First name cannont be blank")

        if float(self.data[n]['price']) == 0:
            if float(self.data[n]['price']) < 0:
                self.errorList.append("price cannont be less than 0")
            else:
                self.errorList.append("First name cannont be blank")


        if len(self.errorList) > 0:
            return False
        else:
            return True