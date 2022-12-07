import java.io.*;

//Test Dialog mit dem Client
// Lehmann Janneck 6/12/2022

public class dialogTestServer extends basisServer {
    // spezielles Verhalten
    public void schreibeAntwort(PrintWriter bleistift) {

        boolean weiter = true;
        while (weiter) {
            // checke den Befehl vom Client
            String[] leseZeile = höreFrageArray();
            System.out.println("Befehl vom Client: " + leseZeile[0]);
            if (leseZeile[0].equals("logout")) // über Client kam der Befehl Logout
                weiter = false;
        }

    }

    // Konstruktor
    public dialogTestServer(int port) {
        super(port);
        System.out.println("Dialog Test Server started on port " + port);
    }

}
