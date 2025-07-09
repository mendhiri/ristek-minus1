import json
import os

def load_hotels(filepath: str = "data/mock_hotels.json") -> list:
    """
    Memuat daftar hotel dari file JSON.
    """
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

def query_hotels(lokasi: str, harga_max: int) -> list:
    """
    Mengembalikan daftar hotel yang sesuai dengan lokasi dan harga maksimal.
    """
    hotels = load_hotels()
    hasil = [
        hotel for hotel in hotels
        if hotel.get("lokasi", "").lower() == lokasi.lower()
        and hotel.get("harga", 0) <= harga_max
    ]
    return hasil
