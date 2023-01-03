import java.util.ArrayList;

public class ListeRobot {
	ArrayList<ServerClientThread> robot = new ArrayList<ServerClientThread>();
	public ListeRobot() {
	}
	public ArrayList<ServerClientThread> getRobot() {
		return robot;
	}
	public void addRobot(ServerClientThread robot) {
		this.robot.add(robot);
	}
	public void delRobot(ServerClientThread robot) {
		this.robot.remove(robot);
	}

}
