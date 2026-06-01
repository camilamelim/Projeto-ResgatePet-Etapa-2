import cherrypy


class PaginaVacinacao():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''
            <section class="banner" style="height: 300px;">
                <h1>Controle de Vacinação</h1>
                <p>Acompanhe a saúde dos animais resgatados</p>
            </section>

            <section>
                <h2>Histórico de Vacinação</h2>
                <table>
                    <tr>
                        <th>Animal</th>
                        <th>Vacina</th>
                        <th>Data</th>
                        <th>Status</th>
                    </tr>
                    <tr>
                        <td>Rex</td>
                        <td>Antirrábica</td>
                        <td>10/03/2026</td>
                        <td>Em dia</td>
                    </tr>
                    <tr>
                        <td>Luna</td>
                        <td>V4 (Gatos)</td>
                        <td>05/03/2026</td>
                        <td>Em dia</td>
                    </tr>
                    <tr>
                        <td>Thor</td>
                        <td>V8</td>
                        <td>01/02/2026</td>
                        <td>Atrasada</td>
                    </tr>
                </table>
            </section>

            <section>
                <h2>Registrar vacinação</h2>
                <form class="filtro-form">
                    <label>Nome do animal</label>
                    <input type="text" placeholder="Ex: Rex">

                    <label>Vacina aplicada</label>
                    <input type="text" placeholder="Ex: Antirrábica">

                    <label>Data</label>
                    <input type="date">

                    <button type="button">Registrar vacina</button>
                </form>
            </section>

            <section class="cta-section">
                <h2>Cuidar também é amar</h2>
                <p>Animais saudáveis têm mais chances de encontrar um lar.</p>
                <a href="/rotaAnimais" class="btn">Ver animais disponíveis</a>
            </section>
        '''
        html += self.rodape
        return html
