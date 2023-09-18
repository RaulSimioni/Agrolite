function enviarDados() {
    // Coletar os valores dos campos de entrada
    const n = document.getElementById("n").value;
    const p = document.getElementById("p").value;
    const k = document.getElementById("k").value;
    const temp = document.getElementById("Temperatura").value;
    const umidade = document.getElementById("Umidade").value;
    const ph = document.getElementById("Ph").value;
    // Coletar outros valores dos campos de entrada, se necessário
  
    // Criar um objeto com os dados coletados
    const dadosSolo = {
      n: n,
      p: p,
      k: k,
      temp: temp,
      umidade: umidade,
      ph: ph
    };
  
    // Enviar os dados para o backend usando uma solicitação HTTP
    fetch("/recomendation.py", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dadosSolo),
    })
      .then((response) => response.json())
      .then((data) => {
        // Lidar com a resposta do backend, que pode conter a recomendação
        // Exibir a recomendação no frontend, se necessário
      })
      .catch((error) => {
        console.error("Erro ao enviar dados para o backend:", error);
      });
  }