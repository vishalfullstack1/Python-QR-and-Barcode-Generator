import qrcode
data = input("Enter the your any profile URL: ")

# data = "https://www.instagram.com/vishalpandey_799/"

try:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("social.png")

except Exception as e:
    print("Something went wrong:", e)
else:
    print("QR code generated successfully and saved as 'social.png'")
