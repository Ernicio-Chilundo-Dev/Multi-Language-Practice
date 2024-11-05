const img =document.getElementById("img");
const buttons = document.getElementById("buttons");

let colorIndex = 0
let intervalId = 0

function trafficLights(event){
    stopAutomatc();
    turnOn[event.target.value]()
}

const nextIndex= ()=> colorIndex = colorIndex < 2? ++colorIndex : 0

const chancecolor = ()=>{
    const colors = ["red","yellow","green"]
    const color = colors[colorIndex]
    turnOn[color]()
    nextIndex()
}

const stopAutomatc = ()=>{
    clearInterval(intervalId)
}

const turnOn = {
    "red": ()=> img.src = "./img/vermelho.png",
    "yellow": ()=> img.src = "./img/amarelo.png",
    "green": ()=> img.src = "./img/verde.png",
    "automatic": ()=> intervalId = setInterval(chancecolor, 1000)
}

buttons.addEventListener("click", trafficLights)