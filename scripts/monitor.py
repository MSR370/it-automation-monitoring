import psutil
import datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
logs_dir = os.path.join(script_dir, "..", "logs")
os.makedirs(logs_dir, exist_ok=True)
#today's date and time for the log filename
log_filename = os.path.join(logs_dir, datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Get cpu usage percentage
cpu = psutil.cpu_percent(interval=1)
# Get memory usage
memory = psutil.virtual_memory().percent

#Format the log entry
log_entry = f"{now} - CPU Usage: {cpu}% - Memory Usage: {memory}%"

#Append to a log file

#log_file= "logs/system_logs.txt"
with open(log_filename, "a") as file:
    file.write(log_entry)

# Print the log entry to console
print("Log added to:", log_filename)

