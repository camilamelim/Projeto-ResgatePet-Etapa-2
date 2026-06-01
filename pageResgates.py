import cherrypy


class PaginaResgates():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        # Form e tabela mantidos como conteúdo visual da Etapa 1.
        # CRUD persistente é exigido apenas para a tabela "adocao".
        html += '''
            <section class="banner" style="height: 300px;">
                <h1>Registro de Resgates</h1>
                <p>Ajude a documentar e organizar os resgates realizados</p>
            </section>

            <section>
                <h2>Registrar novo resgate</h2>
                <form class="filtro-form">
                    <label>Local do resgate</label>
                    <input type="text" placeholder="Ex: Rua X, Bairro Y">

                    <label>Data do resgate</label>
                    <input type="date">

                    <label>Responsável</label>
                    <input type="text" placeholder="Nome do protetor">

                    <label>Descrição</label>
                    <input type="text" placeholder="Ex: Animal ferido, abandonado, etc.">

                    <button type="button">Registrar resgate</button>
                </form>
            </section>

            <section>
                <h2>Resgates recentes</h2>
                <table>
                    <tr>
                        <th>Data</th>
                        <th>Local</th>
                        <th>Responsável</th>
                        <th>Status</th>
                    </tr>
                    <tr>
                        <td>10/03/2026</td>
                        <td>Centro</td>
                        <td>Maria</td>
                        <td>Concluído</td>
                    </tr>
                    <tr>
                        <td>12/03/2026</td>
                        <td>Zona Norte</td>
                        <td>João</td>
                        <td>Em andamento</td>
                    </tr>
                </table>
            </section>

            <section class="cta-section">
                <h2>Quer ajudar ainda mais?</h2>
                <p>Divulgue animais resgatados e aumente as chances de adoção.</p>
                <a href="/rotaAnimais" class="btn">Ver animais disponíveis</a>
            </section>
        '''
        html += self.rodape
        return html
