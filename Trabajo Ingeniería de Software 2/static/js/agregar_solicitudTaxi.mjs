
import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm'

const supabaseUrl = 'https://xeudcfxkwzjnmbjlyorr.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhldWRjZnhrd3pqbm1iamx5b3JyIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQ0MDYxNDcsImV4cCI6MTk5OTk4MjE0N30.9G3UQp_QKsfXTTMlI8jVYudqeTFyHyrzhlkhsNHT6Ok';

const _supabase = createClient(supabaseUrl, supabaseKey);
// Obtener el formulario y agregar un evento de escucha para el envío
console.log('_supabase')
document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formulario-tarjeta');
    console.log(formulario)
    if (formulario) {
        console.log('Hola2')
      formulario.addEventListener('submit', agregarRegistro);
    }
  });
  
async function agregarRegistro(event) {
  event.preventDefault(); // Evitar el envío del formulario

  // Obtener los valores del formulario
  const username = localStorage.getItem('usuario');
  const recogida = document.getElementById('direccion1').value;
  const destino = document.getElementById('direccion2').value;
  const precio = document.getElementById('precio').value;
  const informacion = document.getElementById('informacion').value;
  const tipo = 'Servicio Taxi';
    console.log('recogida')
  // Datos del registro a agregar
  const datos = {
    username: username,
    recogida: recogida,
    destino: destino,
    precio: precio,
    informacion: informacion,
    tipo: tipo,
  };

  // Insertar el registro en la tabla
  const { data, error } = await _supabase.from('Solicitud').insert(datos);

  if (error) {
    console.error('Error al agregar el registro:', error.message);
  } else {
    console.log('Registro agregado exitosamente:', data);
    alert('Solicitud Enviada')
    formulario.reset(); // Reiniciar el formulario después de agregar el registro
  }
}
