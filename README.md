# waf-bypass-learning
## bypass-haha.py

**bypass-haha.py** adalah *script Proof of Concept (PoC)* yang dibuat untuk **pembelajaran dan demonstrasi konsep evasion/bypass secara dasar** pada keamanan aplikasi web.

Script ini **tidak dirancang sebagai alat eksploitasi**, **tidak menjamin keberhasilan bypass**, dan **tidak memiliki logika serangan nyata**. Fungsinya terbatas pada **simulasi pengiriman payload yang dimodifikasi** untuk membantu memahami bagaimana *filter sederhana* atau *validasi input yang lemah* dapat diuji.

Script ini lebih tepat diposisikan sebagai:

* **alat belajar**
* **contoh riset awal**
* **media diskusi defensive security**

---

## Tujuan Pembuatan

Script ini dibuat dengan tujuan:

* Mempelajari **konsep dasar evasion**, bukan bypass tingkat lanjut
* Menguji **filter input sederhana** (keyword / regex dasar)
* Memberi gambaran kepada **developer & blue team** tentang pola input tidak normal
* Media pembelajaran **pentesting legal, defensive security, dan threat modeling awal**

Script ini **bukan representasi serangan dunia nyata yang lengkap**, melainkan **contoh minimal** untuk memahami ide dasarnya.

---

## ⚠️ Peringatan Etika & Legal

❗ **Gunakan script ini HANYA untuk:**

* Website milik sendiri
* Lab pentest (DVWA, Juice Shop, dsb)
* Bug bounty (sesuai scope)
* Pembelajaran & riset keamanan

❌ **DILARANG digunakan untuk:**

* Menyerang website tanpa izin
* Mencuri data
* Merusak sistem pihak lain

Penggunaan di luar izin dapat melanggar hukum.

---

## Konsep Utama yang Digunakan

Script ini mendemonstrasikan **konsep dasar** yang sering dibahas dalam keamanan aplikasi web:

| Konsep             | Catatan Penting                               |
| ------------------ | --------------------------------------------- |
| Obfuscation        | Bersifat sederhana dan acak                   |
| Encoding           | Hanya efektif jika backend melakukan decoding |
| Fragmentasi        | Tidak menjamin payload akan digabung kembali  |
| Header Spoofing    | Sangat dasar dan mudah dideteksi              |
| Low-volume request | Bukan *true low & slow attack*                |

⚠️ Semua teknik di atas **bersifat demonstratif**, bukan implementasi evasion tingkat lanjut.

------|------------|
| Obfuscation | Mengaburkan payload agar lolos filter |
| Encoding | Menyembunyikan payload dari deteksi pola |
| Fragmentasi | Memecah payload jadi beberapa request |
| Header Spoofing | Menyamar sebagai browser normal |
| Low & Slow | Menghindari deteksi berbasis threshold |

---

## Komponen Script & Fungsinya

### 1️⃣ Payload Uji (SQL Injection)

```sql
SELECT * FROM users WHERE username='admin'--
```

Digunakan sebagai **contoh payload berbahaya** untuk pengujian filter input.

---

### 2️⃣ Obfuscation Payload

```python
def obfuscate_payload(s):
```

Payload dimodifikasi dengan menyisipkan komentar SQL `/**/` secara acak.

 **Tujuan:**

* Menghindari deteksi keyword seperti `SELECT`
* Menguji kemampuan parser SQL backend

---

### 3️⃣ Encoding Berlapis (Base64 + URL Encode)

```python
def encode_payload(s):
```

Payload di-*encode* agar tidak terlihat sebagai SQL query.

 **Tujuan:**

* Bypass regex filter
* Menguji apakah backend melakukan decoding berbahaya

---

### 4️⃣ Fragmentasi Payload

```python
def fragment_payload(s, n=5):
```

Payload dipecah menjadi beberapa bagian kecil.

 **Tujuan:**

* Menguji apakah sistem menggabungkan input
* Mensimulasikan HTTP parameter pollution

---

### 5️⃣ Header Spoofing

```http
User-Agent: Chrome
Referer: legitimate-site.com
```

Menyamarkan request agar terlihat seperti user normal.

 **Tujuan:**

* Bypass bot detection
* Bypass firewall sederhana

---

### 6️⃣ Pengiriman Bertahap

```python
for frag in payload_fragments:
```

Setiap fragmen dikirim sebagai request terpisah.

 **Tujuan:**

* Menghindari rate limit
* Mensimulasikan serangan *low & slow*

---

## Relevansi dalam Cyber Security

Script ini relevan sebagai **alat pembelajaran**, bukan sebagai senjata.

Yang bisa dipelajari:

* Bagaimana payload dapat dimodifikasi bentuknya
* Kenapa **blacklist dan regex sederhana tidak cukup**
* Pentingnya normalisasi input di backend
* Pentingnya prepared statement dan ORM

Yang **tidak** dilakukan script ini:

* Tidak melakukan exploit nyata
* Tidak memastikan keberhasilan serangan
* Tidak membaca atau mencuri data

---

## Catatan Akhir

**bypass-haha.py** adalah:

> Script edukasi untuk memahami *konsep awal evasion* dan bagaimana sistem seharusnya bersikap terhadap input tidak normal.

Script ini **tidak cukup** untuk menembus sistem yang dirancang dengan baik, dan **tidak dimaksudkan** untuk digunakan di luar konteks pembelajaran, lab, atau pengujian berizin.

---

## Disclaimer‼️

Script ini disediakan **untuk tujuan edukasi dan pembelajaran**.

Penulis **tidak mendorong dan tidak bertanggung jawab** atas penggunaan di luar konteks:

* pembelajaran
* pengujian berizin
* riset keamanan

Setiap penyalahgunaan merupakan tanggung jawab penuh pengguna.

