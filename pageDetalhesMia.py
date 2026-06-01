import cherrypy


class PaginaDetalhesMia():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''
            <section class="animal-detalhe">
                <h1>Mia</h1>

                <div class="animal-container">
                    <div class="animal-img">
                        <img src="/imagens/mia.jpg" alt="Mia">
                    </div>

                    <div class="animal-info">
                        <h2>Informações</h2>
                        <table>
                            <tr><td><strong>Idade</strong></td><td>6 meses</td></tr>
                            <tr><td><strong>Sexo</strong></td><td>Fêmea</td></tr>
                            <tr><td><strong>Saúde</strong></td><td>Em tratamento</td></tr>
                            <tr><td><strong>Porte</strong></td><td>Pequeno</td></tr>
                        </table>
                        <a href="/rotaAdocao" class="btn-adotar">Quero adotar</a>
                    </div>
                </div>

                <div class="descricao">
                    <h2>Sobre a Mia</h2>
                    <p>
                        Mia foi resgatada de um abrigo e está em busca de um lar amoroso. <br>
                        Ela é muito brincalhona e adora a companhia de crianças.
                    </p>
                </div>
            </section>
        '''
        html += self.rodape
        return html
