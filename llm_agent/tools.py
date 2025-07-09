from langchain.tools import tool
from agent.hotel_query import query_hotels
from models import prediksi_batal
import json

reservasi_mock_db = []

@tool
def tool_query_hotel(input_str: str) -> str:
    """
    Cari hotel berdasarkan lokasi dan harga maksimum. Format input: "lokasi, harga_maks".
    Contoh: "Jakarta, 500000"
    """
    try:
        lokasi, harga = input_str.split(",")
        hasil = query_hotels(lokasi.strip(), int(harga.strip()))
        return json.dumps(hasil, indent=2)
    except Exception as e:
        return f"Format input tidak valid. Gunakan: 'Jakarta, 500000'. Error: {str(e)}"

@tool
def tool_prediksi_batal(input_str: str) -> float:
    """
    Prediksi probabilitas pembatalan berdasarkan fitur numerik. Format: "malam, harga"
    Contoh: "3, 500000"
    """
    try:
        malam, harga = map(int, input_str.split(","))
        fitur = [1, 0, 3, malam, harga]  # fitur dummy
        return prediksi_batal(fitur)
    except:
        return 0.5

@tool
def tool_simpan_reservasi(data: dict) -> str:
    """Menyimpan data reservasi ke memori (mock DB)."""
    reservasi_mock_db.append(data)
    return "Reservasi berhasil disimpan."
