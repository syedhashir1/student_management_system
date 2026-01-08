from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    # Academic tip: Returning a JSON status is great for health checks
    return jsonify({"status": "ok", "message": "Student Management System is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
