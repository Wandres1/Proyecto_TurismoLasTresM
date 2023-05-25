
import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm'

const supabaseUrl = 'https://xeudcfxkwzjnmbjlyorr.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhldWRjZnhrd3pqbm1iamx5b3JyIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQ0MDYxNDcsImV4cCI6MTk5OTk4MjE0N30.9G3UQp_QKsfXTTMlI8jVYudqeTFyHyrzhlkhsNHT6Ok';

const _supabase = createClient(supabaseUrl, supabaseKey);
// Obtener el formulario y agregar un evento de escucha para el envío
console.log('_supabase')
document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formulario2');
    console.log(formulario)
    if (formulario) {
        console.log('Hola2')
      formulario.addEventListener('submit', agregarRegistro);
    }
  });
  
async function agregarRegistro(event) {
  event.preventDefault(); // Evitar el envío del formulario

  // Obtener los valores del formulario
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
    console.log(username)
  // Datos del registro a agregar
  const datos = {
    username: username,
    password: password,
  };

  // Insertar el registro en la tabla
  const { data, error } = await _supabase.from('Usuarios').insert(datos);

  if (error) {
    console.error('Error al agregar el registro:', error.message);
  } else {
    console.log('Registro agregado exitosamente:', data);
    formulario2.reset(); // Reiniciar el formulario después de agregar el registro
  }
}
