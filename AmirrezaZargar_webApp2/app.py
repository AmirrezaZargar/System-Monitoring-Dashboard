from flask import Flask, render_template
import psutil
import platform
from datetime import datetime, timedelta
import random

app = Flask(__name__)

THEMES = [
    {"bg": "linear-gradient(135deg, #0f0c29, #302b63, #24243e)", "accent": "#a78bfa"},
    {"bg": "linear-gradient(135deg, #1a1a2e, #16213e, #0f3460)",  "accent": "#60a5fa"},
    {"bg": "linear-gradient(135deg, #0d1117, #161b22, #1f2937)",  "accent": "#34d399"},
    {"bg": "linear-gradient(135deg, #1a0533, #2d1b69, #11998e)",  "accent": "#f472b6"},
    {"bg": "linear-gradient(135deg, #0f2027, #203a43, #2c5364)",  "accent": "#fbbf24"},
    {"bg": "linear-gradient(135deg, #200122, #6f0000, #200122)",  "accent": "#fb923c"},
]

def get_uptime():
    
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{hours}h {minutes}m"

def get_network():
   
    net = psutil.net_io_counters()
    
    sent_mb = round(net.bytes_sent / 1024 / 1024, 1)
    recv_mb = round(net.bytes_recv / 1024 / 1024, 1)
    return {"sent": sent_mb, "recv": recv_mb}

def get_top_processes():
    
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
   
    top = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    return top

@app.route("/")
def index():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    data = {
        "theme": random.choice(THEMES),
        "time": datetime.now().strftime("%H:%M:%S"),
        "date": datetime.now().strftime("%Y-%m-%d"),

        # CPU
        "cpu": cpu,
        "cpu_cores": psutil.cpu_count(),

        # RAM
        "ram_percent": ram.percent,
        "ram_used": round(ram.used / 1024**3, 1),   # GB
        "ram_total": round(ram.total / 1024**3, 1),  # GB

        # Disk
        "disk_percent": disk.percent,
        "disk_used": round(disk.used / 1024**3, 1),
        "disk_total": round(disk.total / 1024**3, 1),

        
        "hostname": platform.node(),
        "os": f"{platform.system()} {platform.release()}",
        "uptime": get_uptime(),
        "python_ver": platform.python_version(),

       
        "network": get_network(),
        "top_procs": get_top_processes(),
    }
    return render_template("index.html", **data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
