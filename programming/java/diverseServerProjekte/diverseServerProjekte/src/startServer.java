public class startServer {
    public static void main(String[] args) {
        // BasisServer susi = new BasisServer(4711);
        // susi.permanenteVerbindungMitClient();

        // new basisServer(2000).permanenteVerbindungMitClient();
        // new halloServer(3000).permanenteVerbindungMitClient();
        // new echoServer(4000).permanenteVerbindungMitClient();
        // new dialogTestServer(4000).permanenteVerbindungMitClient();
        new textDateiServer(5000).permanenteVerbindungMitClient();
    }
}