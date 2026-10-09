import urllib.parse
from flask import Flask, Response, render_template_string

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
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Öğretmenime Hediye</title>
    
    <!-- PWA Meta Etiketleri -->
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#1e293b">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Öğretmenime Hediye">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
        }
    </script>
    <style>
        body { -webkit-tap-highlight-color: transparent; }
        summary::-webkit-details-marker { display: none; }
    </style>
</head>
<body class="p-3 sm:p-5 max-w-2xl mx-auto bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 transition-colors duration-200 antialiased">

    <!-- Header & Dark Mode Toggle -->
    <div class="flex justify-between items-center mb-4">
        <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-slate-800 dark:text-slate-100">Öğretmenime Hediye</h1>
        <button onclick="toggleDarkMode()" class="p-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 shadow-sm active:scale-95 transition">
            <span id="themeIcon">🌙</span>
        </button>
    </div>

    <!-- PWA Yükleme Bildirimi (Android) -->
    <div id="pwaBanner" class="hidden mb-4 p-3 bg-blue-500/10 border border-blue-500/30 rounded-xl flex justify-between items-center text-sm">
        <span class="text-blue-600 dark:text-blue-400 font-medium">Uygulama olarak yükle</span>
        <button id="pwaInstallBtn" class="bg-blue-600 text-white px-3 py-1.5 rounded-lg font-semibold text-xs active:scale-95">Yükle</button>
    </div>

    <!-- Katalog Formu -->
    <div class="bg-white dark:bg-slate-800 p-4 sm:p-6 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-700/60 mb-5">
        <form id="listForm" class="space-y-2.5">
            {% for kategori, urunler in katalog.items() %}
            <details class="border border-slate-200 dark:border-slate-700/80 rounded-xl bg-slate-50/50 dark:bg-slate-900/40 group overflow-hidden">
                <summary class="p-3.5 font-semibold text-slate-700 dark:text-slate-200 cursor-pointer select-none flex justify-between items-center">
                    <span class="text-sm sm:text-base">{{ kategori }}</span>
                    <span class="text-xs text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                </summary>
                <div class="p-3 pt-1 grid grid-cols-1 sm:grid-cols-2 gap-2 border-t border-slate-200/60 dark:border-slate-700/50">
                    {% for urun in urunler %}
                    <label class="flex items-center space-x-3 p-2.5 rounded-lg border border-slate-200/50 dark:border-slate-700/50 bg-white dark:bg-slate-800 cursor-pointer active:bg-blue-50 dark:active:bg-slate-700/50 transition">
                        <input type="checkbox" name="secilenler" value="{{ urun }}" class="w-5 h-5 rounded text-blue-600 focus:ring-0 cursor-pointer">
                        <span class="text-sm font-medium text-slate-600 dark:text-slate-300">{{ urun }}</span>
                    </label>
                    {% endfor %}
                </div>
            </details>
            {% endfor %}

            <button type="button" onclick="hazirla()" class="w-full mt-4 bg-blue-600 hover:bg-blue-700 active:scale-[0.98] text-white font-bold py-3.5 px-4 rounded-xl shadow-md shadow-blue-500/20 transition duration-150 text-base">
                📋 LİSTEYİ HAZIRLA
            </button>
        </form>
    </div>

    <!-- Önizleme ve WhatsApp Butonu -->
    <div class="bg-white dark:bg-slate-800 p-4 sm:p-6 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-700/60 space-y-4">
        <div>
            <label class="block font-semibold text-slate-700 dark:text-slate-300 mb-2 text-sm">Seçilen Ürünler</label>
            <textarea id="onizleme" rows="7" class="w-full p-3 border border-slate-200 dark:border-slate-700 rounded-xl bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 font-mono text-sm leading-relaxed focus:outline-none" readonly></textarea>
        </div>
        <div id="paylasContainer"></div>
    </div>

    <script>
        // --- DARK MODE MANTIĞI ---
        function applyTheme(isDark) {
            if (isDark) {
                document.documentElement.classList.add('dark');
                document.getElementById('themeIcon').textContent = '☀️';
            } else {
                document.documentElement.classList.remove('dark');
                document.getElementById('themeIcon').textContent = '🌙';
            }
        }

        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            applyTheme(savedTheme === 'dark');
        } else {
            applyTheme(window.matchMedia('(prefers-color-scheme: dark)').matches);
        }

        function toggleDarkMode() {
            const isDark = document.documentElement.classList.toggle('dark');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            document.getElementById('themeIcon').textContent = isDark ? '☀️' : '🌙';
        }

        // --- LİSTE HAZIRLAMA ---
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
                <div class="text-center mt-2">
                    <a href="https://wa.me/?text=${encoded}" target="_blank" 
                       class="inline-block w-full sm:w-auto px-8 py-3.5 bg-blue-600 hover:bg-blue-700 active:scale-[0.98] text-white font-bold rounded-xl shadow-lg shadow-blue-500/20 transition duration-150 text-base">
                        WHATSAPP İLE GÖNDER
                    </a>
                </div>
            `;
        }

        // --- PWA SERVICE WORKER & INSTALL PROMPT ---
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js');
        }

        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            const banner = document.getElementById('pwaBanner');
            if (banner) banner.classList.remove('hidden');
        });

        document.getElementById('pwaInstallBtn')?.addEventListener('click', () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then(() => {
                    deferredPrompt = null;
                    document.getElementById('pwaBanner').classList.add('hidden');
                });
            }
        });
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, katalog=katalog)

@app.route("/manifest.json")
def manifest():
    manifest_data = {
        "name": "Öğretmenime Hediye",
        "short_name": "Hediye",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0f172a",
        "theme_color": "#1e293b",
        "icons": [
            {
                "src": "https://cdn-icons-png.flaticon.com/512/3429/3429149.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            }
        ]
    }
    return Response(render_template_string("{{ data|tojson }}", data=manifest_data), mimetype="application/json")

@app.route("/sw.js")
def service_worker():
    sw_code = """
    self.addEventListener('install', (e) => {
        self.skipWaiting();
    });
    self.addEventListener('fetch', (e) => {
        e.respondWith(fetch(e.request));
    });
    """
    return Response(sw_code, mimetype="application/javascript")

if __name__ == "__main__":
    app.run(debug=True)
