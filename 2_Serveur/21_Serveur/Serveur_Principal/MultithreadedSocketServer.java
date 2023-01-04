 
import java.net.*;
public class MultithreadedSocketServer {
  public static void main(String[] args) throws Exception {
    try{
	  ServerSocket server=new ServerSocket(39039);
      System.out.println("Server Started ...");
      ListeRobot robot = new ListeRobot();
      SendString stringToSend = new SendString();
      Fenetre fenetre = new Fenetre(server, robot, stringToSend);
      stringToSend.addEcouteur(fenetre);
      while(true){
        Socket serverClient=server.accept();  //server accept the client connection request
        stringToSend.receiveMsg("[Connection] Connexion d'un client en cours");
        ServerClientThread sct = new ServerClientThread(serverClient, server, robot, stringToSend); //send  the request to a separate thread
        robot.addRobot(sct);
        sct.start();
      }
    }catch(Exception e){
      System.out.println(e);
    }
  }
  
  

  
  
}