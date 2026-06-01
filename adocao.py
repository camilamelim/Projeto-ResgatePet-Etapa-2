from classes.banco import Banco


class Adocao():
    '''Representa uma solicitação de adoção (tabela adocao do banco).
       Colunas: id_adocao, nome_completo, email, telefone,
                animal_interesse, possui_outros_animais, tipo_moradia,
                data_solicitacao, status
    '''

    def __init__(self):
        self.__id = 0
        self.__nome_completo = ''
        self.__email = ''
        self.__telefone = ''
        self.__animal_interesse = ''
        self.__possui_outros_animais = ''
        self.__tipo_moradia = ''
        self.__status = 'Em análise'
        self.__banco = Banco()

    # --- setters ---
    def set_id(self, pId):
        if pId > 0:
            self.__id = pId

    def set_nome_completo(self, pValor):
        if len(pValor) > 0:
            self.__nome_completo = pValor

    def set_email(self, pValor):
        if len(pValor) > 0:
            self.__email = pValor

    def set_telefone(self, pValor):
        if len(pValor) > 0:
            self.__telefone = pValor

    def set_animal_interesse(self, pValor):
        if len(pValor) > 0:
            self.__animal_interesse = pValor

    def set_possui_outros_animais(self, pValor):
        if len(pValor) > 0:
            self.__possui_outros_animais = pValor

    def set_tipo_moradia(self, pValor):
        if len(pValor) > 0:
            self.__tipo_moradia = pValor

    def set_status(self, pValor):
        if len(pValor) > 0:
            self.__status = pValor

    # --- getters ---
    def get_id(self):
        return self.__id

    def get_nome_completo(self):
        return self.__nome_completo

    def get_email(self):
        return self.__email

    def get_telefone(self):
        return self.__telefone

    def get_animal_interesse(self):
        return self.__animal_interesse

    def get_possui_outros_animais(self):
        return self.__possui_outros_animais

    def get_tipo_moradia(self):
        return self.__tipo_moradia

    def get_status(self):
        return self.__status

    # --- consultas ---
    def obterAdocoes(self):
        sql = '''SELECT * FROM adocao
                 ORDER BY data_solicitacao DESC, id_adocao DESC'''
        return self.__banco.executarSelect(sql)

    def obterAdocao(self, pId=0):
        if pId != 0:
            self.__id = pId
        sql = '''SELECT * FROM adocao
                 WHERE id_adocao = #id'''
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarSelect(sql)

    # --- CRUD ---
    def gravar(self):
        # data_solicitacao usa o DEFAULT date('now') definido no CREATE TABLE
        sql = '''INSERT INTO adocao
                 (nome_completo, email, telefone, animal_interesse,
                  possui_outros_animais, tipo_moradia, status)
                 VALUES
                 ("#nome", "#email", "#tel", "#animal",
                  "#outros", "#moradia", "#status")'''
        sql = sql.replace('#nome', self.__nome_completo)
        sql = sql.replace('#email', self.__email)
        sql = sql.replace('#tel', self.__telefone)
        sql = sql.replace('#animal', self.__animal_interesse)
        sql = sql.replace('#outros', self.__possui_outros_animais)
        sql = sql.replace('#moradia', self.__tipo_moradia)
        sql = sql.replace('#status', self.__status)
        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        sql = '''UPDATE adocao SET
                    nome_completo = "#nome",
                    email = "#email",
                    telefone = "#tel",
                    animal_interesse = "#animal",
                    possui_outros_animais = "#outros",
                    tipo_moradia = "#moradia",
                    status = "#status"
                 WHERE id_adocao = #id'''
        sql = sql.replace('#nome', self.__nome_completo)
        sql = sql.replace('#email', self.__email)
        sql = sql.replace('#tel', self.__telefone)
        sql = sql.replace('#animal', self.__animal_interesse)
        sql = sql.replace('#outros', self.__possui_outros_animais)
        sql = sql.replace('#moradia', self.__tipo_moradia)
        sql = sql.replace('#status', self.__status)
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)

    def excluir(self):
        sql = 'DELETE FROM adocao WHERE id_adocao = #id'
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)
