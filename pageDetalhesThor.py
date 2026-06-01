import cherrypy


class PaginaDetalhesThor():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''
            <section class="animal-detalhe">
                <h1>Thor</h1>

                <div class="animal-container">
                    <div class="animal-img">
                        <img src="/imagens/thor.jpg" alt="Thor">
                    </div>

                    <div class="animal-info">
                        <h2>Informações</h2>
                        <table>
                            <tr><td><strong>Idade</strong></td><td>3 anos</td></tr>
                            <tr><td><strong>Sexo</strong></td><td>Macho</td></tr>
                            <tr><td><strong>Saúde</strong></td><td>Vacinado</td></tr>
                            <tr><td><strong>Porte</strong></td><td>Médio</td></tr>
                        </table>
                        <a href="/rotaAdocao" class="btn-adotar">Quero adotar</a>
                    </div>
                </div>

                <div class="descricao">
                    <h2>Sobre o Thor</h2>
                    <p>
                        Thor é um cachorro muito amigável e leal. Ele adora estar perto das pessoas e é ótimo com crianças. <br>
                        Ele foi resgatado de uma situação de abandono, mas agora está saudável e pronto para encontrar um novo lar onde possa receber todo o amor e cuidado que merece.
                    </p>
                </div>
            </section>
        '''
        html += self.rodape
        return html
