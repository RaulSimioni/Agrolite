document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById("recomendacaoForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // Verificar se algum campo está em branco
        if (
            !isFieldFilled('#N') ||
            !isFieldFilled('#P') ||
            !isFieldFilled('#K') ||
            !isFieldFilled('#Temperatura') ||
            !isFieldFilled('#Umidade') ||
            !isFieldFilled('#Ph') ||
            !isFieldFilled('#Chuva')
        ) {
            // Mostrar o modal de aviso se algum campo estiver em branco
            $('#avisoModal').modal('show');
            return; // Impede o envio do formulário
        }
    
        

        const formData = new FormData(this);
        const modeloSelecionado = document.querySelector('#modelo').value;

        // Verificar se o modeloSelecionado é válido antes de enviar a solicitação
        if (modeloSelecionado) {
            formData.append('modelo', modeloSelecionado);

            fetch(this.action, {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Exibir o modal de resultado apenas se não houve nenhum erro
                if (!data.erro) {
                    // Atualizar o conteúdo do modal com o resultado
                    document.getElementById("resultadoTexto").textContent = data.recomendacao;

                    // Exibir o modal
                    $('#resultadoModal').modal('show');
                }
            })
            .catch(error => console.error('Erro ao obter dados:', error));
        } else {
            console.error("Modelo não selecionado ou inválido.");
        }
    });

    $('#avisoModal').on('hidden.bs.modal', function () {
        // Esconder o modal de resultado
        $('#resultadoModal').modal('hide');
    });

    // Limpar o conteúdo do modal ao fechar
    $('#avisoModal, #resultadoModal').on('hidden.bs.modal', function () {
        console.log('Modal sendo exibido.');

        form.reset();

        document.getElementById("resultadoTexto").textContent = '';
    });

    // Função para verificar se um campo está preenchido
    function isFieldFilled(selector) {
        return $.trim($(selector).val());
    }

    document.getElementById("N").addEventListener("input", function () {
        validateInput(this);
    });
    
    document.getElementById("P").addEventListener("input", function () {
        validateInput(this);
    });
    
    document.getElementById("K").addEventListener("input", function () {
        validateInput(this);
    });
    
    document.getElementById("Temperatura").addEventListener("input", function () {
        validateInput(this);
    });
    
    document.getElementById("Umidade").addEventListener("input", function () {
        validateInput(this);
    });
    
    document.getElementById("Ph").addEventListener("input", function () {
        validateInput(this);
    });
    
    document.getElementById("Chuva").addEventListener("input", function () {
        validateInput(this);
    });
    
    // Função para validar se o valor é um número inteiro
    function validateInput(input) {
        // Remove qualquer não número (exceto '-')
        input.value = input.value.replace(/[^0-9-]/g, '');
    }
});
