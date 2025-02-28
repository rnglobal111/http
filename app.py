from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def log_requests():
    log = f"🔹 {request.remote_addr} - {request.method} - {request.headers.get('User-Agent')}"
    print(log)  # Mostra os logs no terminal da VPS
    return "✅ Servidor ativo! Acesse os logs na saída padrão.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
