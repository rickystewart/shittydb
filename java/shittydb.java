import java.io.*;
import java.lang.*;

public class shittydb {
    public void set(String key, String value) throws IOException {
        FileWriter f = new FileWriter(key);
        try {
            f.append(value);
        } finally {
            f.close();
        }
    }

    public String get(String key) throws IOException, InterruptedException {
        Process p = Runtime.getRuntime().exec("cat " + key);
        p.waitFor();

        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        return reader.readLine();
    }
}
