import { getSomeError } from "./limpiar_comentario.js";

// Desplazamiento al formulario
document
.getElementById("scroll-to-form")
.addEventListener("click", function () {
  const formulario = document.getElementById("formulario-comentario");
  formulario.scrollIntoView({ behavior: "smooth" });
});

// Mostrar/Ocultar Formulario de Respuesta
function mostrarRespuestaForm(comentarioId) {
const form = document.getElementById(`respuesta-form-${comentarioId}`);
if (form.style.display === "none") {
  form.style.display = "block";
} else {
  form.style.display = "none";
}
}

// Interacción con las estrellas
const stars = document.querySelectorAll(".star");
const estrellasInput = document.getElementById("id_estrellas");

stars.forEach((star) => {
star.addEventListener("click", () => {
  const value = star.getAttribute("data-value");
  estrellasInput.value = value;

  getSomeError();

  // Resaltar las estrellas seleccionadas
  stars.forEach((s, index) => {
    if (index < value) {
      s.classList.add("selected");
    } else {
      s.classList.remove("selected");
    }
  });
});

star.addEventListener("mouseover", () => {
  const value = star.getAttribute("data-value");
  stars.forEach((s, index) => {
    if (index < value) {
      s.style.color = "#ffc107"; // Amarillo para estrellas seleccionadas
    } else {
      s.style.color = "#ccc"; // Gris para estrellas no seleccionadas
    }
  });
});

star.addEventListener("mouseout", () => {
  stars.forEach((s, index) => {
    if (index < estrellasInput.value) {
      s.style.color = "#ffc107"; // Mantener amarillo para estrellas seleccionadas
    } else {
      s.style.color = "#ccc"; // Gris para estrellas no seleccionadas
    }
  });
});
});

// Obtener la URL actual de la página
const urlActual = window.location.href;
const tituloNoticia = "{{ noticia.titulo }}";
const imagenNoticia = "{{ noticia.imagen.url }}"; // Asegúrate de que `imagen` sea un campo válido en tu modelo

// Compartir en Facebook
function compartirFacebook(event) {
event.preventDefault();
const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(urlActual)}`;
window.open(facebookUrl, '_blank'); // Abre en una nueva pestaña
}

// Compartir en Twitter
function compartirTwitter(event) {
event.preventDefault();
const twitterUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(urlActual)}&text=${encodeURIComponent(tituloNoticia)}`;
window.open(twitterUrl, '_blank'); // Abre en una nueva pestaña
}

// Compartir en WhatsApp
function compartirWhatsApp(event) {
event.preventDefault();
const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(`${tituloNoticia} - ${urlActual}`)}`;
window.open(whatsappUrl, '_blank'); // Abre en una nueva pestaña
}

// Función para copiar el enlace al portapapeles
function copiarEnlace() {
const enlace = window.location.href;

navigator.clipboard.writeText(enlace).then(() => {
// Obtener el botón y sus elementos internos
const botonCopiar = document.getElementById('copiarEnlaceBtn');
const iconoCopiar = document.getElementById('iconoCopiar');
const textoCopiar = document.getElementById('textoCopiar');

// Agregar clase "copiado" para cambiar el estilo
botonCopiar.classList.add('copiado');

// Cambiar el ícono y el texto
iconoCopiar.classList.remove('fa-link');
iconoCopiar.classList.add('fa-check');
textoCopiar.textContent = 'Copiado';

// Restaurar el botón después de 2 segundos
setTimeout(() => {
  botonCopiar.classList.remove('copiado');
  iconoCopiar.classList.remove('fa-check');
  iconoCopiar.classList.add('fa-link');
  textoCopiar.textContent = 'Copiar Enlace';
}, 2000);
}).catch((error) => {
console.error("Error al copiar el enlace:", error);
});
}