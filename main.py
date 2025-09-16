import streamlit as st
import qrcode
from io import BytesIO

st.title("AI in Agriculture by Nikita Gagare and Mrunali Shirtar")

video_url = "https://drive.google.com/file/d/1hAWpAJixTVswgC0rQQ5UcQU_C3Qag1V8/view?usp=sharing"

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(video_url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

buf = BytesIO()
img.save(buf, format="PNG")
byte_im = buf.getvalue()

st.image(byte_im, caption="Scan to open video")
st.success("QR Code generated!")
