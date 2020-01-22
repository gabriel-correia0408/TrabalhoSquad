from flask import Flask, render_template, request, redirect
import sys
sys.path.append('C:/Users/900137/Desktop/pythonatividades/pythonatividades/Aula37')
from Controller.squad_controller import SquadController
from Model.squad import Squad


controller = SquadController()

nome = 'TESTANDO :/'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def ler():
    squads = squad_controller.listar_todos()
    return render_template('ler.html', titulo_app = nome, lista = squads)

@app.route('/inserir')
def inserir():
    squad = Squad()
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('inserir.html', titulo_app = nome, squad = squad )


@app.route('/deletar')
def deletar():
    id = int(request.args['id'])
    squad_controller.deletar(id)
    if id_end != 'None':
        end_controller.deletar(id_end)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = request.args['id']
    squad.Nome = request.args['Nome']
    squad.Descricao = request.args['Descricao']
    squad.NumeroPessoas = request.args['NumeroPessoas']
    squad.LinguagemBackEnd = request.args['LinguagemBackEnd']
    squad.FrameworkFrontEnd = request.args['FrameworkFrontEnd']
    
    
    
    return squad_controller.inserir(squad)


app.run(debug=True)
