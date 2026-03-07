from flask import Flask, render_template
from flask_socketio import SocketIO
import mysql.connector
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return render_template("dashboard.html")


def send_calls():

    last_id = 0

    while True:
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Chanchal@123",
                database="epbx_logs"
            )

            cursor = db.cursor(dictionary=True)

            cursor.execute(
                "SELECT * FROM call_logs WHERE id > %s ORDER BY id ASC",
                (last_id,)
            )

            rows = cursor.fetchall()

            for row in rows:

                # convert date/time objects to string
                row["call_date"] = str(row["call_date"]) if row["call_date"] else ""
                row["call_time"] = str(row["call_time"]) if row["call_time"] else ""
                row["created_at"] = str(row["created_at"]) if row["created_at"] else ""

                print("Sending:", row)

                socketio.emit("call_event", row)

                last_id = row["id"]

            cursor.close()
            db.close()

        except Exception as e:
            print("Error:", e)

        time.sleep(2)


# start background thread
thread = threading.Thread(target=send_calls)
thread.daemon = True
thread.start()


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)