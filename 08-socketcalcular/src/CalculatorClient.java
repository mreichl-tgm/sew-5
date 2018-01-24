import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class CalculatorClient {
	private String ip;
	private int port;

	public CalculatorClient(String ip, int port) {
		this.ip = ip;
		this.port = port;
	}

	public void connect() {
		try (Socket socket = new Socket(ip, port);
				PrintWriter out = new PrintWriter(socket.getOutputStream(),
						true);
				BufferedReader in = new BufferedReader(new InputStreamReader(
						socket.getInputStream()));
				BufferedReader userInputReader = new BufferedReader(
						new InputStreamReader(System.in));) {
			String msg;
			while ((msg = userInputReader.readLine()) != null) {
				out.println(msg);
				String answer = in.readLine();
				System.out.println("Server: " + answer);
				if (answer == null || answer.equals("Bye!"))
					break;
			}
		} catch (UnknownHostException e) {
			System.err.println("Host not found!");
			System.exit(1);
		} catch (IOException e) {
			System.err.println("Couldn't get I/O!");
			System.exit(1);
		} catch (Exception e) {
			System.err.println("Error!");
			System.exit(1);
		}
	}

	public static void main(String[] args) {
		CalculatorClient client = new CalculatorClient("127.0.0.1", 12345);
		client.connect();
	}

}
