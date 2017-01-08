import os, zipfile
from base import installer,package, qr_code
from subprocess import call
#String to contain IP address:
HOST_IP="0.0.0" #default value, points nowhere
#Default port can be changed , modify this:
PORT_POSIX_DEFAULT='8000'
found=0
#function to get host ip: found on package in base module
#default QR_Image path:
QR_PATH='Image.png'
#Contains list of allowed hosts
ALL_HOSTS=[]
#Main Array which contains all hosts:
ALLOWED_HOSTS_IP=[]

def file_data_fetch():
    
    data_file=open('installer_data.txt', "r")

    return int(data_file.read())

def file_test(char_fname):
    for list in os.listdir():
        if char_fname is list:
            return True

def run_diagnostics():
    if file_test("server-http"):
        found=1
    else:
        installer.file_write('1', installer.INSTALLATION_FLAG_FILE)
        installer.rectify_errors_install()
        found=1
    if file_test("base"):
        found=1
    else:
        zipf=zipfile.ZipFile("core//base.zip","r")
        zipf.extractall()
        found=1

def generate_host_string():
    return package.get_MyIP()+":"+PORT_POSIX_DEFAULT

def add_allowed_hosts(ip_str):
    f=open("allowed_hosts.txt", "a+")
    f.write(ip_str)
    f.close()
    pass

if __name__=="__main__":
    os.remove("allowed_hosts.txt")
    file__=open("allowed_hosts.txt","w")
    file__.close()
    run_diagnostics()
    if found==0:
        qr_code.gen_qrcodes(generate_host_string())
        MY_IP=package.get_MyIP()
        found_append=0
        file_hosts=open('allowed_hosts.txt','r')
        for ip in file_hosts.readlines():
            ALL_HOSTS.append(ip)
        for hosts in ALL_HOSTS:
            if MY_IP is hosts:
                found_append=1
                break
        if found_append==0:
            add_allowed_hosts(MY_IP)
        ALL_HOSTS=ALL_HOSTS
        
        call(["python","server-http//Main.py"])
        print("server running at "+generate_host_string())
    else:
        print("Error installing")
        



