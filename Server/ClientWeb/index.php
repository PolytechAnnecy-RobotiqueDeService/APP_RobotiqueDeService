<!DOCTYPE html>
<html>
<head>
</head>
<body>

	<form name="ContactForm" method="post" action="">
		<label for="message">Message:</label><br />
		<input type="text" name="message" id="message"><br />
	</div>
	<button type="submit" class="btn btn-default">Send</button>
</form>

<div class="message_box" style="margin:10px 0px;">
</div>

<script src="https://code.jquery.com/jquery-3.6.3.min.js"></script>
<script>
function launchReceive(){
	$.ajax({
		url: "receiveClient.php",
		success: function(data)
		{

			setTimeout(function() {
				$('#logServerReceive').append(data.concat("\n"));
				$('#reponse').html(data);
				refreshReponse();
				launchReceive();
				document.getElementById("logServerReceive").scrollTop = document.getElementById("logServerReceive").scrollHeight
			}, delay);
		}

	});
}


var delay = 200;
$(document).ready(function() {
	$.ajax({
		url: "receiveClient.php",
		success: function(data)
		{

			setTimeout(function() {
				$('#logServerReceive').append(data.concat("\n"));
				$('#reponse').html(data);
				refreshReponse();
				launchReceive();
				document.getElementById("logServerReceive").scrollTop = document.getElementById("logServerReceive").scrollHeight
			}, delay);
		}

	});


	$('.btn-default').click(function(e){
		e.preventDefault();
		var message = $('#message').val();
		if(message == ''){
			$('.message_box').html(
				'<span style="color:red;">Merci d\'entrer une commande !</span>'
			);
			$('#message').focus();
			return false;
		}
		$('#logServer').append(">".concat(message,"\n"));
		$.ajax
		({
			type: "POST",
			url: "sendClient.php",
			data: "message="+message,
			beforeSend: function() {
				$('.message_box').html(
					'<img src="Loader.gif" width="25" height="25"/>'
				);
			},
			success: function(data)
			{

				setTimeout(function() {
					$('#message').val("");
					$('.message_box').html("");
					$('#logServer').append(data.concat("\n"));
					document.getElementById("logServer").scrollTop = document.getElementById("logServer").scrollHeight
				}, delay);
			}
		});

	});

});

</script>
<h1>Messages envoyés</h1>
<textarea  style="resize:none;" rows="15" cols="150" name="logServer" id="logServer" disabled></textarea>
<h1>Messages reçus</h1>
<textarea  style="resize:none;" rows="15" cols="150" name="logServerReceive" id="logServerReceive" disabled></textarea>


</body>
</html>
