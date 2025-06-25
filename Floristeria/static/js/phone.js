document.addEventListener('DOMContentLoaded', function () {
    const input = document.querySelector("#phone_supplier");

    const iti = window.intlTelInput(input, {
        initialCountry: "ec",
        preferredCountries: ["ec", "us", "es", "mx"],
        separateDialCode: true,
        nationalMode: false,
        utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@17.0.12/build/js/utils.js"
    });

    const form = input.closest("form");

    form.addEventListener("submit", function (e) {
        const fullNumber = iti.getNumber();

        if (!iti.isValidNumber()) {
            e.preventDefault();
            alert("Número inválido. Ejemplo: +593991234567");
            console.log("Número ingresado inválido:", input.value);
        } else {
            e.preventDefault(); // Evita que se envíe antes de tiempo
            input.value = fullNumber; // Asignamos el número completo con +593
            console.log("Número válido (enviado):", input.value);
            form.submit(); // Enviamos manualmente
        }
    });
});