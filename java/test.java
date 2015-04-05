import java.io.*;
import java.lang.*;

public class test {
    public static void main(String[] args) throws IOException, InterruptedException {
        shittydb db = new shittydb();
        db.set("foo", "this is really proper");
        System.out.println(db.get("foo"));
    }
}