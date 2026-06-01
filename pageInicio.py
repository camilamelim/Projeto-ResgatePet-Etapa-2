import cherrypy


class PaginaInicio():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''
            <section class="banner">
                <h1>Transforme uma vida</h1>
                <p>Adote, cuide e ajude animais resgatados a encontrar um lar.</p>
                <a href="/rotaAnimais" class="btn">Ver animais disponíveis</a>
            </section>

            <section>
                <h2>Nossa Missão</h2>
                <p style="text-align:center; max-width:600px; margin:auto;">
                    Ajudamos protetores independentes a organizar informações e
                    conectar animais resgatados a novos lares com amor e responsabilidade.
                </p>
            </section>

            <section>
                <h2>Animais em destaque</h2>

                <div class="cards">
                    <div class="card">
                        <img src="/imagens/rex.jpg" alt="Rex">
                        <h3>Rex</h3>
                        <p>2 anos • Brincalhão</p>
                        <a href="/rotaDetalhesRex">Ver detalhes</a>
                    </div>

                    <div class="card">
                        <img src="/imagens/luna.jpg" alt="Luna">
                        <h3>Luna</h3>
                        <p>1 ano • Carinhosa</p>
                        <a href="/rotaDetalhesLuna">Ver detalhes</a>
                    </div>
                </div>
            </section>
        '''
        html += self.rodape
        return html
