import urllib.parse
import gradio as gr

# Her şeyin olduğu dev liste
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


def liste_olustur(*secilenler):
    toplam_liste = []
    for s in secilenler:
        if isinstance(s, list) and len(s) > 0:
            toplam_liste.extend(s)

    if not toplam_liste:
        return "Henüz bir şey seçilmedi.", ""

    mesaj = "Seçilen Ürün Listesi:\n\n" + "\n".join(
        [f"• {item}" for item in toplam_liste]
    )
    whatsapp_link = f"https://wa.me/?text={urllib.parse.quote(mesaj)}"

    paylas_html = f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="{whatsapp_link}" target="_blank"
                style="padding: 18px 30px; background-color: #1976d2; color: white;
                text-decoration: none; border-radius: 50px; font-weight: bold; display: inline-block; font-size: 18px; box-shadow: 0 4px 15px rgba(25,118,210,0.3);">
                WHATSAPP İLE GÖNDER
            </a>
        </div>
    """
    return mesaj, paylas_html


custom_theme = gr.themes.Soft(primary_hue="blue").set(
    button_primary_background_fill="#1976d2",
    button_primary_background_fill_hover="#1565c0",
)

with gr.Blocks(theme=custom_theme, title="Öğretmenime Hediye") as demo:
    gr.Markdown("# Öğretmenime Hediye")

    input_listeleri = []
    for kategori, urunler in katalog.items():
        with gr.Accordion(label=kategori, open=False):
            cb = gr.CheckboxGroup(choices=urunler, label=None)
            input_listeleri.append(cb)

    btn = gr.Button("📋 LİSTEYİ HAZIRLA", variant="primary")

    with gr.Column():
        onizleme = gr.Textbox(label="Seçilen Ürünler", lines=8)
        paylas_html = gr.HTML()

    btn.click(
        fn=liste_olustur, inputs=input_listeleri, outputs=[onizleme, paylas_html]
    )

# Vercel Serverless entegrasyonu
app = demo.app

if __name__ == "__main__":
    demo.launch()
