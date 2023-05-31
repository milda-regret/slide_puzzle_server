from flask import Flask, jsonify, send_from_directory
#from werkzeug.serving import WSGIRequestHandler
#WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

puzzles = {
    'puzzle1' : ['png', '에헬즈'],
    'puzzle2' : ['png', '에헬즈'],
    'puzzle3' : ['png', '에헬즈'],
    'puzzle4' : ['png', '에헬즈'],
    'puzzle5' : ['jpg', '에헬즈'],
    'puzzle6' : ['jpg', '에헬즈'],
    'puzzle7' : ['jpg', '에헬즈'],
}

@app.route('/puzzles')
def get_puzzle_list():
    return jsonify(puzzles)

@app.route('/image/<image_name>')
def get_image(image_name):
    return send_from_directory('static', image_name, as_attachment=True)

@app.route('/user')
def get_user_profile():
    pass

if __name__ == '__main__':
    app.run(host='192.168.0.2', port=2456, debug=True)