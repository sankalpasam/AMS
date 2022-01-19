import mysql.connector
#import Source.AMSError

class DBAccess:
    def getConnection():
        connection = mysql.connector.connect(
            host="localhost",
            database="testingcmms",
            user="amsadmin",
            password="amsadmin"
            )
        return connection

    def login(self, username, password):
        result = ""
        connection = DBAccess.getConnection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT 'Success' FROM user where emailid = '"+username+"' and password = '"+password+"'")
            results = cursor.fetchone()
            if "Success" in results[0]:
                result = "Success"
            else:
                result = "Failed"
        except:
            result = "Failed"
        finally:
            connection.close()        
        return result
            #raise AMSError("Cannot connecto to db")
