public class startServer {
    public static void main(String[] args) {
        // BasisServer susi = new BasisServer(4711);
        // susi.permanenteVerbindungMitClient();

        // new basisServer(2000).permanenteVerbindungMitClient();
        // new halloServer(3000).permanenteVerbindungMitClient();
        // new echoServer(4000).permanenteVerbindungMitClient();
        // new dialogTestServer(4000).permanenteVerbindungMitClient();
        // new textDateiServer(5000).permanenteVerbindungMitClient();

        Thread thread1 = new Thread(new halloServer(2000));
        Thread thread2 = new Thread(new echoServer(3000));
        Thread thread3 = new Thread(new dialogTestServer(4000));
        Thread thread4 = new Thread(new textDateiServer(5000));
        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();

    }
}