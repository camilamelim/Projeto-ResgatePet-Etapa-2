import cherrypy
import os
import socket

from pageInicio        import PaginaInicio
from pageAnimais       import PaginaAnimais
from pageDetalhesRex   import PaginaDetalhesRex
from pageDetalhesLuna  import PaginaDetalhesLuna
from pageDetalhesThor  import PaginaDetalhesThor
from pageDetalhesMia   import PaginaDetalhesMia
from pageResgates      import PaginaResgates
from pageVacinacao     import PaginaVacinacao
from pageAdocao        import PaginaAdocao
from pageBlog          import PaginaBlog
from pageFaq           import PaginaFaq
from pagePortfolio     import PaginaPortfolio

local_dir = os.path.dirname(os.path.abspath(__file__))

# ──────────────────────────────────────────────
# Verifica qual porta está disponível
# Tenta 8080 primeiro; se estiver ocupada, usa 8081, 8082 …
# ──────────────────────────────────────────────
def porta_livre(inicio=8080, fim=8090):
    for porta in range(inicio, fim):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', porta))
                return porta
            except OSError:
                continue
    raise RuntimeError(f"Nenhuma porta livre encontrada entre {inicio} e {fim}")

PORTA = porta_livre()

# ──────────────────────────────────────────────
# Monta a árvore de rotas
# ──────────────────────────────────────────────
# A página inicial é uma instância de PaginaInicio (rota "/")
root = PaginaInicio()

# Demais módulos montados como atributos do root (rotas)
root.rotaAnimais       = PaginaAnimais()
root.rotaDetalhesRex   = PaginaDetalhesRex()
root.rotaDetalhesLuna  = PaginaDetalhesLuna()
root.rotaDetalhesThor  = PaginaDetalhesThor()
root.rotaDetalhesMia   = PaginaDetalhesMia()
root.rotaResgates      = PaginaResgates()
root.rotaVacinacao     = PaginaVacinacao()
root.rotaAdocao        = PaginaAdocao()
root.rotaBlog          = PaginaBlog()
root.rotaFaq           = PaginaFaq()
root.rotaPortfolio     = PaginaPortfolio()

# ──────────────────────────────────────────────
# Configuração do servidor
# ──────────────────────────────────────────────
server_config = {
    'server.socket_host': '127.0.0.1',
    'server.socket_port': PORTA,
}
cherrypy.config.update(server_config)

# Libera o diretório do projeto para servir os arquivos estáticos
# (/css, /html, /imagens, /portfolios) automaticamente.
local_config = {
    "/": {
        "tools.staticdir.on": True,
        "tools.staticdir.dir": local_dir,
    },
}

print(f"\n✔ Servidor iniciando em: http://127.0.0.1:{PORTA}/\n")
cherrypy.quickstart(root, config=local_config)
