from PIL import Image


CHAR_ARRAY = [' ', '.', ':', '*', '#', '@']
CHAR_ASPECT_RATIO = 1  

def image_to_ascii_colored(image: Image.Image, width_chars: int, height_chars: int):
    """
    Convert a PIL image to ASCII with color info.
    width_chars, height_chars = number of characters to fit in window
    Returns a list of lines each line is a list of (char, (r,g,b))
    """
    new_width = max(1, width_chars)
    new_height = max(1, int(height_chars * CHAR_ASPECT_RATIO))

    # Resize image and keep color
    image = image.resize((new_width, new_height)).convert("RGBA")
    pixels = list(image.getdata())

    ascii_frame = []
    for i in range(new_height):
        row = pixels[i * new_width:(i + 1) * new_width]
        row_chars = []
        for r, g, b , a in row:
            gray = int((r + g + b ) / 3)
            ch = CHAR_ARRAY[int(gray / 255 * (len(CHAR_ARRAY) - 1))]
            row_chars.append((ch, (r, g, b, a)))
        ascii_frame.append(row_chars)

    return ascii_frame
