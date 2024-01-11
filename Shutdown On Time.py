import subprocess
import time

if __name__ == '__main__':
    if time.localtime().tm_hour == 13:
        subprocess.run(["shutdown", "-p"])
