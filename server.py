from flask import Flask, json, jsonify, send_from_directory, request
#from werkzeug.serving import WSGIRequestHandler
#WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Server on!'

puzzles = { 'size' : 7, 'puzzle' : [
    { 'name' : '1', 'type' : 'png', 'contributor': '에헬즈' },
    { 'name' : '2', 'type' : 'png', 'contributor': '에헬즈' },
    { 'name' : '3', 'type' : 'png', 'contributor': '에헬즈' },
    { 'name' : '4', 'type' : 'png', 'contributor': '에헬즈' },
    { 'name' : '5', 'type' : 'jpg', 'contributor': '에헬즈' },
    { 'name' : '6', 'type' : 'jpg', 'contributor': '에헬즈' },
    { 'name' : '7', 'type' : 'jpg', 'contributor': '에헬즈' },
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
        user = {'id': id, 'name': 'User', 'solved_puzzle': []}
        user_list.append(user)
        with open('./list.json', 'w') as fd:
            json.dump(user_list, fd)
    
    return jsonify(user)

@app.route('/user', methods=['POST'])
def change_user_name():
    data = request.get_json(silent=True)
    if (data is None):
        return 'usage: POST /user \{ "id": "<ID>", "name": "<NAME>" \}'
    data['id'] = str(data['id'])
    
    user = None
    user_list: list = list()
    with open('./list.json', 'r') as fd:
        user_list = json.load(fd)
        for u in user_list:
            if (u['id'] == data['id']):
                user = u
                break

    if (user is None):
        return 'No user'
    
    user['name'] = data['name']
    with open('list.json', 'w') as fd:
        json.dump(user_list, fd)
    return 'name changed'

@app.route('/user', methods=['DELETE'])
def delete_user():
    id = request.args.get('id')
    if (id is None):
        return 'usage: DELETE /user?id=<user id>'
    
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
        return 'No user'
    
    user_list.remove(user)
    with open('./list.json', 'w') as fd:
            json.dump(user_list, fd)
    
    return 'delete success'

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
    
    for x in user['solved_puzzle']:
        if (x == puzzle):
            return 'saved'
    
    user['solved_puzzle'].append(puzzle)
    with open('./list.json', 'w') as fd:
        json.dump(user_list, fd)
    return 'saved'

if __name__ == '__main__':
    app.run(host='192.168.0.2', port=2456, debug=True)
