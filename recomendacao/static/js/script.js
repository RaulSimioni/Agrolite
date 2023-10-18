document.addEventListener('DOMContentLoaded', function () {
    document.querySelector("form").addEventListener("submit", function (event) {
        event.preventDefault();

        var formData = new FormData(this);
        fetch(this.action, {
            method: "POST",
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById("resultado").textContent = data.recomendacao;
            });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementById('botao');
    const botaoVoltar = document.getElementById('botao_voltar')
    const input1 = document.getElementById('N');
    const input2 = document.getElementById('P');
    const input3 = document.getElementById('K');
    const input4 = document.getElementById('Temperatura');
    const input5 = document.getElementById('Umidade');
    const input6 = document.getElementById('Ph');
    const input7 = document.getElementById('Chuva');
    const customPopup = document.getElementById('customPopup');
    const closePopupButton = document.getElementById('closePopup')

    input1.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '');
    });
    input2.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '');
    });
    input3.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '');
    });
    input4.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '');
    });
    input5.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '');
    });
    input6.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '');
    });
    input7.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '');
    });

    submitButton.addEventListener('click', function () {
        if (input1.value.trim() === '' || input2.value.trim() === '' || input3.value.trim() === '' || input4.value.trim() === '' || input5.value.trim() === '' || input6.value.trim() === '' || input7.value.trim() === '') {
            customPopup.style.display = 'block'
        } else {
            input1.style.display = 'none';
            input2.style.display = 'none';
            input3.style.display = 'none';
            input4.style.display = 'none';
            input5.style.display = 'none';
            input6.style.display = 'none';
            input7.style.display = 'none';
            submitButton.style.display = 'none';
            botaoVoltar.style.display = 'block';
        }
    });

    closePopupButton.addEventListener('click', function () {
        customPopup.style.display = 'none';
    });
});