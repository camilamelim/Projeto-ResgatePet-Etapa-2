import cherrypy


class PaginaFaq():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''
            <section class="faq">
                <h1>Perguntas Frequentes</h1>

                <div class="faq-container">
                    <div class="faq-item">
                        <h3>Como funciona a plataforma?</h3>
                        <p>Conectamos animais resgatados a pessoas interessadas em adoção,
                           além de organizar informações sobre resgates, vacinação e cuidados.</p>
                    </div>

                    <div class="faq-item">
                        <h3>O uso da plataforma é gratuito?</h3>
                        <p>Sim! O acesso é totalmente gratuito tanto para adotantes quanto para protetores.</p>
                    </div>

                    <div class="faq-item">
                        <h3>Como posso adotar um animal?</h3>
                        <p>Basta acessar a seção de animais disponíveis, escolher um pet e preencher o formulário de adoção.</p>
                    </div>

                    <div class="faq-item">
                        <h3>O site garante o anonimato?</h3>
                        <p>Seus dados são protegidos e utilizados apenas para fins relacionados ao processo de adoção.</p>
                    </div>

                    <div class="faq-item">
                        <h3>Posso ajudar sem adotar?</h3>
                        <p>Sim! Você pode contribuir com doações, voluntariado ou divulgando os animais nas redes sociais.</p>
                    </div>
                </div>
            </section>
        '''
        html += self.rodape
        return html
