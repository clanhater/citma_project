import {deleteBlock, getNoticia, crearNoticia, insertarBloque} from  "./api.js"
import buttonPanel from "./componentes/buttonPanel.js";
import contentBlock from "./componentes/contentBlock.js";

const testNews = [
    {
        type: 'title',
        content: 'Descubren nueva especie marina en el Pacífico'
    },
    {
        type: 'text',
        content: 'Científicos de la Universidad de Mariana han identificado una nueva especie de pulpo bioluminiscente en las profundidades del océano Pacífico. El descubrimiento se realizó durante una expedición rutinaria.'
    },
    // {
    //     type: 'image',
    //     content: 'https://ejemplo.com/ruta/imagen-pulpo.jpg'
    // },
    {
        type: 'text',
        content: 'El equipo de investigación, liderado por la Dra. Elena Torres, utilizó un submarino no tripulado equipado con cámaras de alta sensibilidad para capturar las primeras imágenes de esta especie que habita a más de 3,000 metros de profundidad.'
    }
];


/**
 * Genera una lista de bloques con botones "Añadir" entre ellos
 * @param {HTMLElement} container - Contenedor principal
 * @param {Array} blocksData - Datos iniciales de los bloques
 * @param {string} blocksData[].type - Tipo de bloque ('title', 'text', 'image')
 * @param {string} blocksData[].content - Contenido inicial del bloque
 */
export function generateBlocksList(blocksData = []) {
    const container = document.getElementById("blocks-container");
    // Limpiar contenedor
    container.innerHTML = '';
    
    // Botón "Añadir bloque" inicial
    container.appendChild(buttonPanel(null, null));
    
    console.log(data.bloques)
    // Generar bloques iniciales
    let blockList = blocksData.map(blockData => {
        console.log("Creando content block", blockData.orden);
        return contentBlock(blockData.type, blockData.orden, blockData.id, blockData.content);
    });
    

    for (let i = 0; i < blockList.length; i++){
        container.appendChild(blockList[i]);
        let next;
        if(i+1<blockList.length) next = i+1;
        console.log("calling button panel with", i, next)
        container.appendChild(buttonPanel(i,next));
    }

}


async function handleBlockDeletion(deleteButton) {
    const block = deleteButton.closest('.block');
    const blockId = block.dataset.blockId;
    const newsId = block.dataset.newsId;

    // Validar si es un bloque ya persistido (no temporal)
    const isPersisted = blockId && !blockId.startsWith('temp-');

    try {
        if (isPersisted) {
            // Confirmación antes de eliminar
            if (!confirm('¿Estás seguro de eliminar este bloque permanentemente?')) {
                return;
            }

            // Llamada al servidor para eliminar
            
        }

        // Eliminar el bloque del DOM y actualizar controles
        const container = block.closest('#blocks-container');
        block.remove();
        updateSwapButtons(container);

    } catch (error) {
        console.error('Error eliminando bloque:', error);
        alert('No se pudo eliminar el bloque. Por favor intente nuevamente.');
    }
}

export const data = await crearNoticia();
data.bloques = [];

const noticia = document.querySelector("#blocks-container")
noticia.dataset.noticiaId = data.noticia.id
generateBlocksList(data.bloques);