document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('company-form');
    if (!form) return;

    const fileInput = document.getElementById('file');
    const preview = document.getElementById('preview');
    const errorDiv = document.getElementById('error-msg');

    const isEdit = form.dataset.isEdit === "true";

    // Previsualización de imagen
    if (fileInput) {
        fileInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            } else {
                preview.style.display = 'none';
            }
        });
    }

    // Validación al enviar el formulario
    form.addEventListener('submit', function(e) {
        errorDiv.innerHTML = '';
        if (!isEdit && (!fileInput || !fileInput.files.length)) {
            e.preventDefault();
            errorDiv.innerHTML = '<p>Por favor selecciona una imagen.</p>';
        }
    });
});