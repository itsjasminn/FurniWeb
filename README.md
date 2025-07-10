# 🪑 FurniWeb – Zamonaviy Mebel Boshqaruvi

# 🇺🇿 O‘zbekcha

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

---

3. Superuser yaratish (admin panel uchun):

```bash
python manage.py createsuperuser
```

---

# ✅ Asosiy Funksiyalar

**🪑 Mebel mahsulotlarini yaratish, tahrirlash va ko‘rish**

**🛒 Buyurtmalar tizimi**

**👤 Foydalanuvchi autentifikatsiyasi**

**📷 Mahsulot rasmlarini yuklash**

**🧾 Django admin orqali to‘liq boshqaruv**

---

# 📈 Kelajakdagi Rejalar

**📱 REST API qo‘shish (mobil ilovalar uchun)**

**💳 To‘lov integratsiyasi (Stripe, Payme, Click)**

**🧍‍♂️ Foydalanuvchi profilingi va hisob sozlamalari**

**📱 Responsive dizaynni yanada takomillashtirish**

--- 

# 👩‍💻 Muallif

**Made with 🧡 by Jasmina Ochildiyeva**

[🔗 GitHub Profilim](https://github.com/itsjasminn)
[📂 FurniWeb Repository](https://github.com/itsjasminn/FurniWeb)

---

# 🇬🇧 English

**FurniWeb** — is a web application that allows users to view, order, and manage furniture products online.  
Built with Django, this project helps digitize your furniture business through a powerful admin panel and optional REST
API support.


---

## 🎯 Purpose

To create a furniture catalog system that stands out for its simplicity and allows users to manage products and orders
efficiently.  
The project focuses on **minimalism**, **speed**, and **user-friendliness**.

---

## 🧱 Architecture

### 📁 Project Folder Structure:


FurniWeb/
├── furni/ # Main Django app (products, orders, users)

├── root/ # Django settings and URLs

├── templates/ # HTML templates

├── static/ # Static files (CSS, JS, images)

├── media/ # Uploaded product images

├── manage.py # Django management file

├── requirements.txt # List of dependencies

└── README.md # Project documentation

---

## 🚀 Technologies Used


| Technology                  | Purpose                            |
|-----------------------------|------------------------------------|
| Python 3.11+                | Main programming language          |
| Django 5.x                  | Web application framework          |
| PostgreSQL / SQLite         | Database                           |
| Django Admin                | Management interface               |
| Bootstrap 5                 | UI design and responsiveness       |
| Pillow                      | Image handling                     |
| Django Rest Framework (DRF) | API endpoints (optional)           |


---

## ⚙️ Getting Started

### 1. Requirements

- Python 3.11+
- `virtualenv` or `poetry`
- PostgreSQL (recommended) or SQLite (for testing)

### 2. Installation

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

---

3. Superuser yaratish (admin panel uchun):

```bash
python manage.py createsuperuser
```

---

# ✅ Key Features

**🪑 Create, edit, and view furniture products**

**🛒 Order management system**

**👤 User authentication system**

**📷 Upload product images**

**🧾Full management via Django admin**

---

# 📈 Future Plans

**📱 Add REST API support (for mobile apps)**

**💳 Integrate payment systems (Stripe, Payme, Click)**

**🧍‍♂️ User profiles and account settings**

**📱 Further improvements in responsive design**

--- 

# 👩‍💻 Author

**Made with 🧡 by Jasmina Ochildiyeva**

[🔗 My GitHub profile](https://github.com/itsjasminn)

[📂 FurniWeb Repository](https://github.com/itsjasminn/FurniWeb)



