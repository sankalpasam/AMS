
import Source.BusinessLayer as business

connect = business.Business()

username = "ram@gmail.com"; #req_data['username']
password = "12345"; #req_data['password']
try:
    isSuccess = connect.login(username, password)
    print(isSuccess)
except:
    raise Exception('We have a problem')
