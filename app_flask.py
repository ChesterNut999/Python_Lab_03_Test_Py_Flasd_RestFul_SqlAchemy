from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api

from models import Devs, Devs_Atividades, ID

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# ID = {'maurilio': '123', 'rafael': '321'}

#@auth.verify_password
#def verificacao(username, password):
#    print ('...VALIDANDO ACESSO...')
#    if not (username, password):
#        return False
#    return ID.get(username) == password

@auth.verify_password
def verificacao(username, password):
    print('...VALIDANDO ACESSO...')
    if not (username, password):
        return False
    return ID.query.filter_by(username=username, password=password).first()


class Devs(Resource):
    @auth.login_required

    # OBTEM A LISTA DE REGISTROS DO BD
    def get(self, NOME):
        devs = Devs.query.filter_by(NOME=NOME).first()

        try:
            response = {'NOME': devs.nome, 'IDADE': devs.idade, 'ID': devs.id}
        except AttributeError:
            response = {'STATUS': 'error', 'MENSAGEM': 'Dev não cadastrado!'}

        return response

    # INSERE NOVOS REGISTROS NO BD
    def put(self, NOME):
        devs = Devs.query.filter_by(NOME=NOME).first()
        dados = request.json

        if 'NOME' in dados:
            devs.nome = dados['NOME']
        if 'IDADE' in dados:
            devs.idade = dados['IDADE']
        devs.save()
        response = {'ID': devs.id, 'NOME': devs.nome, 'IDADE': devs.idade}

        return response

    # DELETA REGISTROS DO BD
    def delete(self, NOME):
        devs = Devs.query.filter_by(NOME=NOME).first()
        devs.delete()
        return {'STATUS': 'sucesso', 'MENSAGEM': 'Dev {} deletado com sucesso!'}


class Devs_Lista(Resource):
    @auth.login_required

    # OBTEM A LISTA DE REGISTROS DO BD
    def get(self):
        devs = Devs.query.all()

        response = [{'ID': i.id, 'NOME': i.nome, 'IDADE': i.idade} for i in devs]
        return response

    # ALTERA OS REGISTROS DO BD
    def post(self):
        dados = request.json
        devs = Devs(nome=dados['NOME'], idade=dados['IDADE'])
        devs.save()

        response = {'ID': devs.id, 'NOME': devs.nome, 'IDADE': devs.idade}


class Devs_Atividades(Resource):
    @auth.login_required

    def get(self):
        dev_atividades = Devs_Atividades.query.all()
        response = [{'ID': i.id, 'NOME': i.nome, 'DEV': i.dev.nome} for i in dev_atividades]
        return response

    def post(self):
        dados = request.json
        dev = Devs.query.filter_by(NOME=dados['DEV']).first()
        devs_atividades = Devs_Atividades(NOME=dados['NOME'], DEV=dev)
        devs_atividades.save()

        response = {'DEV': devs_atividades.DEV.NOME, 'ATIVIDADE': devs_atividades.NOME, 'ID': devs_atividades.id}

        return response


api.add_resource(Devs, '/devs/<string:NOME>/')
api.add_resource(Devs_Lista, '/devs_lista/')
api.add_resource(Devs_Atividades, '/devs_atividades/')

if __name__ == '__main__':
    app.run(debug=True)
