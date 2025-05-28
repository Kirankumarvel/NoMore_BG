# NoMore_BG

🖼️ **NoMore_BG** is a simple, interactive Python desktop tool that removes the background from images with just a few clicks. It uses [rembg](https://github.com/danielgatis/rembg) for powerful background removal, [Pillow](https://python-pillow.org/) for image processing, and [easygui](https://easygui.readthedocs.io/en/master/) for user-friendly file dialogs.

---

## Features

- **Easy-to-use GUI**: No need to type file paths—select images and save locations visually.
- **Supports PNG/JPG/JPEG**: Works with the most common image formats.
- **Automatic background removal**: Uses state-of-the-art AI to cut out backgrounds.
- **Preview option**: See your result immediately after processing.
- **Safe & local**: Everything runs on your computer—no uploads required.

---

## Installation

1. **Clone or download this repository.**

2. **Install the required packages:**

   ```bash
   pip install rembg pillow easygui
   ```

   > Make sure you're using Python 3.7 or higher.

---

## Usage

1. **Run the script:**

   ```bash
   python bg_remover_gui.py
   ```

2. **Follow the prompts:**
   - **Select your input image** (`.jpg`, `.jpeg`, or `.png`).
   - **Choose where to save** the background-free result (`.png`).
   - **Optional:** Preview the result.

3. **Done!**



---

## Troubleshooting

- **Missing packages?**  
  If you see import errors, install the missing dependencies:
  ```bash
  pip install rembg pillow easygui
  ```
- **Not seeing the GUI?**  
  Make sure your Python environment has access to a desktop display.

---

## How It Works

1. User selects an input image via a file dialog.
2. User chooses an output location to save the processed image.
3. The script loads the image, removes the background using `rembg`, and saves the result as a PNG.
4. Optionally, the result is shown in a preview window.

---

## Credits

- [rembg](https://github.com/danielgatis/rembg) - background removal engine
- [Pillow](https://python-pillow.org/) - image processing
- [easygui](https://easygui.readthedocs.io/en/master/) - graphical dialogs

---

## License

This project is provided under the MIT License.

---

**Enjoy your background-free images!**
