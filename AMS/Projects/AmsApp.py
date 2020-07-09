from flask import Flask, request, jsonify
import Source.BusinessLayer as business

app = Flask(__name__)
#app.debug = True

class MiddlewareGateway(object):
#class for URL sorting 
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].lower().replace('/authiot','').startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'].lower().replace('/authiot','')[len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'application/json')])            
            return ["This url does not belong to the app.".encode()]


app.wsgi_app = MiddlewareGateway(app.wsgi_app, prefix='/therams')


connect = business.Business()

@app.route('/bar')
def bar():    
    return "The URL for this page is {}"

@app.route('/login', methods=['POST'])
def login():
    isSuccess = ''
    req_data = request.get_json()
    username = req_data['username']
    password = req_data['password']
    try:
        isSuccess = connect.login(username, password)        
    except:
       raise Exception('We have a problem')         
    return jsonify(isSuccess)

if __name__ == '__main__':
    app.run()