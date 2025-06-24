document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.image-upload-form').forEach(form => {
        const fileInput = form.querySelector('.file-input');
        const preview = form.querySelector('.preview');
        const errorDiv = form.querySelector('.error-msg');
        const isEdit = form.dataset.isEdit === "true";

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

        form.addEventListener('submit', function(e) {
            errorDiv.innerHTML = '';
            if (!isEdit && (!fileInput || !fileInput.files.length)) {
                e.preventDefault();
                errorDiv.innerHTML = '<p>Por favor selecciona una imagen.</p>';
            }
        });
    });
});
