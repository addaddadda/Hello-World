import subprocess
import time
import getpass
import os
from plyer import notification

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


def find_and_kill_process(process_name):
    if process_name in os.popen('tasklist').read():
        notification.notify("Find mc running now", "Close mc 20 minutes later")
        time.sleep(20*60)
        os.system("taskkill /im " + process_name)
    else:
        time.sleep(5)
        print("Can't find mc running now")


def timer(second=7200):
    t = time.time()
    while time.time() - t < second:
        time.sleep(60)


# def notificator(title, message):


def main():
    while True:
        try:
            current_hour = time.localtime().tm_hour
            if current_hour in [13, 23]:
                subprocess.run(["shutdown", "-s"])
                time.sleep(60)
        except Exception as e:
            print(f"An error occurred: {e}")


def notifier(title, message="""It's been 20 minutes
Take a break
Take care of your eyes
            """):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\Users\Chen Xiaoheng\test\test\minecraft.ico",
        timeout=10
    )


if __name__ == "__main__":
    notifier("MC Shutdown On", "It is running and may add it to the startup folder to run automatically")
    startup()
    while True:
        find_and_kill_process("Minecraft")



