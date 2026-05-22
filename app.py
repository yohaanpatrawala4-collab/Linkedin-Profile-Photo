import os
import io
import base64
import streamlit as st
from PIL import Image, ImageOps
from frame_data import FRAME_BASE64

# Page Configuration
st.set_page_config(page_title="Create Your ABLBL Persona", page_icon="🖼️", layout="centered")

st.title("Create Your ABLBL Persona")
st.markdown("Precise, 1:1 pixel fidelity employee photo framing.")

# Main App Phase (Frame is embedded directly in code)
st.write("Upload an employee photo to apply the brand identity frame.")

employee_file = st.file_uploader("Upload Employee Photo", type=["jpg", "jpeg", "png"])

if employee_file is not None:
    employee_bytes = employee_file.read()
    
    with st.spinner("Processing image..."):
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
