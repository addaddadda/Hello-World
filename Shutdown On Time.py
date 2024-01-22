import subprocess
import time
import getpass
import os
from win11toast import toast

toast('Hello Python', duration='long')

USER_NAME: str = getpass.getuser()


def startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "ShutdownCodeByCYH.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)


def shutdown(shutdown_time=-1):
    if shutdown_time == -1:
        subprocess.run(["shutdown", "-s"])
    else:
        subprocess.run(["shutdown", "-s", "-t", str(time)])


def kill_process(process_name):
    if process_name in os.popen('tasklist').read():
        os.system("taskkill /im " + process_name)
    else:
        print("The process is not running")


def timer(second=7200):
    t = time.time()
    while time.time() - t < second:
        time.sleep(60)


#def notificator(title, message):


def main():
    while True:
        try:
            current_hour = time.localtime().tm_hour
            if current_hour in [13, 23]:
                subprocess.run(["shutdown", "-s"])
                time.sleep(60)
        except Exception as e:
            print(f"An error occurred: {e}")
