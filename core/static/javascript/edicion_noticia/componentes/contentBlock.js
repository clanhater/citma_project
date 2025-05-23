import deleteButton from "./deleteButton.js";
import { actualizarContenido } from "../buttonEvents.js";
import crearTextBlock from "./textBlock.js";
/**
 * Crea un bloque con contenido inicial
 * @param {string} type - Tipo de bloque
 * @param {string} content - Contenido inicial
 * @returns {HTMLElement} - Elemento del bloque creado
 */
export default function contentBlock(type, orden, id, content = '') {
    const block = document.createElement('div');
    block.className = `block block-${type} block-content`;
    block.dataset.type = type;
    block.dataset.id = orden;

    // Contenido según tipo
    let contentHtml = '';
    switch(type) {
        case 'title':
            contentHtml = `
                <h1 class="display-5 fw-bold mb-3" contenteditable="true">${content || 'Escribe el título aquí...'}</h1>
            `;
            block.innerHTML = contentHtml;
            break;
            
        case 'text':
            contentHtml = crearTextBlock(id, content);
            block.append(contentHtml);
            break;
            
        case 'image':
            contentHtml = `
                <div class="image-uploader">
                    <input type="file" accept="image/*" class="image-input">
                    ${content ? `<img src="${content}" class="image-preview">` : 
                    '<div class="image-placeholder">Selecciona una imagen</div>'}
                </div>
            `;
            block.innerHTML = contentHtml;
            break;
    }
    

    // Estructura con controles a la derecha
    const deletionButton = deleteButton(orden);
    block.appendChild(deletionButton);

    return block;
}

