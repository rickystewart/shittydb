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

    public String get(String key) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(key));
	
		String o = "";
		String l;

		while ((l = br.readLine()) != null) {
			o += l;
			o += System.lineSeparator();
		}
		
		br.close();
		
		return o;
    }
}
