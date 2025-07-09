from langchain_core.prompts import PromptTemplate

recommendation_template = PromptTemplate.from_template(
    """
Berikut adalah daftar hotel yang tersedia:

{hotel_list}

Berdasarkan preferensi pengguna, pilih hotel terbaik yang direkomendasikan.
Untuk setiap hotel, evaluasi apakah layak diterima atau tidak, dan berikan alasannya.

Output harus dalam format JSON dengan struktur seperti ini:

{{
  "rekomendasi": [
    {{
      "nama": "Hotel Mawar",
      "harga": 450000,
      "diterima": true,
      "alasan": "Harga terjangkau dan rating tinggi"
    }},
    ...
  ]
}}
"""
)
