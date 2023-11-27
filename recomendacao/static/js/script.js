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
                } else {
                    // Se houver um erro, exibir o modal de aviso com a mensagem de erro
                    $('#avisoModal').find('.modal-body').text(data.erro);
                    $('#avisoModal').modal('show');
                }
            })
            .catch(error => console.error('Erro ao obter dados:', error));
        } else {
            console.error("Modelo não selecionado ou inválido.");
        }
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
});
