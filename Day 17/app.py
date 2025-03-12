import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size around the QR code
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")

# Take input from the user
input_data = input("Enter the text, URL, or message to generate a QR code: ")

# Generate and save the QR code
generate_qr_code(input_data)