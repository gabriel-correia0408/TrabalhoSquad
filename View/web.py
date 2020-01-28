from flask import Flask, render_template, request, redirect
import sys
sys.path.append(r'C:\Users\900137\Desktop\TrabalhoSquad')
from Controller.squad_controller import SquadController
from Model.squad import Squad

app = Flask (__name__)
squad_controller = SquadController() 
squad = Squad()
nome = 'HBSIS'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def ler():
    squads = squad_controller.ler()
    return render_template('listar.html', titulo_app = nome, squad = squads)

@app.route('/cadastrar')
def inserir():
    squad = Squad()
    # squad_control = SquadController()
    # squad.Nome = ''
    # squad.descricao = 'testando'
    # squad.NumeroPessoas = 20
    # squad.LinguagemBackEnd = 'testando'
    # squad.FrameworkFrontEnd= 'angular
    # squad_control.inserir(squad)
    if 'id' in request.args:
        id = int(request.args['id'])
        Nome = request.args['Nome']
        Descricao = request.args['Descricao']
        NumeroPessoas = request.args['NumeroPessoas']
        LinguagemBackEnd = request.args['LinguagemBackEnd']
        FrameworkFrontEnd= request.args['FrameworkFrontEnd']
        squad_controller.editar(id, Nome, NumeroPessoas, LinguagemBackEnd, FrameworkFrontEnd)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad )


@app.route('/deletar')
def deletar():
    id = int(request.args['id'])
    squad_controller.deletar(id)    
    return redirect('/listar')

@app.route('/inserir')
def salvar():
    squad = Squad()
    squad.id = request.args['id']
    squad.Nome = request.args['Nome']
    squad.Descricao = request.args['Descricao']
    squad.NumeroPessoas = request.args['NumeroPessoas']
    squad.LinguagemBackEnd = request.args['LinguagemBackEnd']
    squad.FrameworkFrontEnd = request.args['FrameworkFrontEnd']
    
    # squad_controller.inserir(squad)
    if squad.id == 0:
        squad_controller.inserir(squad)
    else:
        squad_controller.editar(squad)
    return redirect ('/listar')
        


    

# @app.route('/editar')
# def editar():
#     return redirect ('/editar')



app.run(debug=True)
#app.run()