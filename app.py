from flask import Flask

app = Flask(__name__)

PAGINA_INICIAL = """
<h1>Instruções</h1>
<p>API simples de saudação.</p>
<ul>
  <li><code>GET /</code> — esta página de instruções</li>
  <li><code>GET /&lt;nome&gt;</code> — retorna <code>{"mensagem": "Olá, [NOME]. Como vai?"}</code></li>
</ul>
<p>Exemplo: <code>/Maria</code> → <code>{"mensagem": "Olá, Maria. Como vai?"}</code></p>
"""

@app.get("/")
def index():
    return PAGINA_INICIAL

@app.get("/<nome>")
def ola_nome(nome):
    return {"mensagem": f"Olá, {nome}. Como vai?"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
