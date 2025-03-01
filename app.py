from flask import Flask, request

app = Flask(__name__)

# Página principal
@app.route("/", methods=["GET", "POST"])
def index():
    log = f"🔹 IP: {request.remote_addr} - Método: {request.method} - User-Agent: {request.headers.get('User-Agent')}"
    
    # Salva os logs em um arquivo local
    with open("logs.txt", "a") as file:
        file.write(log + "\n")
    
    print(log)  # Exibe no terminal da VPS
    return "✅ Servidor rodando! Os logs estão sendo salvos.", 200

# Página para visualizar os logs remotamente
@app.route("/logs", methods=["GET"])
def show_logs():
    with open("logs.txt", "r") as file:
        return "<pre>" + file.read() + "</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
