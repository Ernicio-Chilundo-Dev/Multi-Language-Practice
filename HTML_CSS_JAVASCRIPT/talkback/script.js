// Funcao para simular a fala "talkback" usado API de sintese fala
function falarTexto(texto){
    const sintese = new SpeechSynthesisUtterance(texto);
    window.speechSynthesis.speak(sintese)
}

// Feedback de acessibilidade do botao
document.getElementById("button-example").addEventListener("click",()=>{
    const mensagem = "Voce clico no botao de exemplo";
    document.getElementById("feedback").innerText = mensagem;//Exibir feedback visual
    falarTexto(mensagem);
})

// Detecta quando o usuario termina de digitar
document.getElementById("input-example").addEventListener("input", (event)=>{
    const mensagem = `Voce digitou: ${event.target.value}`;
    document.getElementById("feedback").innerText = mensagem;//Exibir feedback visual
    falarTexto(mensagem);
})