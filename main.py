# Import QRCode from pyqrcode
import pyqrcode
import png

# String that should be converted to QR
s = input("Enter the value to be made QR code")

# Generate QR code
qr_Code = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
qr_Code.png('myqr.png', scale=6)
