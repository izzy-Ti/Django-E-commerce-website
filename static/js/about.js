const button= document.getElementById('button');
let text= document.getElementById('text');
button.addEventListener(`click`,function(){
    text.classList.toggle(`active`);
})