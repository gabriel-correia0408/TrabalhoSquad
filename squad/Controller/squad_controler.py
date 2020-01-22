
from Dao.squad_dao import SquadDao
from Model.squad import Squad

class SquadDao:
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
        self.dao.buscar_por_id(id)