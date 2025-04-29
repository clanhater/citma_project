document.addEventListener('DOMContentLoaded', () => {
  const firstTab = document.querySelector('#personal')
  const secondTab = document.querySelector('#experiencia')

  const nextBtn = document.querySelector('#next-btn')
  const previoustBtn = document.querySelector('#previous-btn')

  const nombreCompleto = document.querySelector('#id_nombre_apellidos')
  const telefono = document.querySelector('#id_telefono')
  const correo = document.querySelector('#id_correo_electronico')
  const direccion = document.querySelector('#id_direccion')


  nextBtn.addEventListener('click', (e) => {
    e.preventDefault();

    let is_valid = true;

    if ( !validarNombre(nombreCompleto.value) ){
      showError(nombreCompleto, "El nombre no está escrito correctamente.")
      is_valid = false;

    } else if ( !validarTelefono(telefono.value) ){
      showError(nombreCompleto, "El numero telefónico no está escrito correctamente.")
      is_valid = false;

    } else if ( !validarCorreo(correo.value) ){
      showError(nombreCompleto, "El correo electrónico no está escrito correctamente.")
      is_valid = false;

    } else if ( !validarDireccion(direccion.value) ){
      showError(nombreCompleto, "La direccion no está escrita correctamente.")
      is_valid = false;

    } else {
      clearError(nombreCompleto);
      clearError(telefono);
      clearError(correo);
      clearError(direccion);
    }

    if (is_valid){
      firstTab.classList.remove('show', 'active');
      secondTab.classList.add('show', 'active');
    }
  });

  previoustBtn.addEventListener('click', (e) => {
    e.preventDefault();

    firstTab.classList.add('show', 'active');
    secondTab.classList.remove('show', 'active');
  });

});

function validarNombre(nombre) {
  // Permite letras, espacios, acentos y caracteres especiales comunes en nombres
  const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s'-]+$/;
  return (
      typeof nombre === 'string' &&
      nombre.trim().length >= 2 &&  // Mínimo 2 caracteres
      nombre.trim().length <= 200 && // Máximo 200 caracteres
      regex.test(nombre.trim())
  );
}

function validarTelefono(telefono) {
  // Valida formatos internacionales, con o sin código de país
  const regex = /^(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{2,4}$/;
  const soloNumeros = telefono.replace(/[^0-9]/g, '');
  return (
      typeof telefono === 'string' &&
      soloNumeros.length >= 7 &&    // Mínimo 7 dígitos (para teléfonos locales)
      soloNumeros.length <= 15 &&   // Máximo 15 dígitos (incluyendo código país)
      regex.test(telefono.trim())
  );
}

function validarCorreo(correo) {
  // Validación estándar de emails
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return (
      typeof correo === 'string' &&
      correo.trim().length <= 100 && // Longitud máxima razonable
      regex.test(correo.trim()) &&
      !correo.includes('..') &&      // Evita puntos consecutivos
      correo.split('@')[0].length >= 1 // Parte antes del @ no vacía
  );
}

function validarDireccion(direccion) {
  // Valida direcciones con letras, números, símbolos comunes y acentos
  const regex = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s#.,-]+$/;
  return (
      typeof direccion === 'string' &&
      direccion.trim().length >= 5 &&  // Mínimo 5 caracteres
      regex.test(direccion.trim()) &&
      /[a-zA-Z]/.test(direccion)       // Debe contener al menos una letra
  );
}

function showError(field, message) {
  field.classList.add('is-invalid');
  const errorElement = document.querySelector('#error-msg');
  errorElement.innerHTML = message;
}

function clearError(field) {
  const errorElement = document.querySelector('#error-msg');
  errorElement.innerHTML = '';
}