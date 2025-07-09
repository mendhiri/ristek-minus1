import streamlit as st
from models import prediksi_batal

def handle_user_input(user_input: str):
    stage = st.session_state.conversation_stage
    data = st.session_state.user_data

    if stage == "init":
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append((
            "agent", 
            "Halo! Saya adalah Asisten Pemesanan Hotel. Apa yang bisa saya bantu hari ini?"
        ))
        st.session_state.conversation_stage = "awaiting_request"

    elif stage == "awaiting_request":
        st.session_state.chat_history.append(("user", user_input))
        if "reservasi" in user_input.lower():
            st.session_state.chat_history.append((
                "agent", 
                "Baik, mohon isi data berikut dalam satu baris:\n**Nama, Lokasi Hotel, Tanggal (YYYY-MM-DD), Jumlah Malam, Harga Maksimum**"
            ))
            st.session_state.conversation_stage = "awaiting_data"
        else:
            st.session_state.chat_history.append((
                "agent", 
                "Saya bisa bantu melakukan reservasi hotel. Silakan beri tahu kebutuhannya."
            ))

    elif stage == "awaiting_data":
        st.session_state.chat_history.append(("user", user_input))
        try:
            nama, lokasi, tanggal, malam, harga = [i.strip() for i in user_input.split(",")]
            data.update({
                "nama": nama,
                "lokasi": lokasi,
                "tanggal": tanggal,
                "malam": int(malam),
                "harga": int(harga)
            })

            # Simulasi prediksi probabilitas pembatalan
            fitur = [1, 0, 3, int(malam), int(harga)]
            prob = prediksi_batal(fitur)

            if prob < 0.7:
                st.session_state.chat_history.append((
                    "agent", 
                    f"Reservasi Anda aman (probabilitas batal: {prob:.2f}). Menyimpan data ke database..."
                ))
                st.session_state.chat_history.append((
                    "agent", 
                    f"Reservasi berhasil untuk **{data['nama']}** di **{data['lokasi']}** tanggal **{data['tanggal']}** selama **{data['malam']} malam**."
                ))
                st.session_state.chat_history.append(("agent", "Terima kasih telah menggunakan layanan kami."))
                st.session_state.conversation_stage = "done"
            else:
                st.session_state.chat_history.append((
                    "agent", 
                    f"Ada kemungkinan tinggi Anda akan membatalkan reservasi ini (probabilitas: {prob:.2f})."
                ))
                st.session_state.chat_history.append((
                    "agent", 
                    "Kami sarankan beberapa opsi berikut:\n1. **Penawaran Bundle dengan Tanggal Baru**\n2. **Transfer Nama / Alih Tamu**\n3. **Ubah Jadwal (Reschedule)**\n\nSilakan pilih salah satu."
                ))
                st.session_state.conversation_stage = "rescue_options"

        except Exception:
            st.session_state.chat_history.append((
                "agent", 
                "Format tidak dikenali. Mohon isi dengan format:\n**Nama, Lokasi Hotel, Tanggal (YYYY-MM-DD), Jumlah Malam, Harga Maksimum**"
            ))

    elif stage == "rescue_options":
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append((
            "agent", 
            f"Baik, kami akan proses opsi **{user_input}**. Terima kasih atas pengertiannya."
        ))
        st.session_state.conversation_stage = "done"

    elif stage == "done":
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append((
            "agent", 
            "Silakan mulai percakapan baru jika ingin melakukan reservasi lainnya."
        ))
