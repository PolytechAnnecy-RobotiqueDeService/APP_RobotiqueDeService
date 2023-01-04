 
import java.net.*;
import java.io.*;
public class ClientServer {
  public ClientServer(String msg, SendString stringToSend) {
  try{
	String clientMessage=msg,serverMessage="";
	Socket socket= new Socket("127.0.0.1",39039);
    DataInputStream inStream=new DataInputStream(socket.getInputStream());
    DataOutputStream outStream=new DataOutputStream(socket.getOutputStream());
    outStream.writeUTF("setname ClientServer");
    outStream.flush();
    serverMessage=inStream.readUTF();
    
    outStream.writeUTF(clientMessage);
    outStream.flush();
    serverMessage=inStream.readUTF();
    stringToSend.receiveMsg(serverMessage);
    
    
    outStream.close();
    socket.close();
  }catch(Exception e){
    System.out.println(e);
  }
  }
}
