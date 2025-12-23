import qrcode

upi_id = "kdesraj373-1@okaxis"
amount = "150.00"
note = "Payment for services"

upi_url = f"upi://pay?pa={upi_id}&pn=Vishal%20Pandey&am={amount}&tn={note}"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

try:
    qr.add_data(upi_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("payment_qr.png")

    print("✅ Payment QR code generated and saved as 'payment_qr.png'")
except Exception as e:
    print("❌ Failed to generate QR code:", e)
# This script generates a UPI payment QR code and saves it as an image file.
