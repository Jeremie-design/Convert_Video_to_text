import os
import cv2
import pygame
from PIL import Image
import yt_dlp
from asciiConverter import image_to_ascii_colored  

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FONT_SIZE = 10
CHAR_ASPECT_RATIO = 1  

BLACK = (60, 60, 60)



#  DOWNLOAD VIDEO 
url = input("Paste the video link here: ").strip()

output_folder = "Video_Downloaded"
os.makedirs(output_folder, exist_ok=True)

ydl_opts = {
    "format": "worst[ext=mp4]/worst",
    "outtmpl": os.path.join(output_folder,"%(title)s.%(ext)s"),
    "quiet": True,
    "noplaylist" : True
    
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    video_path = ydl.prepare_filename(info)

print("Downloaded:", video_path)

# PYGAME 
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise RuntimeError("Failed to open video file")

fps = cap.get(cv2.CAP_PROP_FPS) or 24
frame_delay = 1 / fps

pygame.init()
FONT = pygame.font.SysFont("Courier", FONT_SIZE)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("ASCII Video Player (Color, Fixed Size)")

# number of characters in the window
chars_per_row = WINDOW_WIDTH // FONT_SIZE
chars_per_col = WINDOW_HEIGHT // FONT_SIZE

running = True

# PLAY VIDEO 
while running:
    ret, frame = cap.read()
    if not ret:
        break  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Convert frame to PIL
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    pil_image = Image.fromarray(frame)

    # Convert to ASCII (colored) scaled to fit window
    ascii_frame = image_to_ascii_colored(pil_image, chars_per_row, chars_per_col)

    # Draw ASCII in Pygame
    screen.fill(BLACK)
    for i, row in enumerate(ascii_frame):
        for j, (char, color) in enumerate(row):
            text_surface = FONT.render(char, True, color)
            screen.blit(text_surface, (j * FONT_SIZE, i * FONT_SIZE))

    pygame.display.flip()
    pygame.time.delay(int(frame_delay * 1000))

cap.release()
pygame.quit()
print("Playback finished.")
