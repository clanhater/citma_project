document.addEventListener('DOMContentLoaded', () => {
  const firstTab = document.querySelector('#personal')
  const secondTab = document.querySelector('#experiencia')

  const nextBtn = document.querySelector('#next-btn')
  const previoustBtn = document.querySelector('#previous-btn')

  const nombreCompleto = document.querySelector('#id_nombre_apellidos')
  const telefono = document.querySelector('#id_telefono')
  const correo = document.querySelector('#id_correo_electronico')
  const direccion = document.querySelector('#id_direccion')


  // Eventos de botones y campos ------------------------
  nombreCompleto.addEventListener('blur', (e)=>{
    const msgError = getErrorNomre(nombreCompleto.value);

    if ( msgError != null){
      showError(msgError);
    } else {
      reviewForError();
    }
  });

  telefono.addEventListener('blur', (e)=>{
    const msgError = getErrorTelefono(telefono.value);

    if ( msgError ){
      showError(msgError);
    } else {
      reviewForError();
    }
  });

  correo.addEventListener('blur', (e)=>{
    const msgError = getErrorCorreo(correo.value);

    if ( msgError ){
      showError(msgError);
    } else {
      reviewForError();
    }
  });

  direccion.addEventListener('blur', (e)=>{
    const msgError = getErrorDireccion(direccion.value);

    if ( msgError ){
      showError(msgError);
    } else {
      reviewForError();
    }
  });


  function reviewForError() {
    let msgError;
    msgError = getErrorNomre(nombreCompleto.value);
    if (msgError == null) msgError = getErrorTelefono(telefono.value);
    if (msgError == null) msgError = getErrorCorreo(correo.value);
    if (msgError == null) msgError = getErrorDireccion(direccion.value);

    if (msgError != null){
      showError(msgError);
      console.log("Testing")
    } else {
      clearError();
    }

    return msgError
  }

  nextBtn.addEventListener('click', (e) => {
    e.preventDefault();

    let msgError = reviewForError();

    
    if (msgError != null){
      showError(msgError);
    } else if(!(
        nombreCompleto.value && 
        telefono.value && 
        correo.value && 
        direccion.value)){
      showError("Todos estos campos son obligatorios.");
    } else {
      clearError();
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


 // Funciones de revision para cada campo -----------------


function getErrorNomre(nombre) {
  if(!nombre) return null; //No detectar error si esta vacio
  // Permite letras, espacios, acentos y caracteres especiales comunes en nombres
  const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s'-]+$/;

  if(!regex.test(nombre.trim())) {
  return "El nombre solo debe contener letras y espacios.";
  } else if (nombre.trim().length <= 2){
    return "El nombre es muy corto.";
  } else if (nombre.trim().length > 200){
    return "El nombre es demasiado largo."
  } else {
    return null;
  }
}


function getErrorTelefono(telefono) {
  if(!telefono) return null; //No detectar error si esta vacio
  // Valida formatos internacionales, con o sin código de país
  const regex = /^(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{2,4}$/;
  const soloNumeros = telefono.replace(/[^0-9]/g, '');

  if (/[a-zA-Z]/.test(telefono)){
    return "El número telefónico no debe contener letras.";
  } else if (soloNumeros.length <= 7) {
    return "El número es demasiado corto.";
  } else if (soloNumeros.length > 15) {
    return "El número es demasiado largo.";
  }else if (!regex.test(telefono.trim())){
    return "El número está mal escrito.";
  } else {
    return null;
  }
}

function getErrorCorreo(correo) {
  if(!correo) return null; //No detectar error si esta vacio
  // Validación estándar de emails
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if(correo.trim().length > 100){
    return "El correo es demasiado largo."
  } else if(correo.includes('@@')){
    return "El correo tiene doble '@'."
  } else if(correo.includes('..')) {
    return "El correo contiene puntos consecutivos."
  } else if(!correo.includes('@')){
    return "El correo debe contener dominio(@)."
  }else if (!correo.includes('.')){
    "El dominio correo está mal escrito, no tiene punto '.'"
  } else if (!regex.test(correo.trim())){
    return "El correo está mal escrito."
  } else {
    return null;
  }
}

function getErrorDireccion(direccion) {
  if(!direccion) return null; //No detectar error si esta vacio
  // Valida direcciones con letras, números, símbolos comunes y acentos
  const regex = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s#.,-]+$/;

  if (direccion.length < 5) {
    return "La dirección es demasiado corta."
  } else if(!/[a-zA-Z]/.test(direccion)){
    return "La dirección debe contener letras."
  } else if(!regex.test(direccion.trim())){
    return "La dirección no puede contener carácteres especiales."
  } else {
    return null;
  }
}

function showError(message) {
  const errorElement = document.querySelector('#error-msg');
  errorElement.innerHTML = message;
}

function clearError() {
  const errorElement = document.querySelector('#error-msg');
  errorElement.innerHTML = '';
}