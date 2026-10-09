import urllib.parse
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

katalog = {
    "KAHVALTILIK & SÜT": [
        "Süt",
        "Yumurta",
        "Beyaz Peynir",
        "Kaşar Peyniri",
        "Zeytin (Siyah)",
        "Zeytin (Yeşil)",
        "Tereyağı",
        "Yoğurt",
        "Süzme Yoğurt",
        "Kaymak",
        "Bal",
        "Reçel",
        "Pekmez",
        "Tahin",
        "Sürülebilir Çikolata",
        "Salam",
        "Sucuk",
        "Sosis",
        "Pastırma",
        "Mısır Gevreği",
    ],
    "FIRIN & UNLU MAMÜL": [
        "Beyaz Ekmek",
        "Tam Buğday Ekmek",
        "Tost Ekmeği",
        "Lavaş",
        "Yufka",
        "Simit",
        "Poğaça",
        "Galeta",
        "Milföy Hamuru",
        "Mantı (Hazır)",
    ],
    "TAZE SEBZELER": [
        "Domates",
        "Salatalık",
        "Sivri Biber",
        "Dolmalık Biber",
        "Patlıcan",
        "Patates",
        "Kuru Soğan",
        "Taze Soğan",
        "Sarımsak",
        "Limon",
        "Maydonoz",
        "Dereotu",
        "Roka",
        "Marul",
        "Ispanak",
        "Taze Fasulye",
        "Kabak",
        "Mantar",
        "Havuç",
    ],
    "TAZE MEYVELER": [
        "Elma",
        "Muz",
        "Portakal",
        "Mandalina",
        "Çilek",
        "Karpuz",
        "Kavun",
        "Üzüm",
        "Erik",
        "Şeftali",
    ],
    "BAKLİYAT & MAKARNA": [
        "Pirinç",
        "Pilavlık Bulgur",
        "Köftelik Bulgur",
        "Kırmızı Mercimek",
        "Yeşil Mercimek",
        "Nohut",
        "Kuru Fasulye",
        "Un",
        "Mısır Unu",
        "İrmik",
        "Makarna (Çubuk)",
        "Makarna (Burgu)",
        "Arpa Şehriye",
        "Tel Şehriye",
    ],
    "YAĞ, SOS & SALÇA": [
        "Ayçiçek Yağı",
        "Zeytinyağı",
        "Mısır Yağı",
        "Domates Salçası",
        "Biber Salçası",
        "Ketçap",
        "Mayonez",
        "Nar Ekşisi",
        "Sirke",
        "Turşu",
        "Konserve Mısır",
        "Ton Balığı",
    ],
    "İÇECEKLER": [
        "Çay",
        "Türk Kahvesi",
        "Filtre Kahve",
        "Hazır Kahve",
        "Bitki Çayı",
        "Su (5L/19L)",
        "Maden Suyu",
        "Meyve Suyu",
        "Gazlı İçecek",
        "Ayran",
        "Şalgam Suyu",
    ],
    "ATIŞTIRMALIK": [
        "Tuzlu Bisküvi",
        "Tatlı Bisküvi",
        "Kraker",
        "Cips",
        "Çikolata",
        "Gofret",
        "Kek",
        "Karışık Kuruyemiş",
        "Çekirdek",
        "Leblebi",
    ],
    "ET & ŞARKÜTERİ": [
        "Dana Kıyma",
        "Kuşbaşı Et",
        "Antrikot/Biftek",
        "Bütün Tavuk",
        "Tavuk Göğsü",
        "Tavuk Baget",
        "Taze Balık",
    ],
    "MUTFAK TEMİZLİK": [
        "Bulaşık Deterjanı",
        "Bulaşık Makinesi Tableti",
        "Parlatıcı",
        "Makine Tuzu",
        "Yağ Çözücü",
        "Mutfak Spreyi",
        "Bulaşık Süngeri",
        "Çelik Tel",
        "Mutfak Bezi",
    ],
    "ÇAMAŞIR & BANYO": [
        "Çamaşır Deterjanı",
        "Yumuşatıcı",
        "Çamaşır Suyu",
        "Yüzey Temizleyici",
        "Kireç Çözücü",
        "Lavabo Açıcı",
        "Cam Suyu",
        "Arap Sabunu",
    ],
    "KAĞIT ÜRÜNLERİ": [
        "Tuvalet Kağıdı",
        "Kağıt Havlu",
        "Peçete",
        "Islak Mendil",
        "Çöp Torbası (Mutfak)",
        "Çöp Torbası (Büyük)",
    ],
    "KİŞİSEL BAKIM": [
        "Sabun (Katı)",
        "Sıvı Sabun",
        "Şampuan",
        "Saç Kremi",
        "Duş Jeli",
        "Diş Macunu",
        "Diş Fırçası",
        "Deodorant",
        "Pamuk",
        "Kulak Çubuğu",
    ],
    "BAHARATLAR": [
        "Tuz",
        "Karabiber",
        "Pul Biber",
        "Kekik",
        "Nane",
        "Kimyon",
        "Sumak",
        "Susam",
        "Tarçın",
        "Vanilya/Kabartma Tozu",
    ],
    "EV GENEL": [
        "Piller",
        "Ampul",
        "Alüminyum Folyo",
        "Streç Film",
        "Pişirme Kağıdı",
        "Kürdan",
        "Yara Bandı",
        "Kibrit/Çakmak",
    ],
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Öğretmenime Hediye</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    </style>
</head>
<body class="p-4 max-w-2xl mx-auto">
    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 mb-6">
        <h1 class="text-3xl font-bold text-slate-800 mb-4">Öğretmenime Hediye</h1>
        
        <form id="listForm" class="space-y-3">
            {% for kategori, urunler in katalog.items() %}
            <details class="border border-slate-200 rounded-lg p-3 bg-slate-50 group">
                <summary class="font-semibold text-slate-700 cursor-pointer list-none flex justify-between items-center">
                    <span>{{ kategori }}</span>
                    <span class="text-slate-400 group-open:rotate-180 transition-transform">▼</span>
                </summary>
                <div class="mt-3 grid grid-cols-2 gap-2 pt-2 border-t border-slate-200">
                    {% for urun in urunler %}
                    <label class="flex items-center space-x-2 text-sm text-slate-600 bg-white p-2 rounded border border-slate-100 cursor-pointer">
                        <input type="checkbox" name="secilenler" value="{{ urun }}" class="w-4 h-4 text-blue-600 rounded">
                        <span>{{ urun }}</span>
                    </label>
                    {% endfor %}
                </div>
            </details>
            {% endfor %}

            <button type="button" onclick="hazirla()" class="w-full mt-4 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-lg shadow transition duration-150">
                📋 LİSTEYİ HAZIRLA
            </button>
        </form>
    </div>

    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 space-y-4">
        <div>
            <label class="block font-semibold text-slate-700 mb-2">Seçilen Ürünler</label>
            <textarea id="onizleme" rows="8" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-slate-800 font-mono text-sm" readonly></textarea>
        </div>
        <div id="paylasContainer"></div>
    </div>

    <script>
        function hazirla() {
            const checked = Array.from(document.querySelectorAll('input[name="secilenler"]:checked')).map(cb => cb.value);
            const onizleme = document.getElementById('onizleme');
            const paylasContainer = document.getElementById('paylasContainer');

            if (checked.length === 0) {
                onizleme.value = "Henüz bir şey seçilmedi.";
                paylasContainer.innerHTML = "";
                return;
            }

            const mesaj = "Seçilen Ürün Listesi:\\n\\n" + checked.map(item => "• " + item).join("\\n");
            onizleme.value = mesaj;

            const encoded = encodeURIComponent(mesaj);
            paylasContainer.innerHTML = `
                <div class="text-center mt-4">
                    <a href="https://wa.me/?text=${encoded}" target="_blank" 
                       class="inline-block px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-full shadow-lg transition duration-150 text-lg">
                        WHATSAPP İLE GÖNDER
                    </a>
                </div>
            `;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, katalog=katalog)

if __name__ == "__main__":
    app.run(debug=True)
