var socket = io();

socket.on('connect', function()
{
	console.log('connection established !')
});

function send()
{
	var inputbox = document.getElementById('inputbox')
	socket.emit('message', inputbox.value)
	inputbox.value = ''
}

socket.on('push', function(data)
{
	var msgbox = document.getElementById('msgbox')
	msgbox.innerHTML += data + "<br/>"
})

