import qrcode

url = input("Input ur URL:").strip()
file_path = "C:\\Users\\User\\Documents\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated")