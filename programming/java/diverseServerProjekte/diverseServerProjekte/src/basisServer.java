// LS 9
// Lehman Janneck 06/12/2022

import java.net.*;
import java.io.*;

public class basisServer {
    // die Eigenschaften -----------------------------
    // damit ist es jeweils (mindestens) eine Agregation
    // private --- Stichwort Datenkapselung
    private ServerSocket serverDose;
    private BufferedReader vomClient; // die Ohren zum Hören
    private PrintWriter zumClient; // der Bleistift zum Schreiben
    private int port;
    // ! der Konstruktor -------------------------------

    basisServer(int port) { // ########################
        this.port = port;
        try {
            serverDose = new ServerSocket(port);
        } catch (IOException e) {
            System.out.println("Server konnte am Port " + port + " nicht eingerichtet werden");
        }
        System.out.println("Server läuft am Port " + port);

        // System.out.println("Server wartet am Port " + port + "auf Anfragen");
    }
    // ! die Methoden ----------------------------------

    void verbindungMitClient() {
        try {
            // todo warte auf Client-Anfragen... und warte... und warte...
            System.out.println("Server wartet am Port " + port + " auf Anfragen");
            Socket clientDose = serverDose.accept(); // methode Accept ist Blockierend
            System.out.println("Verbindung mit Client hergestellt" + clientDose.getInetAddress().getHostAddress());

            // todo vomClient = ... -> die Ohren
            vomClient = new BufferedReader(new InputStreamReader(clientDose.getInputStream()));

            // todo zumClient = ... -> der Bleistift
            zumClient = new PrintWriter(clientDose.getOutputStream());
            zumClient.print(">> ");
            zumClient.flush();

            // todo schreibe Info zum Client und schicke mit flush los
            schreibeAntwort(zumClient);

            // todo Verbindung schließen
            clientDose.close();

        } catch (Exception e) {
            System.out.println("Fehler in der Kommunikation mit dem Client");
        }

    }

    void permanenteVerbindungMitClient() { // als Endlosschleife
        while (true) {
            verbindungMitClient();
        }
    }

    /**
     * Wird durch die einzelnen Server überschrieben - der "eigentliche" Job. <br/>
     * Beachte: als abstrakte M. hier nicht möglich, da in verbindungMitClient()
     * benutzt.
     * 
     * @param zumClient Der Bleistift des basisServers ist gekapselt (private)
     */
    public void schreibeAntwort(PrintWriter zumClient) {
        zumClient.println("");
        zumClient.println("BasisServer --> ");
        zumClient.flush();
    };

    /**
     * Unterschiedliches Verhalten beim Schreiben, aber gleiches
     * Verhalten beim Hören -> deshalb beim basisServer implementiert
     * 
     * @return Die vom Client gesendete Zeile als String
     */
    public String höreFrage() {
        try { // zeilenweises Schreiben/Lesen, wie es zB von telnet praktiziert
            return vomClient.readLine();
        } catch (Exception ex) {
            System.out.println("Sorry - Ohren verstopft...");
            return ""; // Rückgabewert bei verstopften Ohren
        }
    }

    /**
     * Die vom Client gesendete Zeile wird an den Leerzeichen gesplittet (getrennt)
     * 
     * @return Die vom Client gesendete Zeile als Array mit Strings
     */
    public String[] höreFrageArray() { // z.B. 'zeige test.txt' oder 'nutze notenDB':
        return höreFrage().split(" ");
    }
}
