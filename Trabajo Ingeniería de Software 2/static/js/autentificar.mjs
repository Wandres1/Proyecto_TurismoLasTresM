
import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm'

const supabaseUrl = 'https://xeudcfxkwzjnmbjlyorr.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhldWRjZnhrd3pqbm1iamx5b3JyIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQ0MDYxNDcsImV4cCI6MTk5OTk4MjE0N30.9G3UQp_QKsfXTTMlI8jVYudqeTFyHyrzhlkhsNHT6Ok';

const _supabase = createClient(supabaseUrl, supabaseKey);

let isLoggedIn = false;

document.addEventListener('DOMContentLoaded', function() {
  const formulario = document.getElementById('formulario');
  
  if (formulario) {
    formulario.addEventListener('submit', buscarRegistro);
  }
});


async function buscarRegistro(event) {
  event.preventDefault(); // Evitar el envío del formulario

  // Obtener los valores del formulario
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Realizar la búsqueda en la tabla
  const { data, error } = await _supabase
    .from('Usuarios')
    .select()
    .eq('username', username)
    .eq('password', password);

  if (error) {
    console.error('Error al realizar la búsqueda:', error.message);
  } else {
    if (data.length > 0) {
      console.log('Inicio de sesión exitoso');
      // Redireccionar a otra página después de un inicio de sesión exitoso
      // Después de confirmar que el usuario está logueado
      isLoggedIn = true;
      let usuario = username;

      // Almacenar en el almacenamiento local del navegador
      localStorage.setItem('isLoggedIn', true);
      localStorage.setItem('usuario', usuario);
      window.location.href = 'index.html';
    } else {
      console.log('Credenciales incorrectas');
      // Aquí puedes mostrar un mensaje de error o realizar alguna otra acción
    }
    formulario.reset(); // Reiniciar el formulario después de realizar la búsqueda
  }
}
