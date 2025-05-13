document.querySelectorAll('.btn-toggle-activo').forEach(button => {
    button.addEventListener('click', async function() {
        const url = 'cambiar-estado';
        const empleoId = this.dataset.empleoId;
        const accion = this.dataset.accion; // 'activar' o 'desactivar'
        const card = document.getElementById(`empleo-${empleoId}`);
        
        try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({
            empleo_id: empleoId,
            accion: accion
            })
        });
        
        if (response.ok) {
            const data = await response.json();
            // Actualizar interfaz
            this.textContent = data.nuevo_estado ? 'Desactivar' : 'Activar';
            this.dataset.accion = data.nuevo_estado ? 'desactivar' : 'activar';
            this.classList.toggle('empleo-desactivado', !data.nuevo_estado);
            this.classList.toggle('empleo-activado', data.nuevo_estado);
            
            //doble previous sibling porque podria estar teniendo en cuenta el salto de linea como etiqueta
            const enlace_detalle = this.previousSibling.previousSibling;
            enlace_detalle.classList.toggle('empleo-desactivado', !data.nuevo_estado);
            enlace_detalle.classList.toggle('empleo-activado', data.nuevo_estado);

            card.classList.toggle('card-inactive', !data.nuevo_estado);

        }
        } catch (error) {
        console.error('Error:', error);
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }