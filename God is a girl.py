import subprocess
import time
import getpass
import os

USER_NAME: str = getpass.getuser()
file_path = os.path.dirname(os.path.realpath(__file__))
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
with open(bat_path + '\\' + "GodRight", "w+") as bat_file:
    bat_file.write(r'start "" "%s"' % file_path)

while True:
    if 22 <= int(time.strftime('%H')):  # %d:Hour
        subprocess.run(["shutdown", "-s", "-t", '0'])
        exit()
    elif time.strftime('%a') not in ['Mon', 'Sun']:  # %a:Week name(short for 3 word)
        subprocess.run(["shutdown", "-s", "-t", '0'])
        exit()
    time.sleep(10)
