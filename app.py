from flask import Flask
from flask_socketio import SocketIO, send
import serial
import time
 
print(serial.Serial("COM6").closed)
# print(serial.Serial("COM6").open())
# arduino = serial.Serial("COM5",9600,timeout=0.1)
  
def write_read(x):
    print("is me arudino")
    string='X{0:d}Y{1:d}'.format((x+10//2),(x+50//2))
    # arduino.write(string.encode('utf-8'))
    time.sleep(1)
    # data = arduino.readline()
#     print(data)
     
# # send => send message to all clients in listen
# to this server

# Create App using flask

app = Flask(__name__)

#Add Secret to 
app.config['SECRET_KEY'] = "iotVibrator"

socket = SocketIO(app, cors_allowed_origins="*")
 
app.debug = True
 
#listen for the event named 'iotInit'

@socket.on('iotInit')
def handleIotInit(serialCode):
    write_read(serialCode)
    socket.emit("iotRecive", serialCode)
    send(serialCode, broadcast=True)
    return None

if __name__ == '__main__':
   socket.run(app, host="192.168.101.244", port=8060)


