// JavaScript Document
const btnStart=document.getElementById('btnStart');
const accion=document.getElementById('accion');
const video=document.getElementById('video');
let recognition = new webkitSpeechRecognition();
recognition.continuous=false;
recognition.interimResults=true;
recognition.onresult=(event)=>{
	const results=event.results;
	const text = results[results.length -1][0].transcript;
	accion.value =text;
	recognition.addEventListener("result",ejecutar(text));
	
}
function ejecutar(texto) {
	// body...alert(texto)
		
		switch(texto) {
		  case "play":
			// code block
			video.autoplay = true;
			video.load();
			break;
		  case "stop":
			// code block
			video.autoplay = false;
			video.load();
			break;
		  default:
			// code block
		}
	}
btnStart.addEventListener('click',()=>{
	recognition.start();
});
btnStop.addEventListener('click',()=>{
	recognition.abort();
});




