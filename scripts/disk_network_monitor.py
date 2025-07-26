import psutil
import datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
logs_dir = os.path.join(script_dir, "..", "logs")
os.makedirs(logs_dir, exist_ok=True)
log_file = os.path.join(logs_dir, "disk_network_logs.txt")

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Get disk usage
disk_usage = psutil.disk_usage('/')
total_disk = disk_usage.total / (1024 ** 3)  # Convert to GB
used_disk = round(disk_usage.used / (1024 ** 3),2)    # Convert to GB
free_disk = disk_usage.free / (1024 ** 3)    # Convert to GB
percent_disk_used = disk_usage.percent

# Get network I/O statistics
network_io = psutil.net_io_counters()
bytes_sent = network_io.bytes_sent / (1024 ** 2)  # Convert to MB
bytes_recv = network_io.bytes_recv / (1024 ** 2)  # Convert to MB

# Format the log entry
log_entry = (
    f"{now} - Disk Usage: {percent_disk_used}% "
    f"{used_disk}GB used, {free_disk}GB free, {total_disk}GB total;\n "
    f"{now} - Network I/O: {bytes_sent}MB sent, {bytes_recv}MB received\n"
)

#Write to the log file
with open(log_file, "a") as file:
    file.write(log_entry)
    if percent_disk_used > 90:
        file.write(f"{now} - Warning: Disk usage is above 90%\n")
# Print the log entry to console
print("Disk and Network monitoring log updated:", log_file)