import { swapBlocks } from "../buttonEvents.js";


export default function swapButton(previousBlockId, nextBlockId) {
    const swapButton = document.createElement('button');
    swapButton.classList.add('btn', 'btn-outline-primary', 'btn-sm', 'm-1');
    swapButton.innerHTML = '<i class="fas fa-exchange-alt"></i> Intercambiar';

    swapButton.dataset.previousId = previousBlockId;
    swapButton.dataset.nextId = nextBlockId;
    
    // Evento para intercambiar bloques
    swapButton.addEventListener('click', (e) => {
        e.preventDefault();
        previousBlockId = swapButton.dataset.previousId;
        nextBlockId = swapButton.dataset.nextId;
        swapBlocks(previousBlockId, nextBlockId);
    });

    return swapButton;
}