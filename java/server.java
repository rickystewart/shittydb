import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class server {
    public static void main(String[] args) throws IOException {
        ServerSocket ss = new ServerSocket(10984);
        shittydb shittydb = new shittydb();
        while (true) {
            try {
                Socket s = ss.accept();
                InputStream i = s.getInputStream();
                OutputStream o = s.getOutputStream();
                o.write("HTTP/1.1 200 OK\n\n".getBytes());
                BufferedReader v = new BufferedReader(new InputStreamReader(i));
                String[] r = v.readLine().split(" ");
                r[1] = r[1].split("/")[1];
                if (r[0].equals("GET")) {
                    o.write(shittydb.get(r[1]).getBytes());
                } else {
                    do {
                        r[0] = v.readLine().trim();
                    } while (!r[0].isEmpty());
                    r[0] = "";
                    while (v.ready()) {
                        r[0] = r[0] + (char) v.read();
                    }
                    shittydb.set(r[1], r[0]);
                }

                o.close();
                i.close();
            } catch (Throwable e) {
                // handles exceptions in the cloud
            }
        }
    }
}