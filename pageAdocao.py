import cherrypy

from classes.adocao import Adocao


class PaginaAdocao():
    topo   = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html",    encoding='utf-8').read()

    # ── helper: monta uma página de feedback com visual padrão ──────────
    def paginaResposta(self, icone, titulo, mensagem, cor, href, labelBtn):
        return self.topo + '''
            <section class="banner" style="height:260px;">
                <h1>Adoção</h1>
                <p>Gerenciamento de solicitações</p>
            </section>

            <section style="text-align:center; padding:60px 20px;">
                <div style="
                    display:inline-block;
                    background:#fff;
                    border-radius:16px;
                    box-shadow:0 4px 20px rgba(0,0,0,.1);
                    padding:50px 60px;
                    max-width:520px;
                    width:100%%;
                ">
                    <div style="font-size:64px; margin-bottom:16px;">%(icone)s</div>
                    <h2 style="color:%(cor)s; margin-bottom:12px;">%(titulo)s</h2>
                    <p style="color:#555; font-size:17px; margin-bottom:32px;">%(mensagem)s</p>
                    <a href="%(href)s" class="btn">%(labelBtn)s</a>
                </div>
            </section>
        ''' % {'icone': icone, 'titulo': titulo, 'mensagem': mensagem,
               'cor': cor, 'href': href, 'labelBtn': labelBtn} + self.rodape

    # ────────────────────────────────────────────────────────────────────
    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()

    def montaFormulario(self, pId=0, pNome='', pEmail='', pTel='',
                        pAnimal='', pOutros='Não', pMoradia='',
                        pStatus='Em análise'):
        html = self.topo

        html += '''
            <section class="banner" style="height: 300px;">
                <h1>Adote um amigo</h1>
                <p>Dê uma nova chance para um animal resgatado</p>
            </section>
        '''

        titulo = 'Formulário de Adoção' if int(pId) == 0 else 'Alterar Adoção'
        botao  = 'Enviar solicitação'   if int(pId) == 0 else 'Salvar alteração'

        opt_outros_sim = 'selected' if pOutros == 'Sim' else ''
        opt_outros_nao = 'selected' if pOutros == 'Não' else ''

        opcoes_moradia = ['Casa', 'Apartamento', 'Sítio', 'Outro']
        moradia_html = ''
        for m in opcoes_moradia:
            sel = 'selected' if m == pMoradia else ''
            moradia_html += '<option value="%s" %s>%s</option>' % (m, sel, m)

        opcoes_status = ['Em análise', 'Aprovada', 'Concluída', 'Rejeitada']
        status_html = ''
        for s in opcoes_status:
            sel = 'selected' if s == pStatus else ''
            status_html += '<option value="%s" %s>%s</option>' % (s, sel, s)

        html += '''
            <section>
                <h2>%s</h2>

                <form class="filtro-form" name="FormCadastro"
                      action="/rotaAdocao/gravarAdocao" method="post">

                    <input type="hidden" id="txtId" name="txtId" value="%s"/>

                    <label>Nome completo</label>
                    <input type="text" id="txtNome" name="txtNome"
                           value="%s" placeholder="Seu nome completo"
                           maxlength="100" required>

                    <label>Email</label>
                    <input type="email" id="txtEmail" name="txtEmail"
                           value="%s" placeholder="seuemail@email.com"
                           maxlength="100" required>

                    <label>Telefone</label>
                    <input type="text" id="txtTel" name="txtTel"
                           value="%s" placeholder="(00) 00000-0000"
                           maxlength="20" required>

                    <label>Animal de interesse</label>
                    <input type="text" id="txtAnimal" name="txtAnimal"
                           value="%s" placeholder="Ex: Rex"
                           maxlength="50" required>

                    <label>Você possui outros animais?</label>
                    <select id="txtOutros" name="txtOutros" required>
                        <option value="Sim" %s>Sim</option>
                        <option value="Não" %s>Não</option>
                    </select>

                    <label>Tipo de moradia</label>
                    <select id="txtMoradia" name="txtMoradia" required>
                        <option value="">-- selecione --</option>
                        %s
                    </select>

                    <label>Status</label>
                    <select id="txtStatus" name="txtStatus" required>
                        %s
                    </select>

                    <button type="submit" id="btnGravar" name="btnGravar">%s</button>
                </form>
            </section>
        ''' % (titulo, pId, pNome, pEmail, pTel, pAnimal,
               opt_outros_sim, opt_outros_nao,
               moradia_html, status_html, botao)

        html += self.montaTabela()
        html += self.rodape
        return html

    def montaTabela(self):
        html = '''
            <section>
                <h2>Adoções cadastradas</h2>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Adotante</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Animal</th>
                        <th>Outros</th>
                        <th>Moradia</th>
                        <th>Data</th>
                        <th>Status</th>
                        <th>Ações</th>
                    </tr>
        '''

        objAdocao = Adocao()
        dados = objAdocao.obterAdocoes()
        for ado in dados:
            html += '''
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>
                        <a href="/rotaAdocao/alterarAdocao?idAdo=%s">[Alterar]</a>
                        &nbsp;|&nbsp;
                        <a href="/rotaAdocao/excluirAdocao?idAdo=%s"
                           onclick="return confirm('Confirma a exclusão desta adoção?');">[Excluir]</a>
                    </td>
                </tr>
            ''' % (ado["id_adocao"], ado["nome_completo"], ado["email"],
                   ado["telefone"], ado["animal_interesse"],
                   ado["possui_outros_animais"], ado["tipo_moradia"],
                   ado["data_solicitacao"], ado["status"],
                   ado["id_adocao"], ado["id_adocao"])

        html += '''
                </table>
            </section>
        '''
        return html

    @cherrypy.expose()
    def gravarAdocao(self, txtId, txtNome, txtEmail, txtTel, txtAnimal,
                     txtOutros, txtMoradia, txtStatus, btnGravar=None):
        # validação mínima
        if (len(txtNome) == 0 or len(txtEmail) == 0 or len(txtTel) == 0
                or len(txtAnimal) == 0 or len(txtMoradia) == 0):
            return self.paginaResposta(
                icone='⚠️',
                titulo='Campos obrigatórios',
                mensagem='Todos os campos devem ser preenchidos antes de enviar.',
                cor='#e67e22',
                href='/rotaAdocao',
                labelBtn='Voltar ao formulário'
            )

        objAdocao = Adocao()
        objAdocao.set_nome_completo(txtNome)
        objAdocao.set_email(txtEmail)
        objAdocao.set_telefone(txtTel)
        objAdocao.set_animal_interesse(txtAnimal)
        objAdocao.set_possui_outros_animais(txtOutros)
        objAdocao.set_tipo_moradia(txtMoradia)
        objAdocao.set_status(txtStatus)

        if int(txtId) == 0:
            retorno = objAdocao.gravar()
        else:
            objAdocao.set_id(int(txtId))
            retorno = objAdocao.alterar()

        if retorno > 0:
            return self.paginaResposta(
                icone='🐾',
                titulo='Solicitação enviada!',
                mensagem='A adoção de <strong>%s</strong> foi registrada com sucesso.' % txtNome,
                cor='#27ae60',
                href='/rotaAdocao',
                labelBtn='Ver todas as adoções'
            )
        else:
            return self.paginaResposta(
                icone='❌',
                titulo='Erro ao gravar',
                mensagem='Não foi possível registrar a adoção de <strong>%s</strong>. Tente novamente.' % txtNome,
                cor='#e74c3c',
                href='/rotaAdocao',
                labelBtn='Voltar ao formulário'
            )

    @cherrypy.expose()
    def excluirAdocao(self, idAdo):
        objAdocao = Adocao()
        objAdocao.set_id(int(idAdo))
        if objAdocao.excluir() > 0:
            raise cherrypy.HTTPRedirect('/rotaAdocao')
        else:
            return self.paginaResposta(
                icone='❌',
                titulo='Erro ao excluir',
                mensagem='Não foi possível excluir esta solicitação de adoção.',
                cor='#e74c3c',
                href='/rotaAdocao',
                labelBtn='Voltar'
            )

    @cherrypy.expose()
    def alterarAdocao(self, idAdo):
        objAdocao = Adocao()
        dadosSelec = objAdocao.obterAdocao(idAdo)
        if len(dadosSelec) == 0:
            return self.paginaResposta(
                icone='🔍',
                titulo='Não encontrado',
                mensagem='Nenhuma adoção foi encontrada com o ID informado.',
                cor='#7f8c8d',
                href='/rotaAdocao',
                labelBtn='Voltar'
            )
        d = dadosSelec[0]
        return self.montaFormulario(
            pId=d["id_adocao"],
            pNome=d["nome_completo"],
            pEmail=d["email"],
            pTel=d["telefone"],
            pAnimal=d["animal_interesse"],
            pOutros=d["possui_outros_animais"],
            pMoradia=d["tipo_moradia"],
            pStatus=d["status"],
        )
