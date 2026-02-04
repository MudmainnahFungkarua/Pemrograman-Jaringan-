import requests

def rupiah_ke_usd(jumlah_rp):
    try:
        response = requests.get("https://api.exchangerate.host/latest", params={"base": "IDR", "symbols": "USD"})
        response.raise_for_status()  # cek status HTTP
        data = response.json()
        rate = data['rates']['USD']
        usd = jumlah_rp * rate
        print(f"Rp {jumlah_rp:,} = ${usd:.2f} USD (kurs real-time)")
    except requests.exceptions.RequestException as e:
        print("Gagal mengakses API kurs mata uang.")
        print("Pastikan koneksi internet aktif.")
    except KeyError:
        print("Data kurs tidak ditemukan di respons API.")

# Contoh pemakaian
rupiah_ke_usd(1000000)
