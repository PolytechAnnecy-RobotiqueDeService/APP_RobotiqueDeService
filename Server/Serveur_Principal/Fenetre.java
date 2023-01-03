import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.ServerSocket;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

@SuppressWarnings("serial")
public class Fenetre extends JFrame implements ActionListener, ReceiveEvent {

	
	private JPanel pan = new JPanel();
	
	private JPanel sendBlock = new JPanel();
	private JTextField command = new JTextField("", 20);
	private JButton sendButton = new JButton("Send");
	
	
	private JPanel buttonBlock = new JPanel();
	private JButton stopButton = new JButton("Stop");
	
	
	private JPanel container = new JPanel();
	
	
	private JTextArea log = new JTextArea(20,60);

	private SendString stringToSend;
	private ServerSocket server;

	
    public void KeyInput(JTextField command){ //or JTextField
        this.command = command;
    }
	
	public Fenetre(ServerSocket server, ListeRobot robot, SendString stringToSend) {

		this.server = server;
		this.stringToSend = stringToSend;
		this.setTitle("Server");
	    this.setSize(800, 450);
	    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    this.setLocationRelativeTo(null);

	    sendBlock.add(command);
	    sendBlock.add(sendButton);
	    
	    buttonBlock.add(stopButton);
	    
	    stopButton.addActionListener(this);
	    stopButton.setActionCommand("stop");
	    sendButton.addActionListener(this);
	    sendButton.setActionCommand("send");
	   
	    this.getRootPane().setDefaultButton(sendButton);
	    log.append("Log du serveur:\n");
	    log.setEditable(false);
	    JScrollPane scroller = new JScrollPane(log, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);

	    
	    pan.add(container);
	    container.add(scroller, BorderLayout.CENTER);
	    container.add(sendBlock, BorderLayout.SOUTH);
	    container.add(buttonBlock, BorderLayout.SOUTH);
	    this.setContentPane(container);
	    this.setVisible(true);
		
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getActionCommand().equals("send")) {
			if(!command.getText().equals("")){
				@SuppressWarnings("unused")
				ClientServer client = new ClientServer(command.getText(), stringToSend);
				command.selectAll();
				command.replaceSelection("");	
			}
		}
		if(e.getActionCommand().equals("stop")) {
			try {
				server.close();
			} catch (IOException e1) {
				e1.printStackTrace();
			}
			this.dispose();
		}
		
	}

	@Override
	public void transferMsg(String msg) {
		Date now = new Date();
		String format2 = new SimpleDateFormat("HH:mm:ss", Locale.FRENCH).format(now);
		log.append("[" + format2 + "]" + msg + "\n");
		log.setCaretPosition(log.getDocument().getLength());
	}

}
