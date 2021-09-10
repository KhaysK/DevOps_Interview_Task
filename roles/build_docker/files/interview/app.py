from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def index():
    mskTimeZone = pytz.timezone("Europe/Moscow")
    mskDataTime = datetime.now(mskTimeZone)
    return "Hello World! Time is: " + mskDataTime.strftime("%I:%M %p")


if __name__ == "__main__":
    app.run()
