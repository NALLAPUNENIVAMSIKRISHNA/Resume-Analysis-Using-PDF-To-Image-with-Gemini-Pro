# ATS Resume Evaluation using Google Gemini Pro (PDF to Image)

Demo Video Link :- https://drive.google.com/file/d/1qH_60joDIp4-NBABmiVKErpDlmfmE-Ao/view?usp=sharing

This project is a Streamlit-based AI tool that evaluates a candidate's resume against a given job description using Google's Gemini Pro model. It uses PDF-to-image conversion for analyzing visual resumes and generates insightful feedback including resume review, skill improvement suggestions, and match percentage.

---

##  Features

- Paste a **Job Description**.
- Upload your **Resume in PDF format**.
- Choose between 3 options:
  -  Get a review of your resume.
  -  Suggestions for improving your skills.
  -  Get a match percentage between your resume and the job description.
- AI-powered feedback using **Gemini Pro**.
- Works with visually designed resumes (PDFs converted to image format).

---

##  Technologies Used

- **Python**
- **Streamlit** – for the interactive web interface
- **Google Generative AI SDK** – for interacting with Gemini Pro
- **pdf2image** – for converting PDF to image
- **Pillow (PIL)** – for image processing
- **base64** – for encoding images to be compatible with Gemini
- **python-dotenv** – to load API keys securely from `.env` file

---

##  Project Structure

```
 resume_gemini_app/
├── app.py                # Streamlit application
├── .env                   # Contains the Google API Key (not to be shared)
├── requirements.txt       # List of dependencies
```

---

##  Setup Instructions

### 1. Clone the Repository

### 2. Install Dependencies

Make sure you are using Python 3.8 or above.

```bash
pip install -r requirements.txt
```

### 3. Install Poppler

- **Windows**: Download from https://github.com/oschwartz10612/poppler-windows
- **Mac**: Use `brew install poppler`
- **Linux**: Use `sudo apt install poppler-utils`

Make sure `poppler` is added to your system PATH.

### 4. Set Up Environment Variables

Create a `.env` file in the root folder and add your Google API Key:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

##  How to Run the Application

```bash
streamlit run main.py
```

The app will open in your browser.

---

##  How It Works

1. **User Inputs**:
   - A **Job Description** is entered in a text area.
   - A **Resume PDF** is uploaded.

2. **PDF to Image**:
   - The first page of the resume PDF is converted to an image using `pdf2image`.
   - The image is encoded in **base64** format (required by Gemini Pro for image input).

3. **Gemini Prompt Selection**:
   - Based on the selected button, the app sends a specific prompt to Gemini Pro:
     - General resume feedback
     - Skill improvement advice
     - Percentage match between resume and job description

4. **Gemini Pro Response**:
   - The AI model responds with a detailed analysis.
   - The result is displayed in the app interface.

---

##  Example Prompts Used

- “Act like an ATS and evaluate this resume based on the job description...”
- “Identify missing skills in the resume when compared to this job description...”
- “Give me a percentage match between this resume and the job description...”

---

##  Security

- The API key is stored in a `.env` file and should **not be shared publicly**.

---

##  Requirements File (`requirements.txt`)

```
streamlit
python-dotenv
google-generativeai
pdf2image
```

##  Future Improvements

- Add support for multiple-page resume analysis.
- Highlight missing keywords visually.
- Save analysis results to a database.
- Add downloadable PDF report generation.
