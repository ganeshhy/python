import qrcode as qr
from PIL import Image

# Create a QR code instance
qr_code = qr.QRCode(  # Use 'qr' since that's the alias you used when importing
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,  # Corrected spelling and value
    box_size=10,
    border=4
)

# Add data to the QR code
qr_code.add_data("https://github.com/ganeshhy")  # Fixed URL format with 'https://'
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="blue")

# Save the image
img.save("image1.png")
