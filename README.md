# 📄 ATS Resume Analyzer

Upload your resume PDF and get an instant ATS-friendliness score!  
Easily see what sections are detected, what skills are matched, and how your resume performs against common Applicant Tracking System (ATS) criteria.

---

## 🚀 Features

- **Intuitive Streamlit UI**: Upload your PDF, view parsed text, and get results in seconds.
- **Real-time ATS Scoring**: Analyzes sections, skills, contact info, and optimal length.
- **Privacy-first**: All analysis runs locally in your browser/session.
- **Customizable**: Expand skill/section lists and scoring logic to fit your field.

---

## 📦 File Structure

resume_ats_app/
├── app.py # Streamlit frontend
├── ats_scoring.py # Resume analysis & scoring logic
├── utils.py # PDF text extraction utilities
├── requirements.txt # List of dependencies
├── sample_resume.pdf # (Optional) Example resume
text

---

## ⏳ Getting Started

### 1. Clone the Project

git clone https://github.com/Raghavv7989/resume_ats_app.git
cd resume_ats_app
text

### 2. (Recommended) Create Virtual Environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
text

### 3. Install Dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm
text
<details>
<summary>Note for deployment on Streamlit Cloud or similar</summary>
Include the SpaCy model in `requirements.txt`, e.g.:  
spacy>=3.0.0,<4.0.0
https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1.tar.gz#egg=en_core_web_sm
text
</details>

### 4. Run the App

streamlit run app.py
text

- Go to the provided localhost link in your browser
- Upload your PDF and see the results!

---

## ⚙️ How It Works

1. **Upload a PDF**  
2. App extracts text using PyPDF2  
3. Resume is analyzed for:
    - Sections (Education, Experience, Skills, etc.)
    - In-demand skills
    - Contact info (email, phone)
    - Appropriate length
4. **Score and breakdown** are presented along with suggestions.

---

## 🛠️ Customization

- Add skills to `COMMON_SKILLS` in `ats_scoring.py`
- Add or tweak section headers in `SECTION_KEYWORDS`
- Adjust scoring logic as per industry or job

---

## 🤝 Contributing

Contributions welcome!  
- Fork the project  
- Create a branch: `git checkout -b feature/YourFeature`
- Commit your changes
- Open a pull request

---

## 📄 License

[MIT License](LICENSE)

---

## 📬 Contact

For suggestions or collaboration, reach out via LinkedIn or open an issue/pr!

---

*Empower your job search. Make your resume bot-friendly!*
