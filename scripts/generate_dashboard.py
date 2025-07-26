import psutil
import datetime
import os

#dashboard directory
dashboard_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dashboard")
os.makedirs(dashboard_dir, exist_ok=True)
#dashboard file
dashboard_file = os.path.join(dashboard_dir, "index.html")

#Collect system information
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent
network_io = psutil.net_io_counters()

cpu_color = "red" if cpu_usage > 80 else "orange" if cpu_usage > 50 else "green"
memory_color = "red" if memory_info > 80 else "orange" if memory_info > 50 else "green"
disk_color = "red" if disk_usage > 90 else "orange" if disk_usage > 70 else "green"
# Prepare HTML content
# HTML Content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>System Dashboard</title>
    <meta http-equiv="refresh" content="10">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; }}
        .container {{ max-width: 600px; margin: 50px auto; background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }}
        h2 {{ text-align: center; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>System Dashboard</h2>
        <p><strong>Last updated:</strong> {now}</p>
        <ul>
            <li><strong>CPU Usage:</strong> <span style="color:{cpu_color}">{cpu_usage}%</span></li>
            <li><strong>Memory Usage:</strong> <span style="color:{memory_color}">{memory_info}%</span></li>
            <li><strong>Disk Usage:</strong> <span style="color:{disk_color}">{disk_usage}%</span></li>
        </ul>

        <canvas id="usageChart" width="400" height="200"></canvas>
    </div>

    <script>
        const ctx = document.getElementById('usageChart').getContext('2d');
        const usageChart = new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: ['CPU', 'Memory', 'Disk'],
                datasets: [{{
                    label: 'Usage %',
                    data: [{cpu_usage}, {memory_info}, {disk_usage}],
                    backgroundColor: ['{cpu_color}', '{memory_color}', '{disk_color}'],
                    borderWidth: 1
                }}]
            }},
            options: {{
                scales: {{
                    y: {{
                        beginAtZero: true,
                        max: 100
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

#Wirte Html
with open(dashboard_file, "w") as file:
    file.write(html_content)

print("Dashboard generated at:", dashboard_file)