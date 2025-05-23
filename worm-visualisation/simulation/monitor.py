import time
import os


LOG_DIR = "/vagrant/logs/"
FILES = ["code_red.log", "voyager.log"]


def follow(filename):
    with open(filename, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line:
                print(f"[{filename}] {line.strip()}")
            else:
                time.sleep(0.5)


if __name__ == "__main__":
    for file in FILES:
        path = os.path.join(LOG_DIR, file)
        if os.path.exists(path):
            print(f"Monitoring: {file}")
        else:
            print(f"File {file} not found. Waiting...")

    try:
        while True:
            for file in FILES:
                path = os.path.join(LOG_DIR, file)
                if os.path.exists(path):
                    follow(path)
    except KeyboardInterrupt:
        print("Stopped monitoring.")
