
document.addEventListener("DOMContentLoaded", function() {
    console.log("La página ha sido cargada completamente.");
    
    //alerta de mensaje enviado
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            alert("Mensaje enviado!");
        });
    }
});
