import psutil
import datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
logs_dir = os.path.join(script_dir, "..", "logs")
os.makedirs(logs_dir, exist_ok=True)
log_file =  os.path.join(logs_dir, "process_logs.txt")

#process names to monitor
process_to_monitor = ["python", "node", "chrome"]

#Get running processes
running_processes = [proc.name().lower() for proc in psutil.process_iter(['name'])]

#time stamp
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Log
with open(log_file, "a") as file:
    file.write(f"Process Monitoring Log - {now}\n")
    for process in process_to_monitor:
        if process in running_processes:
            log_entry = f"{now} - {process} is running\n"
        else:
            log_entry = f"{now} - {process} is not running\n"
        file.write(log_entry)

# Print the log entry to console
print("Process monitoring log updated:", log_file)