# src/app/order_status.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

# Simulate order status updates
def simulate_order_updates():
    import time
    statuses = ['Preparing', 'Cooking', 'Ready for Pickup', 'Delivered']
    for status in statuses:
        socketio.emit('order_status', {'status': status}, namespace='/')
        time.sleep(5)  # Simulate delay

if __name__ == '__main__':
    socketio.run(app)
