const lamp = document.getElementById('lamp')
const turnOnOff = document.getElementById("turnOnOff")

function isLampBroken(){
    return lamp.src.indexOf('quebrada') > -1
}

function lampOn(){
    if(!isLampBroken()){
        lamp.src = "./img/ligada.jpg"
    }
}

function lampOff(){
    if(!isLampBroken()){
        lamp.src = "./img/desligada.jpg"
    }
}

function LampBroken(){
 lamp.src = "./img/quebrada.jpg"
}

function lampOnOff(){
    if(turnOnOff.textContent == "Ligar"){
        lampOn()
        turnOnOff.textContent = "Desligada"
    }else{
        lampOff()
        turnOnOff.textContent = 'Ligar'
    }
}

turnOnOff.addEventListener("click", lampOnOff)
lamp.addEventListener("mouseover", lampOn)
lamp.addEventListener("mouseleave", lampOff)
lamp.addEventListener("dblclick", LampBroken)