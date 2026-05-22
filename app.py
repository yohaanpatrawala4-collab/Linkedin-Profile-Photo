import os
import io
import base64
import streamlit as st
from PIL import Image, ImageOps
from frame_data import FRAME_BASE64

# Page Configuration
st.set_page_config(page_title="Brand Identity Overlay", page_icon="🖼️", layout="centered")

def detect_person(image_bytes):
    """
    Detects if there is a person in the image using a pure Python skin-tone heuristic.
    """
    try:
        img = Image.open(io.BytesIO(image_bytes)).convert('YCbCr')
        img.thumbnail((100, 100)) # resize for speed
        
        # Skin tone range in YCbCr: Y > 80, 85 < Cb < 135, 135 < Cr < 180
        pixels = img.getdata()
        skin_pixels = 0
        total_pixels = len(pixels)
        
        for y, cb, cr in pixels:
            if y > 80 and 85 < cb < 135 and 135 < cr < 180:
                skin_pixels += 1
                
        # If more than 5% of the image is skin tone, assume there's a person
        return (skin_pixels / total_pixels) > 0.05
    except Exception:
        return True # Default to True on error

st.title("Brand Identity Overlay")
st.markdown("Precise, 1:1 pixel fidelity employee photo framing.")

# Main App Phase (Frame is embedded directly in code)
st.write("Upload an employee photo to apply the brand identity frame.")

employee_file = st.file_uploader("Upload Employee Photo", type=["jpg", "jpeg", "png"])

if employee_file is not None:
    employee_bytes = employee_file.read()
    
    with st.spinner("Processing image..."):
        if not detect_person(employee_bytes):
            st.error("No person detected in the image. Please upload a valid employee photo.")
        else:
            try:
                # 1. Open images
                emp_img = Image.open(io.BytesIO(employee_bytes)).convert("RGBA")
                
                # Load the embedded frame image
                frame_bytes = base64.b64decode(FRAME_BASE64)
                frame_img = Image.open(io.BytesIO(frame_bytes)).convert("RGBA")
                
                fw, fh = frame_img.size
                
                # 2. Composition & Alignment
                emp_cropped = ImageOps.fit(emp_img, (fw, fh), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
                
                # 3. Layering
                final_img = Image.new("RGBA", (fw, fh))
                final_img.paste(emp_cropped, (0, 0))
                final_img = Image.alpha_composite(final_img, frame_img)
                
                # Display
                st.image(final_img, caption="Final Output", use_container_width=True)
                
                # Save to buffer for download
                img_io = io.BytesIO()
                final_img.save(img_io, 'PNG')
                img_io.seek(0)
                
                st.download_button(
                    label="Download Result",
                    data=img_io,
                    file_name="branded_employee.png",
                    mime="image/png"
                )
            except Exception as e:
                st.error(f"Image processing failed: {str(e)}")
