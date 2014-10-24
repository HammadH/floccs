var socket = io.connect("/event_chat");

socket.on('connect', function(){
	$('#chat').append('connected');
	socket.emit('join',window.event_room_id);
	

});