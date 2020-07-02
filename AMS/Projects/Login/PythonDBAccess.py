import pypyodbc
import db_access as dbconn

def main():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete ')
    choice = input('Choose your option = ')
    
    obj = dbconn.DBAccess()

    if choice == 'C':
        name = input('Enter your name = ')
        age = input('Enter your age = ')
        obj.func_CreateData(name, age)
    elif choice == 'R':
        obj.func_ReadData()
    elif choice == 'U':
        id = input('Enter your id = ')
        name = input('Enter your name = ')
        age = input('Enter your age = ')
        obj.func_UpdateData(id, name, age)
    elif choice == 'D':
        id = input('Enter your id = ')
        obj.func_DeleteData(id)
    else:
        print('Wrong choice, You are going exist.')

# Call the main function
main()