import subprocess
from sys import platform

if __name__ == '__main__':
    if platform.system() == 'Windows':
        subprocess.run(["shutdown", "-p"])