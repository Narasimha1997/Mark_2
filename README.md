# Mark_2
A Django platform to transfer large files between your Phone and your Personal Computer.
<h1>Mark_2</h1>

A Django platform to transfer large files between your Phone and your Personal Computer.

<h2>Mark_2</h2>

<h3>A brief introduction:</h3>

<p>Using USB cables to transfer files from your phone is always a tedious task, any distortion or damage in the wire, your entire job will be wasted for no reason, and also the transmission is slow and many phones does not support USB transmission because of security reasons if the target PC has an older OS or some out-dated components. We all use websites like filckr, facebook etc to upload pictures, We all know about dropbox where you can upload documents and other files and use it on any connected device, but dropbox is very slow if we upload large files this is not the drawback of dropbox development team, but it is due to fact that server is present far away from you, which imparts long routes for data transmission, Hence it is slow. Mark_2 works on the same client-server model. Client is your phone and server is your Laptop/PC. Thanks to python's new web server framework Django, it provides a stable sever model for your machine, it is secure too.</p>

<h2> A brief working procedure </h2>

<p>The application conatins an interface built by combining Python and C Languages. The C program provides an executable (.exe) interface for the users (Mark_2.exe), The application is currently CLI, but GUI will be provided in next release. The interface provides a real-time error detection utility and also user can call the package installer , configuration manager anytime. Package installer uses pip to automatically download all dependencies for running python APIs and to run the server. Configuration manager automatically configures the app for your use, but the automatic error detection and configuration takes place each time you run the app.

Next, the interface.py is the main module required to interact with the server and other parts of the app. C program simply calls interface.py which then executes the remaining parts and also if everything went fine the server will be started.

server-http conytains all code to start the server and it uses django base tools, allowed_hosts.txt file will be created everytime you create a server to notify it the current connection is secure. You no need to have any knowledge of your IP address to start the transfer, core packages of mark_2 will automatically detect your IP address and by default it can create a server running at port 8000. Therefore, the url of your host will be: https://YOUR_IP:8000/.</p>

 <h3>How to use<h3>

<h4> Requirements: </h4>

<p>A suitable python interpreter with path set, pip will be installed by default. (Python 3.4+ is recommended)

Dependencies: All dependencies will be installed automatically when user triggers the installation, dependencies can also be installed manually

The C program is compiled on amd64 Intel x86 architecture, and I am not sure about the backward compability, so if .exd doesn't work compile it using GCC or any other suitable C Compiler.</p>

<h4> Usage <h4>

<p>Connect both laptop and phone to a common access point, Transmission can take place faster if you use your own phone's hotspot.

Run Mark_2.exe, Follow the instructions, if something fishy happens run the installer. Now the application should start.

Now the application will create a server for data transfer, you don't have to worry about the URL, A QR code will be generated with name host.png, scan it in your phone to get the URL, Any QR code scanner is sufficient. Open the link in your phone's browser, UC browser works most efficiently for file uploads.

Once you visit the generated URL, a file upload interface will be displayed, it can be used to uploadnatimages as well a file with any size

The rate of transmission is around 10MB/s, the speed will be max. if you use your ows network.

The recieved file will be in server-http\media folder.</p>

<h3> By Narasimha Prasanna HN, BE CSE </h3>

<p>Contact me @ narasimhaprasannahn@gmail.com, 9611818690<p>

<p>Thanks!! Happy coding</p>
