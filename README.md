# 🛠️ it-automation-monitoring

This project automates common system monitoring tasks using Python and Bash. It tracks CPU, memory, disk, network, and process info, and saves logs with timestamps. The scripts are modular, extensible, and can be scheduled with cron. A Flask dashboard and alert system are coming soon.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Mac%20%7C%20Linux-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Progress-Week%201%20Complete-brightgreen)

---

## 📚 Table of Contents
- [Project Structure](#project-structure)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Sample Commands](#️-sample-commands)
- [Log Examples](#log-examples)
- [Web Dashboard (Coming Soon)](#-web-dashboard-coming-soon)
- [Progress Roadmap](#-progress-roadmap)

---

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

## 🔄 Progress Roadmap

 | Week | Task                               | Status         |
| ---- | ---------------------------------- | -------------- |
| 1️⃣  | Bash/Python monitoring + logging   | ✅ Complete     |
| 2️⃣  | Flask web dashboard (HTML + Flask) | 🚧 In Progress |
| 3️⃣  | Alerts (email/Telegram) + AWS S3   | ⏳ Upcoming     |
| 4️⃣  | Deployment + documentation polish  | 🔜 Upcoming    |


## ✅ Author
MSR370

MIT License © 2025

