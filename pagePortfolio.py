import cherrypy


class PaginaPortfolio():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        # Os portfólios pessoais são sub-sites auto-contidos (CSS e imagens próprias)
        # servidos como arquivos estáticos a partir de /portfolios/...
        html += '''
            <section class="portfolio">
                <h1>Portfólios do Grupo</h1>
                <p>Escolha um integrante para visualizar seu portfólio</p>

                <div class="portfolio-cards">
                    <div class="portfolio-card">
                        <div class="avatar">C</div>
                        <h3>Camila</h3>
                        <a href="/portfolios/camila/site.html">Acessar</a>
                    </div>

                    <div class="portfolio-card">
                        <div class="avatar">E</div>
                        <h3>Eduardo</h3>
                        <a href="/portfolios/eduardo/index.html">Acessar</a>
                    </div>

                    <div class="portfolio-card">
                        <div class="avatar">C</div>
                        <h3>Cinthia</h3>
                        <a href="/portfolios/cinthia.html">Acessar</a>
                    </div>

                    <div class="portfolio-card">
                        <div class="avatar">Y</div>
                        <h3>Yago</h3>
                        <a href="/portfolios/yago.html">Acessar</a>
                    </div>

                    <div class="portfolio-card">
                        <div class="avatar">M</div>
                        <h3>Matheus</h3>
                        <a href="/portfolios/matheus/Index.html">Acessar</a>
                    </div>
                </div>
            </section>
        '''
        html += self.rodape
        return html
