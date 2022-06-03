# wRATh

wRATh is an open source Remote Administration Tool fully developed in Python.
I've been learning more about the TkInterface and have decided to implement it on the server for a half-way decent GUI.
This is the first tool I've release for the public and will be continuing to develop it as time goes on - hope you enjoy!

**Username & Password: admin**

**Client Capabilities**
- Can retreive commands from the Server
- Will execute commands retrieved from the Server
- Will deliver the results back to the Server.
- Traffic is simply encoded/decoded by way of Python capabilities
- Client is able to be run on both Linux & Windows OS (MAC OS functionality is in progress)


**Server Capabilities**
- Will queue tasks for client to retrieve.
- Operator will be able to review task results. A blank space means there is some sort of syntax error on your end.
- Configurable Server (Feel free to change the port as well as the host)


**FUTURE PLANS**
- Upload/Download file feature (although this may be possible by creating an additional server on your machine and using "wget" or "certutil" commands, respectively.)
- Kill command (it works now but sends some error).

**DEPENDENCIES**
- Python 3.x.x
- Tkinterface
- any .png file named "index1.png" (I know this is a pain - I'm working on it). I've provided one to help out :)
