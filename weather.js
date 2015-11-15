$(document).ready(function() {
	console.log('hey');

function weather(){
	$.get("http://127.0.0.1:5000/get_weather", function(data){
		var t = data['temp'];
		var d = data['desc'];
		var l = data['low'];
		var h = data['high'];
		$('#tempp').text(t+'\xB0'+'F');
		$('#descc').text(d);
		$('#low').text('Low: '+l+'\xB0');
		$('#high').text('High: '+h+'\xB0');
	});
};

function fadeIn(){ $("#text").fadeIn();}

function fadeOut(){ $("#text").fadeOut();}

setInterval(fadeOut, 1000*5);
weather();
setInterval(weather,1000*60*5);
});

			