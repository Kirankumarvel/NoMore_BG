from rembg import remove
from PIL import Image
import easygui
import sys
import os

def main():
    try:
        print("🖼️ Background Remover Tool - Starting...")
        
        # Step 1: Select input image
        print("1. Please select your input image...")
        input_path = easygui.fileopenbox(
            title="Select Image to Remove Background",
            default="*.jpg;*.jpeg;*.png",
            filetypes=["*.jpg", "*.jpeg", "*.png"]
        )
        
        if not input_path:
            print("❌ No image selected. Exiting...")
            return
            
        # Step 2: Select output location
        print("2. Choose where to save the result...")
        default_name = os.path.splitext(os.path.basename(input_path))[0] + "_nobg.png"
        output_path = easygui.filesavebox(
            title="Save Background-Free Image",
            default=default_name,
            filetypes=["*.png"]
        )
        
        if not output_path:
            print("❌ No save location selected. Exiting...")
            return
            
        # Ensure .png extension
        if not output_path.lower().endswith('.png'):
            output_path += '.png'
        
        # Step 3: Process the image
        print("🔄 Removing background (this may take a moment)...")
        with Image.open(input_path) as img:
            result = remove(img)
            result.save(output_path)
            print(f"✅ Success! Image saved to:\n{output_path}")
            
            # Show preview option
            if easygui.ynbox("Background removed successfully! Show preview?", "Preview", ("Yes", "No")):
                result.show()
                
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        if easygui.ynbox("An error occurred. Would you like to see more details?", "Error", ("Yes", "No")):
            raise
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    # Check requirements
    try:
        import rembg
        import PIL
        import easygui
    except ImportError as e:
        print(f"❌ Missing package: {str(e)}")
        print("Please install required packages:")
        print("pip install rembg pillow easygui")
        sys.exit(1)
    
    main()
