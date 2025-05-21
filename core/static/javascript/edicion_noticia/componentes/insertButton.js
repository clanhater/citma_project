import buttonPanel from "./buttonPanel.js";
import contentBlock from "./contentBlock.js";
import { insertarBloque } from "../buttonEvents.js";

export default function createInsertButton(insersionId) {

    const insertButton = document.createElement('button');
    insertButton.classList.add('btn', 'btn-outline-success', 'btn-insert');
    insertButton.innerHTML = '<i class="fas fa-plus"></i> Añadir bloque';

    insertButton.dataset.insersionId = insersionId

    // Evento de click mejorado
    insertButton.addEventListener('click', async (e) => {
        e.preventDefault();
        const id = insertButton.dataset.insersionId;
        console.log(id);
        insertarBloque(id);
    });

    return insertButton;
}
