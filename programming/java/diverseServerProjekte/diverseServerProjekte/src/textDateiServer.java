import java.io.*;

public class textDateiServer extends basisServer {

    // spezielle Eigenschaften
    PrintWriter bleistift; // Bekomme ich vom Basisserver
                           // über die Methode schreibeAntwort
    String befehle = "Für eine Liste der Befehle geben Sie 'help' ein";
    String aktuellesVerzeichnis = "C:\\home\\repos\\coding_P22\\programming\\java\\diverseServerProjekte\\diverseServerProjekte";

    // Spezielles Verhalten
    public void schreibeAntwort(PrintWriter bleistift) {
        this.bleistift = bleistift; // damit ist der Bleistift vom Basisserver gespeichert als Eigenschaft
        boolean weiter = true;
        while (weiter) {
            bleistift.println(aktuellesVerzeichnis);
            bleistift.flush();
            try {
                // checke den Befehl vom Client
                String[] leseZeile = höreFrageArray();
                System.out.println("Befehl vom Client: " + leseZeile[0]);

                // fallunterscheidung der einzelnen Befehle
                if (leseZeile[0].equals("logout")) { // über Client kam der Befehl Logout
                    weiter = false;
                } else if (leseZeile[0].equals("cd")) {
                    System.out.println("Parameter vom Client: " + leseZeile[1]);
                    changeDirectory(leseZeile[1]);
                } else if (leseZeile[0].equals("dir")) {
                    zeigeInhalOrdner();
                } else if (leseZeile[0].equals("zeige")) {
                    zeigeInhaltDatei(leseZeile[1]);
                } else if (leseZeile[0].equals("help")) {
                    help();
                } else {
                    fehlermeldung();
                }
            } catch (Exception error) {
                System.out.println("Befehl vom Client: ... Fehler");
                // fehlermeldung();
                error.printStackTrace();
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

    void changeDirectory(String name) {
        File neuesVerzeichnis = new File(aktuellesVerzeichnis + "\\" + name);
        if (neuesVerzeichnis.isDirectory()) {
            aktuellesVerzeichnis = aktuellesVerzeichnis + "\\" + name;
            bleistift.println("\033[0;32mVerzeichnis gewechselt\u001B[0m");
            bleistift.flush();
        } else {
            bleistift.println("\033[0;31mVerzeichnis nicht gefunden\u001B[0m");
            bleistift.flush();
        }
    }

    void zeigeInhalOrdner() {
        File verzeichnis = new File(aktuellesVerzeichnis);
        System.out.println("Verzeichnis: " + verzeichnis.getPath());
        if (verzeichnis.isDirectory()) {
            System.out.println("in der if Funktion");
            String[] verzeichnisInhalt = verzeichnis.list();
            for (int i = 0; i < verzeichnisInhalt.length; i++) {
                bleistift.println("\033[0;33m  > " + verzeichnisInhalt[i] + "\033[0m");
            }
            bleistift.flush();
        } else {
            System.out.println("in der else Funktion");
        }
    }

    void zeigeInhaltDatei(String name) {
    }

    void help() {
        bleistift.println("_________________  \033[1;32mBefehle\u001B[0m  _________________");
        bleistift.println("\u001B[33mdir\u001B[0m - Zeigt den Inhalt des aktuellen Verzeichnisses an");
        bleistift.println(
                "\u001B[33mcd\u001B[0m \033[0;34m[Verzeichnisname]\033[0m - Wechselt das aktuelle Verzeichnis");
        bleistift.println("\u001B[33mzeige\u001B[0m \033[0;34m[Dateiname]\033[0m - Zeigt den Inhalt der Datei an");
        bleistift.println("\u001B[33mlogout\u001B[0m - Beendet die Verbindung zum Server");
        bleistift.println("\u001B[33mhelp\u001B[0m - Zeigt diese Hilfe an");
        bleistift.flush();
    }

}
