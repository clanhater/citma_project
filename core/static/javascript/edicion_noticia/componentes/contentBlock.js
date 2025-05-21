/**
 * Crea un bloque con contenido inicial
 * @param {string} type - Tipo de bloque
 * @param {string} content - Contenido inicial
 * @returns {HTMLElement} - Elemento del bloque creado
 */
export default function contentBlock(type, id, content = '') {
    const block = document.createElement('div');
    block.className = `block block-${type}`;
    block.dataset.type = type;
    
    // Contenido según tipo
    let contentHtml = '';
    switch(type) {
        case 'title':
            contentHtml = `
                <h1 class="display-5 fw-bold mb-3" contenteditable="true">${content || 'Escribe el título aquí...'}</h1>
            `;
            break;
            
        case 'text':
            contentHtml = `
                <p class="lead" contenteditable="true" >${content|| 'Escribe el texto aquí...'}</p>
            `;
            break;
            
        case 'image':
            contentHtml = `
                <div class="image-uploader">
                    <input type="file" accept="image/*" class="image-input">
                    ${content ? `<img src="${content}" class="image-preview">` : 
                    '<div class="image-placeholder">Selecciona una imagen</div>'}
                </div>
            `;
            break;
    }
    
    // Estructura con controles a la derecha
    block.innerHTML = `
        <div id="${id}" class="block-content" data-id="${id}">
            ${contentHtml}
            <button type="button" 
                    class="btn btn-outline-danger btn-delete" 
                    title="Eliminar documento">
              <i class="fas fa-trash"></i>
            </button>
        </div>

    `;
    
    // Añadir eventos a los controles
    // setupBlockControls(block);
    return block;
}

