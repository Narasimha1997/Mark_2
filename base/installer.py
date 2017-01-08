import os, platform
from base import package
import zipfile

#This module is used during installation of dependencies and for configuration.. please do not delete this

#GLOBALS
#installation file
INSTALLATION_FLAG_FILE="installer_data.txt"
INSTALLER_DEP=False
INSTALLER_CONF=False

def line_by_line():
    file__=open(INSTALLATION_FLAG_FILE, "r")
    data=int(file__.read())
    return data



def file_write(data, f_name):
    file_f=open(f_name, "w")
    file_f.write(str(data))
    file_f.close()

def configuration_manager():
    file=zipfile.ZipFile("server-http.zip", "r")
    file.extractall()
    pass

def rectify_errors_install():
    installer_flag=line_by_line()
    if installer_flag==0:
        if package.package_downloader():
            configuration_manager()
            file_write(4, INSTALLATION_FLAG_FILE)
        else:
            file_write(0, INSTALLATION_FLAG_FILE)
            print("some error occured during installation, check internet connectivity")
    if installer_flag==1:
        configuration_manager()
        file_write(4,INSTALLATION_FLAG_FILE)
    if installer_flag==2:
        if package.package_downloader():
            file_write(4, INSTALLATION_FLAG_FILE)
        else:
            file_write(0, INSTALLATION_FLAG_FILE)
            print("some error occured during installation, check internet connectivity")
    if installer_flag==4:
        print("Everything is fine , no need to run the installer")

if __name__=="__main__":
    rectify_errors_install()
    

    


    
