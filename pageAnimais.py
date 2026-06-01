import cherrypy


class PaginaAnimais():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        # Form de filtro mantido como elemento visual da Etapa 1 (sem ação).
        html += '''
            <section class="banner" style="height: 300px;">
                <h1>Encontre seu novo melhor amigo</h1>
                <p>Veja os animais disponíveis para adoção</p>
            </section>

            <section>
                <h2>Filtrar animais</h2>
                <form class="filtro-form">
                    <input type="text" placeholder="Nome do animal">
                    <input type="text" placeholder="Espécie (Cachorro/Gato)">
                    <input type="text" placeholder="Idade">
                    <button type="button">Buscar</button>
                </form>
            </section>

            <section>
                <h2>Animais disponíveis</h2>

                <div class="cards">
                    <div class="card">
                        <img src="/imagens/rex.jpg" alt="Rex">
                        <h3>Rex</h3>
                        <p>Cachorro • 2 anos</p>
                        <p>Brincalhão e cheio de energia</p>
                        <a href="/rotaDetalhesRex">Ver detalhes</a>
                    </div>

                    <div class="card">
                        <img src="/imagens/luna.jpg" alt="Luna">
                        <h3>Luna</h3>
                        <p>Cachorra • 1 ano</p>
                        <p>Carinhosa e tranquila</p>
                        <a href="/rotaDetalhesLuna">Ver detalhes</a>
                    </div>

                    <div class="card">
                        <img src="/imagens/thor.jpg" alt="Thor">
                        <h3>Thor</h3>
                        <p>Cachorro • 3 anos</p>
                        <p>Leal e protetor</p>
                        <a href="/rotaDetalhesThor">Ver detalhes</a>
                    </div>

                    <div class="card">
                        <img src="/imagens/mia.jpg" alt="Mia">
                        <h3>Mia</h3>
                        <p>Gata • 6 meses</p>
                        <p>Curiosa e brincalhona</p>
                        <a href="/rotaDetalhesMia">Ver detalhes</a>
                    </div>
                </div>
            </section>

            <section style="text-align:center; padding: 60px 20px;">
                <h2 style="margin-bottom: 15px;">Quer ajudar mais?</h2>
                <p style="margin-bottom: 25px; font-size: 18px; color: #555;">
                    Você também pode apoiar resgates ou divulgar animais.
                </p>
                <a href="/rotaResgates" class="btn" style="display:inline-block;">
                    Registrar um resgate
                </a>
            </section>
        '''
        html += self.rodape
        return html
