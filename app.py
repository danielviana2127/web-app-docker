import os
from flask import Flask, jsonify
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

DB_CONFIG = {
    "dbname": os.getenv("POSTGRES_DB", "appdb"),
    "user": os.getenv("POSTGRES_USER", "appuser"),
    "password": os.getenv("POSTGRES_PASSWORD", "secret"),
    "host": os.getenv("POSTGRES_HOST", "db"),
    "port": int(os.getenv("POSTGRES_PORT", 5432)),
}


def check_database() -> bool:
    """Verifica conectividade com o banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG, connect_timeout=3)
        conn.close()
        return True
    except OperationalError:
        return False


@app.route("/", methods=["GET"])
def home():
    """Endpoint raiz da aplicação."""
    return "<h1>App Web com Docker 🚀</h1>", 200


@app.route("/health", methods=["GET"])
def health():
    """Healthcheck da aplicação e do banco de dados."""
    return jsonify({
        "status": "ok",
        "database": "up" if check_database() else "down"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("APP_PORT", 8000)),
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true"
    )