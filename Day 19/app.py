from PIL import Image

# Function to convert an image to ASCII art
def image_to_ascii(image_path, output_width=100, output_file=None):
    # Define ASCII characters based on intensity (dark to light)
    ASCII_CHARS = "@%#*+=-:. "

    # Open the image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return

    # Resize the image while maintaining aspect ratio
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * output_width * 0.55)  # Adjust for font aspect ratio
    resized_image = image.resize((output_width, new_height))

    # Convert the image to grayscale
    grayscale_image = resized_image.convert("L")

    # Map each pixel to an ASCII character
    pixels = grayscale_image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    ascii_str_len = len(ascii_str)
    ascii_art = "\n".join([ascii_str[index:index + output_width] for index in range(0, ascii_str_len, output_width)])

    # Print or save the ASCII art
    if output_file:
        with open(output_file, "w") as f:
            f.write(ascii_art)
        print(f"ASCII art saved to {output_file}")
    else:
        print(ascii_art)

# Main program
if __name__ == "__main__":
    # Input image path
    image_path = input("Enter the path to the image file: ")

    # Output width (number of characters per line)
    output_width = int(input("Enter the output width (e.g., 100): "))

    # Save to file or print to console
    save_option = input("Do you want to save the ASCII art to a file? (y/n): ").lower()
    output_file = None
    if save_option == "y":
        output_file = input("Enter the output file name (e.g., ascii_art.txt): ")

    # Convert the image to ASCII art
    image_to_ascii(image_path, output_width, output_file)