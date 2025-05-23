import {generateBlocksList as render, data} from "./edicion_noticia.js";
import { deleteBlock, insertarBloque as insertarBloqueServer, intercambiarBloques } from "./api.js";


function reordenarBloques(){
    for(let i = 0; i < data.bloques.length; i++){
        data.bloques[i].orden = i;
    }
}

export async function insertarBloque(id_insertado){
    // Llamar al servidor para insertar
    const container = document.querySelector("#blocks-container")
    const noticia_id = container.dataset.noticiaId;
    const response = await insertarBloqueServer(id_insertado, noticia_id, 'text');
    
    if (response.success) {
        const nuevoBloque = {
            id: response.blockData.block_id,
            type: response.blockData.type,
            orden: response.blockData.order,
            content: response.blockData.contenido
        }
        console.log(response.blockData)
        data.bloques.splice(id_insertado, 0, nuevoBloque);
        reordenarBloques()
        render(data.bloques);
    }
}

export async function swapBlocks(previousId, nextId) {
    const container = document.querySelector("#blocks-container")
    const noticia_id = container.dataset.noticiaId;
    const response = await intercambiarBloques(noticia_id, previousId, nextId);
    
    if (response) {
        const temp = data.bloques[previousId];
        data.bloques[previousId] = data.bloques[nextId]
        data.bloques[nextId] = temp;

        render(data.bloques);
    }
}

export async function actualizarContenido(idBloque, nuevoContenido) {
    const container = document.querySelector("#blocks-container")
    const noticia_id = container.dataset.noticiaId;

    let i = 0;
    for( ; i<data.bloques.length; i++){
        if(data.bloques[i].id == idBloque){
            data.bloques[i].content = nuevoContenido;
            break;
        }
    }

}

export async function eliminarBloque(id_eliminado) {
    const container = document.querySelector("#blocks-container")
    const noticia_id = container.dataset.noticiaId;

    const response = await deleteBlock(noticia_id, id_eliminado);

    if (response) {
        data.bloques.splice(id_eliminado, 1);
        reordenarBloques()
        render(data.bloques);
    }
}