
from Dao.squad_dao import SquadDao
from Model.squad import Squad

class SquadController: # subscrevendo para a classe 'SquadController'
    dao = SquadDao()

    def ler(self):
        return self.dao.ler()

    def salvar(self, Squad:Squad):
        return self.dao.salvar(Squad)

    def inserir(self, squad:Squad):
        self.dao.inserir(squad)

    def deletar(self, id):
        self.dao.deletar(id)

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def editar(self,id, Nome,Descricao,NumeroPessoas,LinguagemBackEnd,FrameworkFrontEnd):
        self.dao.editar(self, id,Nome,Descricao,NumeroPessoas,LinguagemBackEnd,FrameworkFrontEnd)