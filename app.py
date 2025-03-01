from flask import Flask, request
import socket

app = Flask(__name__)

# Função para obter o reverso DNS do IP (se disponível)
def get_reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "N/A"

@app.route("/", methods=["GET", "POST"])
def log_requests():
    client_ip = request.remote_addr  # IP do visitante
    client_port = request.environ.get('REMOTE_PORT', 'N/A')  # Porta usada pelo visitante
    user_agent = request.headers.get("User-Agent", "N/A")  # User-Agent
    headers = dict(request.headers)  # Captura todos os headers HTTP
    cookies = request.cookies  # Captura cookies enviados pelo cliente
    body_data = request.get_data(as_text=True) if request.data else "N/A"  # Captura dados do corpo da requisição
    reverse_dns = get_reverse_dns(client_ip)  # Obtém reverso DNS

    # Montando log completo
    log = f"""
    🔹 IP: {client_ip}
    🔹 Reverse DNS: {reverse_dns}
    🔹 Porta de Origem: {client_port}
    🔹 Método HTTP: {request.method}
    🔹 User-Agent: {user_agent}
    🔹 Headers HTTP: {headers}
    🔹 Cookies: {cookies}
    🔹 Corpo da Requisição: {body_data}
    --------------------------
    """

    # Salva os logs em um arquivo local
    with open("logs.txt", "a") as file:
        file.write(log + "\n")

    print(log)  # Exibe no terminal da VPS
    return "✅ Servidor rodando! Logs estão sendo salvos.", 200

# Página para visualizar os logs remotamente
@app.route("/logs", methods=["GET"])
def show_logs():
    with open("logs.txt", "r") as file:
        return "<pre>" + file.read() + "</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

