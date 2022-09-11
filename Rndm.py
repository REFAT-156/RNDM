import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from rndm64 import Main
 
        Main()
 
 
 
elif bit == "32bit":
 
        from rndm32 import Main
 
 
        Main()
 
 
