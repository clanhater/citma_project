export function getErrorNombre(nombre) {
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


export function getErrorTelefono(telefono) {
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

export function getErrorCorreo(correo) {
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
    } else if (!correo.includes('.')){
        "El dominio correo está mal escrito, no tiene punto '.'"
    } else if (!regex.test(correo.trim())){
        return "El correo está mal escrito."
    } else {
        return null;
    }
}

export function getErrorDireccion(direccion) {
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
