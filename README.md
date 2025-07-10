# 🪑 FurniWeb – Zamonaviy Mebel Boshqaruvi

**FurniWeb** — bu mebel mahsulotlarini onlayn tarzda ko‘rish, buyurtma berish va boshqarish imkonini beruvchi web
ilova.  
Django asosida qurilgan ushbu loyiha REST API (opsional) va admin interfeys orqali mebel biznesingizni raqamlashtirishga
yordam beradi.

---

## 🎯 Maqsad

Foydalanuvchilar uchun soddaligi bilan ajralib turuvchi, mahsulotlar va buyurtmalarni boshqarish imkonini beruvchi mebel
katalogi yaratish.  
Loyihaning asosiy e’tibori — **minimalizm**, **tezkorlik** va **foydalanuvchi uchun qulaylik**.

---

## 🧱 Arxitektura

### 📁 Loyihaning papka tuzilmasi:

FurniWeb/
├── furni/ # Asosiy Django app (mahsulotlar, buyurtmalar, foydalanuvchilar)
├── root/ # Django sozlamalari (settings, urls)
├── templates/ # HTML shablonlar
├── static/ # Statik fayllar (CSS, JS, rasm)
├── media/ # Yuklangan rasm fayllari
├── manage.py # Django boshqaruv fayli
├── requirements.txt# Kutubxonalar ro‘yxati
└── README.md # Loyihaga oid hujjat


---

## 🚀 Ishlatilgan Texnologiyalar

| Texnologiya                 | Maqsadi                       |
|-----------------------------|-------------------------------|
| Python 3.11+                | Asosiy dasturlash tili        |
| Django 5.x                  | Web ilova framework           |
| PostgreSQL / SQLite         | Ma'lumotlar bazasi            |
| Django Admin                | Tizimni boshqarish interfeysi |
| Bootstrap 5                 | UI dizayn va responsivelik    |
| Pillow                      | Rasm fayllar bilan ishlash    |
| Django Rest Framework (DRF) | API endpointlar (opsional)    |

---

## ⚙️ Ishga tushirish

### 1. Talablar

- Python 3.11+
- `virtualenv` yoki `poetry`
- PostgreSQL (asosiy) yoki SQLite (test rejimi)

### 2. O‘rnatish

```bash
git clone https://github.com/itsjasminn/FurniWeb.git
cd FurniWeb
```

```
python3 -m venv .venv
source .venv/bin/activate
```

```
pip install -r requirements.txt
```

```
python manage.py migrate
python manage.py runserver
```

3. Superuser yaratish (admin panel uchun):

```bash
python manage.py createsuperuser
```

**✅ Asosiy Funksiyalar**

# 🪑 Mebel mahsulotlarini yaratish, tahrirlash va ko‘rish

# 🛒 Buyurtmalar tizimi

# 👤 Foydalanuvchi autentifikatsiyasi

# 📷 Mahsulot rasmlarini yuklash

# 🧾 Django admin orqali to‘liq boshqaruv

**📈 Kelajakdagi Rejalar**

# 📱 REST API qo‘shish (mobil ilovalar uchun)

# 💳 To‘lov integratsiyasi (Stripe, Payme, Click)

# 🧍‍♂️ Foydalanuvchi profilingi va hisob sozlamalari

# 📱 Responsive dizaynni yanada takomillashtirish


