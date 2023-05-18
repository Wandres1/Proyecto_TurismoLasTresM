from supabase_py import supabase

class Taxista:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def guardar(self):
        data = {
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono
        }
        response = supabase.table('taxista').insert(data)
        if response['error']:
            return False
        else:
            return True