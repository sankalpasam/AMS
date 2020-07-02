import pypyodbc
import configuration

#CREATE DATABASE Test
#GO
#USE Test
#GO
#CREATE TABLE Employee(Id int PRIMARY KEY IDENTITY(1,1),	Name varchar(255) NULL,	Age int NULL)

class DBAccess:
    # Return the sql connection 
    def getConnection():
         connection = pypyodbc.connect("Driver= {"+config.DATABASE_CONFIG["Driver"]+"};Server=" + config.DATABASE_CONFIG["Server"] + ";Database=" + config.DATABASE_CONFIG["Database"] + ";uid=" + config.DATABASE_CONFIG["UID"] + ";pwd=" + config.DATABASE_CONFIG["Password"]) 
         return connection 

    def func_CreateData(self, name, age):
            # Get the sql connection
            connection = DBAccess.getConnection()
            try:
               query = "Insert Into Employee(Name, Age) Values(?,?)" 
               cursor = connection.cursor()
               # Execute the sql query
               cursor.execute(query, [name, age])
               # Commit the data
               connection.commit()
               print('Data Saved Successfully')
            except:
                 print('Something wrong, please check')
            finally:
               # Close the connection
               connection.close()

    def func_ReadData(self):   
            # Get the sql connection
            connection = DBAccess.getConnection()
            cursor = connection.cursor()
            # Execute the sql query
            cursor.execute('Select * from Employee')
            # Print the data
            for row in cursor:
                print('row = %r' % (row,))

    def func_UpdateData(self, id, name, age):
            # Get the SQL connection
            connection = DBAccess.getConnection()
            try:
               # Fetch the data which needs to be updated
               sql = "Select * From Employee Where Id = ?" 
               cursor = connection.cursor()
               cursor.execute(sql, [id])
               item = cursor.fetchone()
               print('Data Fetched for Id = ', id)
               print('ID\t\t Name\t\t\t Age')
               print('-------------------------------------------')       
               print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
               print('-------------------------------------------')
               print('Enter New Data To Update Employee Record ')

               query = "Update Employee Set Name = ?, Age =? Where Id =?" 
       
               # Execute the update query
               cursor.execute(query, [name, age, id])
               connection.commit()
               print('Data Updated Successfully')
            except:
                 print('Something wrong, please check')
            finally:
               # Close the connection
               connection.close()

    def func_DeleteData(self, id):
            # Get the SQL connection
            connection = DBAccess.getConnection()
            try:
               # Get record which needs to be deleted
               sql = "Select * From Employee Where Id = ?" 
               cursor = connection.cursor()
               cursor.execute(sql, [id])
               item = cursor.fetchone()
               print('Data Fetched for Id = ', id)
               print('ID\t\t Name\t\t\t Age')
               print('-------------------------------------------')       
               print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
               print('-------------------------------------------')
               confirm = input('Are you sure to delete this record (Y/N)?')

               # Delete after confirmation
               if confirm == 'Y':
                   deleteQuery = "Delete From Employee Where Id = ?"
                   cursor.execute(deleteQuery,[id])
                   connection.commit()
                   print('Data deleted successfully!')
               else:
                    print('Wrong Entry')
            except:
                print('Something wrong, please check')
            finally:
                connection.close()
