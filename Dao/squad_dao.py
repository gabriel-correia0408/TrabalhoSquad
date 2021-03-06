import MySQLdb
from Model.squad import Squad 

squad = Squad()
class SquadDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()
    
    def ler(self):
        comando = f"SELECT * FROM Squad_gabrielcorreia "
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def inserir(self, squad: Squad):
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



    def deletar(self, id):
        comando = f"DELETE FROM Squad_gabrielcorreia WHERE id = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
        
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM Squad_gabrielcorreia WHERE id = {id}"
        self.cursor.execute(comando)
        p = self.cursor.fetchone()
        squad = Squad()
        squad.id =  p[0]
        squad.Nome = p[1]
        squad.Descricao = p[2]
        squad.NumeroPessoas = p[3]
        squad.LinguagemBackEnd = p[4]
        squad.FrameworkFrontEnd = p[5]
        return squad


# PDATE `topskills01`.`Squad_gabrielcorreia` SET `Nome` = 'odinzelolo' WHERE (`id` = '80');
    def editar(self, id,Nome,Descricao,NumeroPessoas,LinguagemBackEnd,FrameworkFrontEnd):
        comando = f''' 
        UPDATE Squad_gabrielcorreia SET
        Nome = '{Nome}'
        Descricao = '{Descricao}'
        NumeroPessoas = '{NumeroPessoas}'
        LinguagemBackEnd = '{LinguagemBackEnd}
        FrameworkFrontEnd = '{FrameworkFrontEnd}'
        WHERE  id = {id}
        
        '''
        self.cursor.execute(comando)
        self.conexao.commit()