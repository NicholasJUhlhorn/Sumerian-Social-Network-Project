from getpass import getpass
from mysql.connector import connect, Error

class SQLfuncs(object):
    connection = None

    def __init__(self, hostname, username, userpassword):
        try:
            self.connection = connect(
                host=hostname,
                user=username,
                password=userpassword,
                database='sumerianDB'
            )
            #print('Connection to sumerian-social-network successful')
        except Error as e:
            print(f"The error '{e}' occurred")

    def addNameToTab(self, name, tabid):
        cursor = self.connection.cursor()
        year = self.sanitizeInput(name)
        addNameQuery = 'INSERT INTO rawnames (name, tabid) VALUES (\'' + name + '\', \'' + tabid + '\');'
        try:
            cursor.execute(addNameQuery)
            self.connection.commit()
            #print('Added name successfuly')
        except Error as e:
            print(f"The error '{e}' occurred")

    def addYearToTab(self, year, tabid):
        cursor = self.connection.cursor()
        year = self.sanitizeInput(year)
        addYearQuery = 'INSERT INTO rawyears (year, tabid) VALUES (\'' + year + '\', \'' + tabid + '\');'
        try:
            cursor.execute(addYearQuery)
            self.connection.commit()
            #print('Added year successfuly')
        except Error as e:
            print(f"The error '{e}' occurred")

    def addBestYearToTab(self, bestYear, tabid, similarity):
        cursor = self.connection.cursor()
        bestYear = self.sanitizeInput(bestYear)
        addBestYearQuery = 'INSERT INTO bestyears (year, tabid, similarity) VALUES (\'' + bestYear + '\', \'' + tabid +'\', \'' + similarity +'\');'
        try:
            cursor.execute(addBestYearQuery)
            self.connection.commit()
            #print('Added year successfuly')
        except Error as e:
            print(f"The error '{e}' occurred")

    def getAttribute(self, attribute, relation):
        cursor = self.connection.cursor()
        getAttributeQuery = 'SELECT ' + attribute + ' FROM ' + relation + ';'
        try:
            cursor.execute(getAttributeQuery)
            print('Fetched data successfuly')
            return cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        print(query)
        try:
            data = cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")
            return None

    def count(self, relation, attribute):
        cursor = self.connection.cursor()
        relation = self.sanitizeInput(relation)
        attribute = self.sanitizeInput(attribute)
        getCountQuery = 'SELECT COUNT(' + attribute + ') FROM ' + relation + ';'
        try:
            data = cursor.execute(getCountQuery)
            print('Fetched data successfuly')
            return data
        except Error as e:
            print(f"The error '{e}' occurred")


    def sanitizeInput(self, input):
        out = ""
        for i in range(len(input)):
            out += input[i]
            if input[i] == '\'':
                out += '\''
        return out