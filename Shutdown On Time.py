import subprocess
import time
import getpass
import os
USER_NAME: str = getpass.getuser()


def startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "ShutdownCodeByCYH.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)


if __name__ == '__main__':
    startup()
    while True:
        try:
            current_hour = time.localtime().tm_hour
            if current_hour in [13, 23]:
                subprocess.run(["shutdown", "-s"])
                time.sleep(60)
        except Exception as e:
            print(f"An error occurred: {e}")
