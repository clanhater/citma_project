import {
  getErrorNombre,
  getErrorCorreo,
} from './limpiar_campos.js'

const formulario = document.getElementById('formulario')

  // Obteniendo inputs del formulario
  const nombre = document.getElementById('id_nombre');
  const correo = document.getElementById('id_correo');
  const texto = document.getElementById('id_texto');
  const estrellas = document.getElementById('id_estrellas');
  const submit = document.getElementById('boton_envio');

  export function getSomeError() {
    const errorNombre = getErrorNombre(nombre.value);
    console.log(errorNombre)
    const errorCorreo = getErrorCorreo(correo.value);
    console.log(errorCorreo)
    const errorEstrellas = estrellas.value < 1? "Añade una calificacion" : null;
    console.log(errorEstrellas)

    let errorMsg;
    console.log(estrellas.value)
    if (errorNombre){
      errorMsg = errorNombre;
      showError(errorNombre);
    } else if (errorCorreo){
      errorMsg = errorCorreo;
      showError(errorCorreo)
    } else if( !(nombre.value && correo.value && texto.value) ){
      errorMsg = 'Los tres campos son obligatorios';
      showError(errorMsg);
    } else if(errorEstrellas){
      errorMsg = errorEstrellas;
      showError(errorEstrellas);
    } else {
      cleanError();
    }
    return errorMsg;
  }

  nombre.addEventListener('blur', (e) => {
    const errorNombre = getErrorNombre(nombre.value);

    if (errorNombre) {
      showError(errorNombre);
    } else {
      getSomeError();
    }
  });

  correo.addEventListener('blur', (e) => {
    const errorCorreo = getErrorCorreo(correo.value);

    if (errorCorreo) {
      showError(errorCorreo);
    } else {
      getSomeError();
    }
  })

  submit.addEventListener('click', (e) => {
    console.log('HOLA??')
    const errorMsg = getSomeError();
    console.log(errorMsg)
    if (errorMsg){
      e.preventDefault();
    }
  })

export function showError(msg) {
  const label = document.querySelector('#error-msg');
  label.innerHTML = msg;
}
export function cleanError() {
  const label = document.querySelector('#error-msg');
  label.innerHTML = '';
}