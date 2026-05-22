# 🖼️ Brand Identity Photo Overlay Tool

An interactive, 1:1 pixel fidelity employee photo overlay tool tailored for the **Aditya Birla Lifestyle Brands** network.

This web application allows employees to easily upload their portrait photo and instantly generate a beautifully framed, circular profile image complete with company branding and official lifestyle brand logos.

---

## ✨ Features

- **Built-in Brand Frame**: The official Aditya Birla Lifestyle Brands frame is fully embedded directly in the application code. No setup or external file hosting required!
- **Pure-Python Face-Detection**: Safe client-side heuristic to check that the uploaded photo is a valid portrait.
- **LANCZOS High-Quality Scaling**: Automatically resizes and centers employee photos to perfectly align with the circular brand boundary with no distortion.
- **One-Click Download**: Generates a high-quality transparent PNG output ready for LinkedIn, Slack, or other professional profiles.

---

## 🛠️ How It Works

1. Open the deployed Streamlit link.
2. Click **Upload Employee Photo** and select your portrait (`.jpg`, `.jpeg`, or `.png`).
3. View the final result in the preview window.
4. Click **Download Result** to save your high-resolution branded profile picture.

---

## 💻 Local Installation & Development

If you want to run this application locally on your computer:

### Prerequisites
Make sure you have [Python 3.8+](https://www.python.org/) installed.

### Setup Instructions
1. Clone or download this repository.
2. Open your terminal in the repository folder.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
