from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return app.send_static_file('index.html')
# @app.route('/favicon.ico')
# def favicon():
# 	return app.send_static_file('favicon.ico')
@socketio.on('message')
def handle_message(data):
	socketio.emit('push', data, broadcast = True, include_self = False)

if __name__ == '__main__':
	socketio.run(app)
