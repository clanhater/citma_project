import { actualizarContenido } from "../buttonEvents.js";

export default function crearTextBlock(idBloque, contenido = "") {
    const text = document.createElement('p');
    text.contentEditable = "true";
    text.classList = "lead"
    text.innerHTML = contenido || 'Escribe el texto aquí...';

    text.addEventListener('blur', function() {
        console.log('Edición finalizada:', this.innerHTML);
        actualizarContenido(idBloque, this.innerHTML);
    });

    return text;
}