import java.io.*;

public class textDateiServer extends basisServer {

    // spezielle Eigenschaften
    PrintWriter bleistift; // Bekomme ich vom Basisserver
                           // über die Methode schreibeAntwort
    String befehle = "Folgende Befehle sind moeglich: <dir> <logout>";

    // Spezielles Verhalten
    public void schreibeAntwort(PrintWriter bleistift) {
        this.bleistift = bleistift; // damit ist der Bleistift vom Basisserver gespeichert als Eigenschaft
        boolean weiter = true;
        while (weiter) {
            try {
                // checke den Befehl vom Client
                String[] leseZeile = höreFrageArray();
                System.out.println("Befehl vom Client: " + leseZeile[0]);

                // fallunterscheidung der einzelnen Befehle
                if (leseZeile[0].equals("logout")) { // über Client kam der Befehl Logout
                    weiter = false;
                }
                if (leseZeile[0].equals("dir")) { //
                
                else {
                    fehlermeldung();
                }
            } catch (Exception error) {
                System.out.println("Befehl vom Client: ... Fehler");
                fehlermeldung();
                weiter = true;
            }

        }

    }

    // spezielle Methoden
    void fehlermeldung() {
        System.out.println("Fehlermeldung");
        bleistift.println("\u001B[31mBefehl nicht Verstanden\u001B[0m");
        bleistift.println(befehle);
        bleistift.flush();
    }

    // Konstruktor
    public textDateiServer(int port) {
        super(port);
        System.out.println("Text Datei Server started on port " + port);
    }
}
