import Source.MySqlClient as dbClient

obj = dbClient.DBAccess()

class Business:
    def login(self, username, password):
        isLogin = ""
        try:
            isLogin = obj.login(username, password)
        except:
            print('Something wrong, please check')
        finally:
            return isLogin