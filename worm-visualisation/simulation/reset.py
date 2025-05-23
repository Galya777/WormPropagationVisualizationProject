import os

LOG_DIR = "/vagrant/logs/"
FILES = ["code_red.log", "voyager.log"]

def reset_logs():
    for file in FILES:
        path = os.path.join(LOG_DIR, file)
        if os.path.exists(path):
            os.remove(path)
            print(f"Deleted: {file}")
        else:
            print(f"Not found: {file} (will be recreated)")

        # Създаване на празен файл, за да не крашва monitoring.py
        with open(path, "w") as f:
            pass
        print(f"Recreated empty log: {file}")

if __name__ == "__main__":
    reset_logs()
    print("✔️ Simulation reset complete.")
