import MySQLdb
from Model.squad import Squad 

class SquadDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()


    
    def ler(self, id):
        comando = f"SELECT * FROM Squad_gabrielcorreia ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad_gabrielcorreia):
        comando = f""" INSERT INTO Squad_gabrielcorreia
        (
            Nome,
            Descricao,
            NumeroPessoas,
            LinguagemBackEnd,
            FrameworkFrontEnd
        )
        VALUES
        (
            '{squad.Nome}',
            '{squad.Descricao}',
            '{squad.NumeroPessoas}',
            '{squad.LinguagemBackEnd}',
            '{squad.FrameworkFrontEnd}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def inserir(self, Squad:Squad):
        comando = f""" UPDATE Squad_gabrielcorreia
        SET
            NOME = '{squad.Nome}',
            SOBRENOME ='{squad.Descricao}',
            IDADE = {squad.NumeroSquads},
            ENDERECO_ID = {squad.endereco.id}
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM Squad_gabrielcorreia WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
        
    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  p[0]
        squad.Nome = p[1]
        squad.Descricao = p[2]
        squad.NumeroPessoas = p[3]
        squad.LinguagemBackEnd = p[5]
        squad.FrameworkFrontEnd = p[6]
        return squad