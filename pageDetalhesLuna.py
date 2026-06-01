import cherrypy


class PaginaDetalhesLuna():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''
            <section class="animal-detalhe">
                <h1>Luna</h1>

                <div class="animal-container">
                    <div class="animal-img">
                        <img src="/imagens/luna.jpg" alt="Luna">
                    </div>

                    <div class="animal-info">
                        <h2>Informações</h2>
                        <table>
                            <tr><td><strong>Idade</strong></td><td>1 ano</td></tr>
                            <tr><td><strong>Sexo</strong></td><td>Fêmea</td></tr>
                            <tr><td><strong>Saúde</strong></td><td>Vacinada</td></tr>
                            <tr><td><strong>Porte</strong></td><td>Médio</td></tr>
                        </table>
                        <a href="/rotaAdocao" class="btn-adotar">Quero adotar</a>
                    </div>
                </div>

                <div class="descricao">
                    <h2>Sobre a Luna</h2>
                    <p>
                        Luna foi resgatada das ruas e hoje está saudável e pronta para encontrar um novo lar.<br>
                        É muito dócil, carinhosa e se dá bem com pessoas e outros animais.
                    </p>
                </div>
            </section>
        '''
        html += self.rodape
        return html
