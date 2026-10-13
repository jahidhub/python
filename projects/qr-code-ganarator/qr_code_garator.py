import qrcode

data = input("Enter the text and url: ").strip()
file_name = input("Enter the file name: ").strip()

# Automatically add .png if the user forgot it
if not file_name.endswith((".png", ".jpg", ".jpeg")):
    file_name += ".png"

qr = qrcode.QRCode(
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)  # Compiles the data to fit the code size

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_name)

print(f"QR saved as {file_name}")