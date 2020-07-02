from ErrorHandler.AMSError import AMSError
import mysql.connector
import configuration as config


class connect:   

    def __init__(self,sql):
        self.sql = sql
     
    try:   
        db = mysql.connector.connect(host=config.MySQLDATABASE_CONFIG["host"],user=config.MySQLDATABASE_CONFIG["host"], password=config.MySQLDATABASE_CONFIG["host"])
        cursor = db.cursor()

        def execute(self):
                try:
                    cursor.execute(self.sql)
                    results = cursor.fetchone()
                    if(results.count > 0):
                        return 'Success'
                    else:
                        return 'Failed'
                except:
                    print("Error: unable to fecth data")
        db.close()
    except mysql.connector.Error as err: 
        
        db.close()
        raise AMSError("Cannot connecto to db")
        
    