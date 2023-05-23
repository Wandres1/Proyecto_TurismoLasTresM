class ModelUsuario():

    def login(self, db, user):
        try:
            cursor=db.connection.cursor()
        except:
            pass