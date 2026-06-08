from flask import Flask, render_template
import psutil
from datetime import datetime
import random
import os

app = Flask(__name__)

def get_background_colors():
    return ["#A5AA1F", "#3662da", "#c40c0c", "#8031F7", "#00fff7"]


@app.route("/")
def home():
    colors = get_background_colors()
    selected_color = random.choice(colors)

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=0.5)
    ram_usage = psutil.virtual_memory().percent

    return render_template(
        "index.html",
        message="Hello World",
        current_datetime=current_datetime,
        cpu_usage=cpu_usage,
        ram_usage=ram_usage,
        background_color=selected_color
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
