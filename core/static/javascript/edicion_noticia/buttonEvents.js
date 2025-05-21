import {generateBlocksList, data} from "./edicion_noticia.js";
import { insertarBloque as insertarBloqueServer, intercambiarBloques } from "./api.js";

export async function insertarBloque(id_insertado){
    // Llamar al servidor para insertar
    const container = document.querySelector("#blocks-container")
    const noticia_id = container.dataset.noticiaId;
    const response = await insertarBloqueServer(id_insertado, noticia_id, 'text');
    
    if (response.success) {
        const nuevoBloque = {
            type: response.blockData.type,
            id: response.blockData.order,
            content: response.blockData.contenido
        }
        console.log(response.blockData)
        data.bloques.splice(id_insertado, 0, nuevoBloque);
        generateBlocksList(data.bloques);
    }
}

export async function swapBlocks(previousId, nextId) {
    const container = document.querySelector("#blocks-container")
    const noticia_id = container.dataset.noticiaId;
    const response = await intercambiarBloques(noticia_id, previousId, nextId);
    
    if (response.success) {
        const temp = data.bloques[previousId];
        data.bloques[previousId] = data.bloques[nextId]
        data.bloques[nextId] = temp;

        generateBlocksList(data.bloques);
    }
}
