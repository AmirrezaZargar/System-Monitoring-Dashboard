from flask import Flask, render_template
import psutil
import datetime
import random

app = Flask(__name__)
COLORS = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33A8"]

@app.route('/')
def index():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color = random.choice(COLORS)
    return render_template('index.html', cpu=cpu, ram=ram, time=time, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
