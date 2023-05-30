from flask import Flask
#from werkzeug.serving import WSGIRequestHandler
#WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)

@app.route('/')
def handshake():
    return 'Hello, world!'

@app.route('/puzzle')
def get_puzzle_list():
    pass

@app.route('/image')
def get_image():
    pass

@app.route('/user')
def get_user_profile():
    pass

if __name__ == '__main__':
    app.run(host='192.168.0.2', port=2456)