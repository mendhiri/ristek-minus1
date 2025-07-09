import random

def prediksi_batal(fitur_user: list) -> float:
    """
    Mock fungsi prediksi pembatalan hotel.
    Return: probabilitas (float) antara 0 dan 1
    """
    # Simulasi probabilitas berbasis panjang fitur
    if len(fitur_user) % 2 == 0:
        return round(random.uniform(0.3, 0.6), 2)
    else:
        return round(random.uniform(0.7, 0.95), 2)



"""
import joblib
model = joblib.load("models/Hotel_Booking_Cancel.pkl")
def prediksi_batal(fitur_user):
    return model.predict_proba([fitur_user])[0][1]  
"""