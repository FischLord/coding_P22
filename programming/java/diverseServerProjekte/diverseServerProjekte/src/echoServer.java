// LS 10 Teste die Vererbung
// Lehmann Janneck 6/12/2022

import java.io.*;

public class echoServer extends basisServer {

    public void schreibeAntwort(PrintWriter bleistift) {
        bleistift.println("");
        bleistift.println("Sie hatten geschrieben: " + "\u001B[31m" + höreFrage());
        bleistift.flush();
    }

    public echoServer(int port) {
        super(port);
        System.out.println("Echo Server started on port " + port);
    }
}
