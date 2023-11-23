# Aula 18 do Capitulo 9 de APIs
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Criar usuários admin
        autor = Autor(nome='Ariel',email='arieldevops@fiuza.com.br', senha=123456, admin=True)
        db.session.add(autor) # Add as especificações do autor a cima dentro da tabela
        db.session.commit() # Salva na tabela esse mesmo autor

if __name__ == '__main__':
    inicializar_banco()