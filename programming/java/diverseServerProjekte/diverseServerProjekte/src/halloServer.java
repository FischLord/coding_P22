// LS 10 Teste die Vererbung
// Lehmann Janneck 6/12/2022 

import java.io.*;

public class halloServer extends basisServer {
    // Spetielle eigenschaften
    // Spezielles Verhalten.... Spezielle methoden
    // Überschreibe die Methode des BasisServers

    String[] hallos = {
            "Sprache: English --> Welcome!",
            "Sprache: Afrikaans --> hallo",
            "Sprache: Albanian --> Përshëndetje",
            "Sprache: Amharic --> ሰላም",
            "Sprache: Arabic --> مرحبا",
            "Sprache: Armenian --> Բարեւ",
            "Sprache: Azerbaijani --> Salam",
            "Sprache: Basque --> Kaixo",
            "Sprache: Belarusian --> добры дзень",
            "Sprache: Bengali --> হ্যালো",
            "Sprache: Bosnian --> zdravo",
            "Sprache: Bulgarian --> Здравейте",
            "Sprache: Catalan --> Hola",
            "Sprache: Cebuano --> Hello",
            "Sprache: Chichewa --> Moni",
            "Sprache: Chinese (Simplified) --> 您好",
            "Sprache: Chinese (Traditional) --> 您好",
            "Sprache: Corsican --> Bonghjornu",
            "Sprache: Croatian --> zdravo",
            "Sprache: Czech --> Ahoj",
            "Sprache: Danish --> Hej",
            "Sprache: Dutch --> Hallo",
            "Sprache: English --> Hello",
            "Sprache: Esperanto --> Saluton",
            "Sprache: Estonian --> Tere",
            "Sprache: Filipino --> Kumusta",
            "Sprache: Finnish --> Hei",
            "Sprache: French --> Bonjour",
            "Sprache: Frisian --> Hello",
            "Sprache: Galician --> Ola",
            "Sprache: Georgian --> გამარჯობა",
            "Sprache: German --> Hallo",
            "Sprache: Greek --> Γεια σας",
            "Sprache: Gujarati --> હેલો",
            "Sprache: Haitian Creole --> Bonjou",
            "Sprache: Hausa --> Sannu",
            "Sprache: Hawaiian --> Alohaʻoe",
            "Sprache: Hebrew --> שלום",
            "Sprache: Hindi --> नमस्ते",
            "Sprache: Hmong --> Nyob zoo",
            "Sprache: Hungarian --> Helló",
            "Sprache: Icelandic --> Halló",
            "Sprache: Igbo --> Ndewo",
            "Sprache: Indonesian --> Halo",
            "Sprache: Irish --> Dia duit",
            "Sprache: Italian --> Ciao",
            "Sprache: Japanese --> こんにちは",
            "Sprache: Javanese --> Hello",
            "Sprache: Kannada --> ಹಲೋ",
            "Sprache: Kazakh --> Сәлем",
            "Sprache: Khmer --> ជំរាបសួរ",
            "Sprache: Korean --> 안녕하세요.",
            "Sprache: Kurdish (Kurmanji) --> Hello",
            "Sprache: Kyrgyz --> салам",
            "Sprache: Lao --> ສະບາຍດີ",
            "Sprache: Latin --> salve",
            "Sprache: Latvian --> Labdien!",
            "Sprache: Lithuanian --> Sveiki",
            "Sprache: Luxembourgish --> Moien",
            "Sprache: Macedonian --> Здраво",
            "Sprache: Malagasy --> Hello",
            "Sprache: Malay --> Hello",
            "Sprache: Malayalam --> ഹലോ",
            "Sprache: Maltese --> Hello",
            "Sprache: Maori --> Hiha",
            "Sprache: Marathi --> हॅलो",
            "Sprache: Mongolian --> Сайн байна уу",
            "Sprache: Myanmar (Burmese) --> မင်္ဂလာပါ",
            "Sprache: Nepali --> नमस्ते",
            "Sprache: Norwegian --> Hallo",
            "Sprache: Pashto --> سلام",
            "Sprache: Persian --> سلام",
            "Sprache: Polish --> Cześć",
            "Sprache: Portuguese --> Olá",
            "Sprache: Punjabi --> ਹੈਲੋ",
            "Sprache: Romanian --> Alo",
            "Sprache: Russian --> привет",
            "Sprache: Samoan --> Talofa",
            "Sprache: Scots Gaelic --> Hello",
            "Sprache: Serbian --> Здраво",
            "Sprache: Sesotho --> Hello",
            "Sprache: Shona --> Hello",
            "Sprache: Sindhi --> هيلو",
            "Sprache: Sinhala --> හෙලෝ",
            "Sprache: Slovak --> ahoj",
            "Sprache: Slovenian --> Pozdravljeni",
            "Sprache: Somali --> Hello",
            "Sprache: Spanish --> Hola",
            "Sprache: Sundanese --> halo",
            "Sprache: Swahili --> Sawa",
            "Sprache: Swedish --> Hallå",
            "Sprache: Tajik --> Салом",
            "Sprache: Tamil --> ஹலோ",
            "Sprache: Telugu --> హలో",
            "Sprache: Thai --> สวัสดี",
            "Sprache: Turkish --> Merhaba",
            "Sprache: Ukranian --> Здрастуйте",
            "Sprache: Urdu --> ہیلو",
            "Sprache: Uzbek --> Salom",
            "Sprache: Vietnamese --> Xin chào",
            "Sprache: Welsh --> Helo",
            "Sprache: Xhosa --> Sawubona",
            "Sprache: Yiddish --> העלא",
            "Sprache: Yoruba --> Kaabo",
            "Sprache: Zulu --> Sawubona"
    };

    @Override
    public void schreibeAntwort(PrintWriter bleistift) {
        bleistift.println("");
        bleistift.println("--> " + hallos[(int) (Math.random() * hallos.length - 1)]);
        bleistift.flush();
    }

    // Konstruktor
    public halloServer(int port) {
        super(port);
        System.out.println("Hallo Server started on port " + port);
    }

}
