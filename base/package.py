import pip as PYTHON_PACKAGES
import socket

#GLOBAL FOR package.py
DEP_ARRY=["qrcode", "django", "pillow"]
#defines a test DNS address, say "www.google.com"
GLOBAL_TEST_URL="www.google.com"
#default HTTP port
PORT_DEF=80
#Timeout variable for connection, set maximum value in case of lower connections
MAX_TIMEOUT=100

#function to create a new socket
def create_socket(GLOBAL_TEST_URLI):
    host=socket.gethostbyname(GLOBAL_TEST_URLI)
    return host

#function to check Internet connectivity
def isInternetAvailable(host_name):
    return socket.create_connection([host_name, PORT_DEF], MAX_TIMEOUT)
    
def package_downloader():
    if isInternetAvailable(create_socket(GLOBAL_TEST_URL)):
        for dependencies in DEP_ARRY:
            PYTHON_PACKAGES.main(['install', dependencies])
            return True
    else:
        print("Internet connection is required for the first time.")
        return False
    pass

def get_MyIP():
    return socket.gethostbyname(socket.gethostname())