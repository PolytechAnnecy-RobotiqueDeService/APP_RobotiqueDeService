import java.util.ArrayList;

public class SendString {
	ArrayList<ReceiveEvent> ecouteur = new ArrayList<ReceiveEvent>();
	public SendString() {
	}
	
	public void receiveMsg(String msg) {
		for(ReceiveEvent e: ecouteur) {
			e.transferMsg(msg);
		}
	}
	public void addEcouteur(ReceiveEvent e) {
		ecouteur.add(e);
	}
	
}
