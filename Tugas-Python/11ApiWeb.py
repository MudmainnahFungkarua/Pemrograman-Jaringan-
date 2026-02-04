import requests

# =========================
# Fungsi Cuaca
# =========================
def get_weather(city_name, lat, lon):
    print(f"\n--- Mengambil Data Cuaca untuk {city_name} ---")
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': lat,
        'longitude': lon,
        'current_weather': 'true',
        'timezone': 'auto'
    }

    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()
        current = data.get('current_weather')

        if current:
            suhu = current.get('temperature', 'N/A')
            kecepatan_angin = current.get('windspeed', 'N/A')
            print(f"🌡️  Suhu Saat Ini: {suhu}°C")
            print(f"💨 Kecepatan Angin: {kecepatan_angin} km/h")
            print(f"🌍 Koordinat: {lat}, {lon}")
        else:
            print("[ERROR] Data cuaca tidak tersedia.")

    except requests.exceptions.ConnectionError:
        print("[ERROR] Tidak ada koneksi internet! Tidak bisa mengambil data cuaca.")
    except requests.exceptions.Timeout:
        print("[ERROR] Request API cuaca timeout!")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")


# =========================
# Fungsi Random Quote (Online + Offline)
# =========================
def random_quote():
    print("\n--- Menampilkan Kata Mutiara Hari Ini ---")
    url = "https://api.quotable.io/random"
    default_quote = '"Hidup adalah perjalanan, nikmati setiap langkahnya." — Albert Einstein'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        quote = data.get("content", "Tidak ada quote")
        author = data.get("author", "Unknown")

        print(f'💬 "{quote}" — {author}')

    except requests.exceptions.RequestException:
        # Internet mati / timeout / API error → tampil quote default
        print(f'💬 {default_quote}')


# =========================
# Main Program
# =========================
if __name__ == "__main__":
    # 1. Cuaca
    get_weather("Jakarta", -6.2088, 106.8456)
    get_weather("Makassar", -5.1477, 119.4327)

    # 2. Random Quote (online/offline)
    random_quote()
