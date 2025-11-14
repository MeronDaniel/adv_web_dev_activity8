from flask import Flask, jsonify, request

app = Flask(__name__)

app.echos = {}


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/echo/<int:echo_id>', methods=['PUT'])
def echo_put(echo_id):
    data = request.get_json(force=True)
    msg = data.get('msg')

    updated_echo = {'id': echo_id, 'msg': msg}

    return jsonify(
        updated_echo
    ), 201


@app.route('/echo/<int:echo_id>', methods=['DELETE'])
def echo_delete(echo_id):

    if echo_id not in app.echos:
        return jsonify({'error': 'Task not found'}), 404

    del app.echos[echo_id]

    return jsonify({
        "message": "Echo has been deleted!"
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
