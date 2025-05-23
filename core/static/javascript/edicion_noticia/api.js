const url = "/edicion_noticia/";

function getCSRFToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    return cookieValue || '';
}

export async function getNoticia(noticiaId) {
    try {
        const response = await fetch(url + `datos/${noticiaId}/`);
        const data = await response.json();
        
        if (data.status === 'success') {
            return data;  // Retorna {noticia, bloques}
        } else {
            throw new Error(data.message || 'Error al obtener noticia');
        }
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

export async function crearNoticia() {
    try {
        const response = await fetch(url+'crear', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                // Puedes enviar parámetros iniciales si es necesario
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            return {
                noticia: data.noticia,
                bloques: [],
            };
        } else {
            throw new Error(data.message || 'Error al crear noticia');
        }
    } catch (error) {
        console.error('Error creando noticia:', error);
        throw error;
    }
}


export async function insertarBloque(posicion, noticia_id, tipo = 'text') {
    try {
        const response = await fetch(url + "nuevo_bloque", {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                noticia_id: noticia_id,
                orden: posicion,
                type: tipo
            })
        });

        const data = await response.json();
        console.log("id from api", data.order);
        if (!response.ok) {
            throw new Error(data.message || 'Error al insertar bloque');
        }

        return {
            success: true,
            blockData: data
        };
    } catch (error) {
        console.error('Error en insertarBloque:', error);
        return {
            success: false,
            error: error.message
        };
    }
}


export async function intercambiarBloques(noticiaId, bloque1Orden, bloque2Orden) {
    const response = await fetch(url+'intercambiar_bloques', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({
            noticia_id: noticiaId,
            bloque1_orden: bloque1Orden,
            bloque2_orden: bloque2Orden
        })
    });

    const data = await response.json();

    if (response.ok) {
        return true;
    } else {
        console.error(data.message);
        return false;
    }
}


export async function deleteBlock(noticiaId, bloqueId) {
    const response = await fetch(url+"borrar_bloque", {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            noticia_id: noticiaId,
            orden: bloqueId
        })
    });

    if (response.ok) {
        return true;
    } else {
        console.error("No se pudo eliminar el bloque en la Base de datos");
        return false
    }
}
