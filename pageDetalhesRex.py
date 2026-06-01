import cherrypy


class PaginaDetalhesRex():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''
            <section class="animal-detalhe">
                <h1>Rex</h1>

                <div class="animal-container">
                    <div class="animal-img">
                        <img src="/imagens/rex.jpg" alt="Rex">
                    </div>

                    <div class="animal-info">
                        <h2>Informações</h2>
                        <table>
                            <tr><td><strong>Idade</strong></td><td>2 anos</td></tr>
                            <tr><td><strong>Sexo</strong></td><td>Macho</td></tr>
                            <tr><td><strong>Saúde</strong></td><td>Vacinado</td></tr>
                            <tr><td><strong>Porte</strong></td><td>Médio</td></tr>
                        </table>
                        <a href="/rotaAdocao" class="btn-adotar">Quero adotar</a>
                    </div>
                </div>

                <div class="descricao">
                    <h2>Sobre o Rex</h2>
                    <p>
                        Rex é um cachorro muito brincalhão e cheio de energia.<br>
                        Ele adora correr e brincar com outros cães, mas também é muito carinhoso com as pessoas. <br>
                        Ele foi resgatado das ruas e está em busca de um lar amoroso onde possa receber todo o carinho que merece.
                    </p>
                </div>
            </section>
        '''
        html += self.rodape
        return html
