function previewImage(event) {
    const input = event.target;
    const file = input.files[0];
    const preview = document.getElementById('preview');

    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };

        reader.readAsDataURL(file);
    } else {
        preview.src = '#';
        preview.style.display = 'none';
    }
}

function confirmDelete() {
    if (confirm("¿Estás seguro de que quieres eliminar esta empresa?")) {
        document.getElementById('delete-form').submit();
    }
}