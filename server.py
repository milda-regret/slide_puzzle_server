from flask import Flask, json, jsonify, send_from_directory, request
#from werkzeug.serving import WSGIRequestHandler
#WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

puzzles = { 'size' : 7, 'puzzle' : [
    { 'name' : 'puzzle1', 'type' : 'png', 'contributor': '에헬즈' },
    { 'name' : 'puzzle2', 'type' : 'png', 'contributor': '에헬즈' },
    { 'name' : 'puzzle3', 'type' : 'png', 'contributor': '에헬즈' },
    { 'name' : 'puzzle4', 'type' : 'png', 'contributor': '에헬즈' },
    { 'name' : 'puzzle5', 'type' : 'jpg', 'contributor': '에헬즈' },
    { 'name' : 'puzzle6', 'type' : 'jpg', 'contributor': '에헬즈' },
    { 'name' : 'puzzle7', 'type' : 'jpg', 'contributor': '에헬즈' },
]}

@app.route('/puzzles')
def get_puzzle_list():
    return jsonify(puzzles)

@app.route('/image/<image_name>')
def get_image(image_name):
    return send_from_directory('static', image_name, as_attachment=False)

@app.route('/user')
def get_user_profile():
    id = request.args.get('id')
    if (id is None):
        return 'usage: /user?id=<user id>'
    
    user = None
    user_list: list = list()
    with open('./list.json', 'r') as fd:
        user_list = json.load(fd)
        for u in user_list:
            if (u['id'] == id):
                user = u
                break

        # 등록되지 않은 사용자
    if (user is None):
        user = {'id': id, 'name': 'User', 'solved puzzle': []}
        user_list.append(user)
        with open('./list.json', 'w') as fd:
            json.dump(user_list, fd)
    
    return jsonify(user)

@app.route('/clear')
def clear_puzzle():
    id = request.args.get('id')
    puzzle = int(request.args.get('puzzle'))

    user = None
    user_list: list = list()
    with open('./list.json', 'r') as fd:
        user_list = json.load(fd)
        for u in user_list:
            if (u['id'] == id):
                user = u
                break

    if (user is None):
        return 'No user'
    
    for x in user['solved puzzle']:
        if (x == puzzle):
            return 'saved'
    
    user['solved puzzle'].append(puzzle)
    with open('./list.json', 'w') as fd:
        json.dump(user_list, fd)
    return 'saved'

if __name__ == '__main__':
    app.run(host='192.168.0.2', port=2456, debug=True)