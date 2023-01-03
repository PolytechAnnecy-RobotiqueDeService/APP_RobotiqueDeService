<?php
$message = $_POST['message']; //la méthode Post pour récupérer le mssage du client

try {
  $socket = stream_socket_client("localhost:39039", $errno, $errstr, 30) or die("Could not create socket\n");   //Création du Socket
  $conec = "setname WebSend";
  $size = strlen($conec);
  fwrite($socket, pack("n", $size), 2) or die("Could not send data to server\n");
  fwrite($socket, $conec, $size) or die("Could not send data to server\n");
  fread($socket, 1024) or die("Could not read server response\n");
} catch(socket_connect $e){
  echo $e;
  echo "[Erreur] Timeout\nVérifier que le serveur est bien démarré et réessayer !";
  exit();
}

$size = strlen($message);
fwrite($socket, pack("n", $size), 2) or die("Could not send data to server\n");
fwrite($socket, $message, $size) or die("Could not send data to server\n");
$result =  fread($socket, 1024) or die("Could not read server response\n");
echo substr($result, 2, strlen($result));

$message= "disconnect";
$size = strlen($message);
fwrite($socket, pack("n", $size), 2) or die("Could not send data to server\n");
fwrite($socket, $message, $size) or die("Could not send data to server\n");

fclose($socket);
?>
