import cherrypy


class PaginaBlog():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''
            <section class="banner" style="height: 300px;">
                <h1>Blog &amp; Conteúdos</h1>
                <p>Informação, cuidado e conscientização</p>
            </section>

            <section>
                <h2>Artigos recentes</h2>

                <div class="cards">
                    <div class="card">
                        <img src="https://images.unsplash.com/photo-1518717758536-85ae29035b6d" alt="">
                        <div class="card-content">
                            <h3>Por que adotar um animal?</h3>
                            <p>Adotar salva vidas e combate o abandono.</p>
                            <a href="#">Ler mais</a>
                        </div>
                    </div>

                    <div class="card">
                        <img src="https://images.unsplash.com/photo-1517849845537-4d257902454a" alt="">
                        <div class="card-content">
                            <h3>Cuidados com pets resgatados</h3>
                            <p>Veja como cuidar corretamente de um animal adotado.</p>
                            <a href="#">Ler mais</a>
                        </div>
                    </div>

                    <div class="card">
                        <img src="https://images.unsplash.com/photo-1507146426996-ef05306b995a" alt="">
                        <div class="card-content">
                            <h3>Voluntariado em ONGs</h3>
                            <p>Descubra como ajudar mesmo sem adotar.</p>
                            <a href="#">Ler mais</a>
                        </div>
                    </div>
                </div>
            </section>

            <section class="destaque">
                <h2>Destaque da semana</h2>

                <div class="destaque-box">
                    <h3>Como ajudar ONGs mesmo sem adotar</h3>
                    <p>
                        Nem todo mundo pode adotar, mas todos podem ajudar.
                        Doações, divulgação e voluntariado fazem toda a diferença
                        na vida de animais resgatados.
                    </p>
                    <ul>
                        <li>✔ Doe ração, medicamentos ou dinheiro</li>
                        <li>✔ Compartilhe campanhas nas redes sociais</li>
                        <li>✔ Seja voluntário em ONGs locais</li>
                    </ul>
                    <a href="#" class="btn-destaque">Saiba mais</a>
                </div>
            </section>

            <section class="cta-section">
                <h2>Faça parte dessa causa</h2>
                <p>Compartilhe informações e ajude mais animais a encontrarem um lar.</p>
                <a href="/rotaAnimais" class="btn">Ver animais disponíveis</a>
            </section>
        '''
        html += self.rodape
        return html
