import sys
import os
from PIL import Image, ImageSequence

INPUT_FILE = "../badderbaby.gif"
OUTPUT_FILE = "videoout-64x48x8.dat"
WIDTH = 64
HEIGHT = 48

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        sys.exit(1)

    try:
        img = Image.open(INPUT_FILE)
    except Exception as e:
        print(f"Error opening GIF: {e}")
        sys.exit(1)

    frames_data = []
    for i, frame in enumerate(ImageSequence.Iterator(img)):
        frame = frame.convert("RGB").convert("L")
        frame = frame.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
        frames_data.append(list(frame.getdata()))

    print(f"Processed {len(frames_data)} frames from {INPUT_FILE}.")

    with open(OUTPUT_FILE, "wb") as f:
        header = f"{WIDTH} {HEIGHT}\n".encode('ascii')
        f.write(header)
        
        for frame_pixels in frames_data:
            f.write(bytes(frame_pixels))

    print(f"Successfully wrote {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

