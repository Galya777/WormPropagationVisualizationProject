import os
import time
import threading
import argparse
from datetime import datetime
from colorama import init, Fore, Style

# Инициализация на цветовете за терминала
init(autoreset=True)

def follow_log(filepath, worm_name):

    try:
        with open(filepath, "r") as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    color = Fore.RED if worm_name.lower() == "code_red" else Fore.MAGENTA
                    print(f"{color}[{now}] [{worm_name.upper()}] {line.strip()}")
                else:
                    time.sleep(0.5)
    except FileNotFoundError:
        print(Fore.YELLOW + f"[WARN] File not found: {filepath}")
    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to read {filepath}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Worm infection log monitor")
    parser.add_argument("--log-dir", default="/home/galya777/PycharmProjects/WormPropagationVisualizationProject/worm-visualisation/vagrant/logs/", help="Directory with log files")
    parser.add_argument("--files", nargs="+", default=["code_red.log", "voyager.log"], help="Log files to monitor")
    args = parser.parse_args()

    log_dir = args.log_dir
    log_files = args.files

    threads = []
    for file in log_files:
        full_path = os.path.join(log_dir, file)
        worm_name = os.path.splitext(file)[0]  # Пример: code_red.log → code_red
        t = threading.Thread(target=follow_log, args=(full_path, worm_name))
        t.daemon = True
        t.start()
        threads.append(t)
        print(Fore.GREEN + f"Started monitoring {file} as {worm_name}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nMonitoring stopped by user.")

if __name__ == "__main__":
    main()
