import {
  getErrorNombre,
  getErrorCorreo,
  getErrorTelefono,
  getErrorDireccion,
} from './limpiar_campos.js'

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
    const msgError = getErrorNombre(nombreCompleto.value);

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
    msgError = getErrorNombre(nombreCompleto.value);
    if (msgError == null) msgError = getErrorTelefono(telefono.value);
    if (msgError == null) msgError = getErrorCorreo(correo.value);
    if (msgError == null) msgError = getErrorDireccion(direccion.value);

    if (msgError != null){
      showError(msgError);
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

function showError(message) {
  const errorElement = document.querySelector('#error-msg');
  errorElement.innerHTML = message;
}


function clearError() {
  const errorElement = document.querySelector('#error-msg');
  errorElement.innerHTML = '';
}