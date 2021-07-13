from models import Devs, ID

def insere_db():
    devs_nomes = Devs (NOME='Rafael', IDADE=30)
    print(devs_nomes)
    Devs.save()

def insere_usuario_db(username, password):
    id = ID(username=username, password=password)
    id.save()

def consulta_db():
    devs_nomes = Devs.query.all()
    print(devs_nomes)
    devs_nomes = Devs.query.filter_by(NOME='Rafael').first()
    print(devs_nomes.idade)

def consulta_usuarios_db():
    id = ID.query.all
    print(id)

def altera_db():
    devs_nomes = Devs.query.filter_by(NOME='Maurilio').first()
    devs_nomes.nome = 'Felipe'
    devs_nomes.save()

def deleta_db():
    devs_nomes = Devs.query.filter_by(NOME='Maurillio').first()
    devs_nomes.delete()



if __name__ == '__main__':
    #insere_db()
    insere_usuario_db('Mauricio', '123')
    insere_usuario_db('Xiquinha', '123')
    #altera_db()
    #consulta_db()
    consulta_usuarios_db()
    #deleta_db()



