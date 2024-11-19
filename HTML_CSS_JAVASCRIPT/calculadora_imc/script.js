const calcular = document.getElementById("calcular");

const imc = () => {
    const nome = document.getElementById("nome").value;
    const altura = document.getElementById("altura").value;
    const peso = document.getElementById("peso").value;
    const resultado = document.getElementById("resultado");

    if (nome != "" && altura != "" && peso != "") {
        const valorIMC = (peso / (altura * altura)).toFixed(1)

        let classificacao = "";

        if (valorIMC < 18.5) {
            classificacao = "Abaixo do peso"
        } else if (valorIMC < 25) {
            classificacao = "Com peso ideal. Parabens!!!"
        } else if (valorIMC < 30) {
            classificacao = "Levimente acima do peso."
        } else if (valorIMC < 35) {
            classificacao = "Com obisidade grau 1."
        } else if (valorIMC < 40) {
            classificacao = "Com obisidade grau 2."
        } else {
            classificacao = "Com obesidade grau 3, Cuidado!!!"
        }

        resultado.textContent = `${nome} seu IMC e ${valorIMC}e  voce esta ${classificacao}`
    } else {
        resultado.textContent = "Preencha os campos para obter o seu IMC!!!"
    }
}

calcular.addEventListener("click", imc)