from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def db_ok():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "appdb"),
            user=os.getenv("POSTGRES_USER", "appuser"),
            password=os.getenv("POSTGRES_PASSWORD", "secret"),
            host=os.getenv("POSTGRES_HOST", "db"),
            port=5432
        )
        conn.close()
        return True
    except Exception:
        return False

@app.route("/")
def home():
    return "<h1>App Web com Docker 🚀</h1>"

@app.route("/health")
def health():
    return {"status": "ok", "db": db_ok()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)