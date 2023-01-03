import os,platform,time
 
bitt=platform.architecture()[0]
 
if bitt=="32bit":
    print('[!] YOUR DEVICE IS 32 BIT');time.sleep(1);print('\n\n[!] YOUR PYTHON VERSION :');time.sleep(1);os.system('[!] python --version')
    time.sleep(2)
    import refat.Main
 
 
elif bitt=="64bit":
    os.system('clear');print('[!] YOUR DEVICE IS 32 BIT');time.sleep(1);print('\n\n[!] YOUR PYTHON VERSION :');time.sleep(1);os.system('[!] python --version')
    time.sleep(2)
    import refat.Main
 
else:
    print('\nUNKNOWN DEVICE')
