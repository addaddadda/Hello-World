import subprocess
import time

if __name__ == '__main__':
    while True:
        if time.localtime().tm_hour == 13:
            subprocess.run(["shutdown", "-s"])
