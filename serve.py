from flask import Flask, request
import json
import subprocess
import socket
app = Flask(__name__)
currSeed = 0

@app.route('/', methods= ['POST', 'GET'])
def fungo():
    if request.method == 'POST':
        subprocess.Popen(["python3", "stress_cpu.py"])
    return str(socket.gethostname())
        
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)