# Badderbaby Project

This project adapts an existing highly optimized video compression framework to process a new input, `badderbaby.gif`, focusing solely on generating a compressed GIF output without audio. The original framework was designed for extreme compression of the "Bad Apple!!" video for deployment on resource-constrained microcontrollers.

![Badderbaby Compressed GIF](docs/images/video-64x48x8.gif)  

## Project Overview and Techniques

This project leverages sophisticated compression techniques, originally developed for the "Bad Apple!!" demoscene, to achieve a highly efficient representation of video data suitable for extremely resource-constrained devices. Key techniques utilized include:

*   **Block-based Encoding**: Video frames are broken down into 8x8 pixel blocks (tiles).
*   **K-Means Clustering**: Used to identify a limited set of unique "glyphs" (block patterns) that best represent the video content, minimizing visual quality loss.
*   **Run-Length Encoding (RLE)**: Identifies consecutive identical data points to replace them with a single data point and a count, reducing redundancy.
*   **Huffman Coding**: A variable-length coding algorithm used to assign shorter codes to more frequent symbols (glyphs or run lengths), further reducing the bitstream size.
*   **VPX (Range) Coding**: A form of arithmetic coding that approaches theoretical entropy limits by efficiently encoding symbols based on their probabilities, yielding superior compression ratios for the data stream.

The goal of these techniques is to minimize the output size while maintaining recognizable visual quality, making it suitable for hardware with very limited flash and RAM.

## Changes for the "Badderbaby" Compression

To compress the `badderbaby.gif` using this codebase, the following modifications were implemented:

1.  **Input Source Redirection**:
    *   References to the original "Bad Apple!!" video (`badapple-sm8628149.mp4`) across `comp/Makefile`, `comp2/Makefile`, and `ml/Makefile` were updated to point to `badderbaby.gif`.
    *   The `ml/Makefile` was configured to copy `badderbaby.gif` to `"Touhou - Bad Apple.mp4"` for compatibility with existing Python machine learning scripts that expected this specific filename.

2.  **GIF to Raw Frame Data Conversion**:
    *   A new Python script, `comp2/gif_to_dat.py`, was created. This script is responsible for:
        *   Reading the `badderbaby.gif` file.
        *   Iterating through its frames.
        *   Resizing each frame to `64x48` pixels.
        *   Converting each frame to 8-bit grayscale.
        *   Writing the processed frames into a raw binary format (`videoout-64x48x8.dat`) expected by the compression pipeline (header with dimensions, followed by raw grayscale pixel data).

3.  **Build Environment Adaptation (Windows)**:
    *   The `comp2/Makefile` was significantly adjusted to function correctly in a Windows MinGW environment:
        *   Removed dependencies on the `decodevideo` executable (which required FFMPEG libraries not present).
        *   Integrated `comp2/gif_to_dat.py` to generate the initial video data.
        *   Added essential linker flags (`-lgdi32 -luser32 -lkernel32`) for Windows GDI to resolve linking errors in visualization tools (`videocomp`, `streamcomp`).
        *   Re-enabled `-mavx2` compiler flag for `videocomp` to ensure correct compilation of performance-critical vector instructions.
        *   Updated the `FRAMECT` variable to `183` to reflect the actual number of frames in `badderbaby.gif`.

4.  **Cleanup Script**:
    *   A Python script, `comp2/clean.py`, was created and integrated into the `Makefile`'s `clean` targets. This script handles the removal of generated executables and intermediate data files in a platform-agnostic way, addressing issues with `rm -rf` on the current Windows setup.

## Compression Result (for `TARGET_GLYPH_COUNT=256`)

The `badderbaby.gif` (183 frames, 64x48 pixels) was successfully compressed using the project's techniques.

*   **Original Data (raw pixel equivalent)**: `183 frames * 64 * 48 pixels/frame * 1 byte/pixel = 560,640 bytes`.
*   **Final Compressed Output**: `docs/images/video-64x48x8.gif` (This file is now located in `docs/images/`)
*   **Size**: **6387 bytes**
*   **Compression Ratio**: Approximately **87.77:1** (uncompressed raw data to compressed GIF).

This result demonstrates highly effective compression, fitting the project's mandate for extremely small video payloads.

Although, if it's already good, try increasing the TARGET_GLYPH_COUNT to 512 - 1048 by increment to get better quality.

## Build Process

https://www.youtube.com/watch?v=VZwdiV46wpY
