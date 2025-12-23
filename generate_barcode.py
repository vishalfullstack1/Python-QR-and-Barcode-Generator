from barcode import Code128
from barcode.writer import ImageWriter

try:
    address = "Noida 201301, India"

    # Generate Code128 barcode
    code = Code128(address, writer=ImageWriter())
    filename = code.save("address_barcode")

    print(f"✅ Barcode generated and saved as '{filename}.png'")

except Exception as e:
    print("❌ Error:", e)
