from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def log_requests():
    log = f"🔹 IP: {request.remote_addr} - Método: {request.method} - User-Agent: {request.headers.get('User-Agent')}"
    with open("logs.txt", "a") as file:
        file.write(log + "\n")
    return "✅ Servidor ativo! Logs estão sendo salvos.", 200

@app.route("/logs", methods=["GET"])
def show_logs():
    with open("logs.txt", "r") as file:
        return "<pre>" + file.read() + "</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
