from flask import Flask, url_for ,render_template,jsonify,request
from DataAccess.MySqlClient import connect

app = Flask(__name__)
#app.debug = True

class MiddlewareGateway(object):
#class for URL sorting 
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].lower().replace('/flask','').startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'].lower().replace('/flask','')[len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'application/json')])            
            return ["This url does not belong to the app.".encode()]


app.wsgi_app = MiddlewareGateway(app.wsgi_app, prefix='/ams')

@app.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()
    username = req_data['username']
    password = req_data['password']
    try:
        data = connect.execute("select 'success' from user where username = '"+ username +"' and password = '"+ password+"'")
        
    except:
       raise Exception('We have a problem')
         
    return jsonify(data)
            
    #data = {username:username,password:password}
    
	
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9010)