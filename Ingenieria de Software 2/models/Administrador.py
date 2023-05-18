from supabase_py import supabase

class Administrador:
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
        response = supabase.table('administrador').insert(data)
        if response['error']:
            return False
        else:
            return True