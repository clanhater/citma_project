import insertButton from './insertButton.js';
import swapButton from './swapButton.js';
/**
 * Crea un div con los botones intercambiar y añadir segun sea necesario
 * Se debe colocar aldededor o entre los bloques para añadir nuevos bloques
 * @param {HTMLElement|null} previousBlock - Bloque después del cual se inserta (null para inicio)
 * @param {HTMLElement|null} nextBlock - Bloque antes del cual se inserta (null para final)
 */
export default function buttonPanel(previousBlockId, nextBlockId) {
    const buttons = document.createElement('div')
    buttons.classList.add("block-controls");

    const hasPrevious = previousBlockId !== undefined && previousBlockId !== null;
    const hasNext = nextBlockId !== undefined && nextBlockId !== null;

    let insersionId;
    if(hasNext){
        insersionId = nextBlockId;
    } else if(hasPrevious){
        insersionId = previousBlockId+1;
    } else{
        insersionId = 0;
    }
    const boton_insertar = insertButton(insersionId);
    buttons.append(boton_insertar)
    
    if (hasPrevious && hasNext) {
        const botonIntercambio = swapButton(previousBlockId, nextBlockId);
        buttons.append(botonIntercambio);
    }
    

    return buttons;
    // if (previousBlock) {
    //     previousBlock.after(buttons);
    // } else {
    //     container.prepend(buttons);
    // }
}