from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get("Body")  # Pega a mensagem do usuário
    response = MessagingResponse()

    if msg.lower().startswith("buscar "):
        pesquisa = msg[7:]
        response.message(f"Buscando: {pesquisa}")
        # Aqui você pode adicionar uma busca no YouTube ou outras fontes

    else:
        response.message("Comando não reconhecido. Use: 'Buscar [nome da música]'")

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
