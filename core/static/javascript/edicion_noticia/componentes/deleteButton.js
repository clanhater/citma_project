import { eliminarBloque } from "../buttonEvents.js";

export default function deleteButton(deletionId) {
    const button = document.createElement('button');
    button.dataset.id = deletionId;
    
    button.classList.add("btn");
    button.classList.add("btn-outline-danger");
    button.classList.add("btn-delete");

    button.innerHTML = '<i class="fas fa-trash"></i>';
    
    button.addEventListener('mouseup', async(e) => {
        e.preventDefault();
        eliminarBloque(deletionId);
    });

    return button;
}
