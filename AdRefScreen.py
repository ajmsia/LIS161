from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['JAS'] = 'JAS'  # Add your secret key here
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    socketio.emit('server_response', {'data': 'Connected'})

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

@socketio.on('client_message')
def on_message(message):
    socketio.emit('server_response', {'data': message['data']})

if __name__ == '__main__':
    socketio.run(app)
