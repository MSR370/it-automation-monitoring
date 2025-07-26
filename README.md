# it-automation-monitoring
# 🛠️ System Automation with Python

This project automates common system monitoring tasks using Python scripts. It includes CPU, memory, disk, and network monitoring, as well as process checks and log storage – all organized for easy use and extensibility.

## 📁 Project Structure

it_automation_dash_monitoring/
├── logs/
│ └── ...log files stored with timestamps
├── scripts/
│ ├── cpu_memory_monitor.py
│ ├── process_monitor.py
│ ├── disk_network_monitor.py
│ └── backup_script.py (optional)
├── README.md
└── requirements.txt

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Mac%20%7C%20Linux-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Progress-Week%201%20Complete-brightgreen)

## 🚀 Features

- ✅ Monitor **CPU and Memory** usage
- ✅ Track **disk space** and **network I/O**
- ✅ Check for running processes (like `python`, `chrome`, etc.)
- ✅ Save logs into a `logs/` directory with timestamps
- ✅ Scripts can be run manually or scheduled via **cron**
- ✅ Easily extendable to monitor services like `nginx`, `mysql`, etc.

## 📌 Technologies Used

- Python 3
- [`psutil`](https://pypi.org/project/psutil/)
- `datetime`, `os`, `subprocess`
- Linux/Mac terminal (for `cron` jobs)

## 🖥️ Sample Commands

```bash
# Run a script
python3 scripts/cpu_memory_monitor.py

# Add to crontab (runs every 5 minutes)
*/5 * * * * /usr/bin/python3 /path/to/disk_network_monitor.py
```
## Log Examples
2025-07-24 15:00:00 - CPU Usage: 12.5% - Memory Usage: 45.1%
2025-07-24 15:05:00 - python is running
2025-07-24 15:10:00 - Disk Usage: 83% - 90GB used, 10GB free


## 💡 Next Steps
 ✅ Add a Flask web dashboard (Week 2)

 🚨 Add alerting via email or Telegram bot (Week 3)

 ☁️ Upload logs to AWS S3 (Week 3)

 🚀 Deploy Flask dashboard (Week 4)

