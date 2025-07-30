import re
import spacy

nlp = spacy.load('en_core_web_sm')

# Define important section keywords
SECTION_KEYWORDS = [
    "education", "experience", "projects", "skills", "certifications",
    "summary", "interests", "languages", "contact"
]
# Simple skillset as an example (expand as needed)
COMMON_SKILLS = [
    "python", "machine learning", "deep learning", "sql", "data analysis",
    "java", "c++", "excel", "communication", "project management"
]

def extract_sections(text):
    """Return detected section headers (case-insensitive match)."""
    found = []
    for kw in SECTION_KEYWORDS:
        if re.search(r'\b' + re.escape(kw) + r'\b', text, re.I):
            found.append(kw)
    return found

def extract_skills(text):
    """Return matched skills from COMMON_SKILLS."""
    text_lower = text.lower()
    return [skill for skill in COMMON_SKILLS if skill in text_lower]

def has_contact_info(text):
    email = re.search(r'[\w\.-]+@[\w\.-]+', text)
    phone = re.search(r'\b\d{10,15}\b', text.replace(" ", ""))
    return bool(email and phone)

def analyze_length(text):
    # Ideal resume: 1-2 pages; we can proxy length by word count
    words = len(text.split())
    return 300 <= words <= 900

def calculate_ats_score(text):
    """Analyze resume text and return a score and details breakdown."""
    sections = extract_sections(text)
    n_sections = len(sections)
    skills = extract_skills(text)
    n_skills = len(skills)
    contact = has_contact_info(text)
    good_length = analyze_length(text)

    # Rudimentary scoring logic (can be improved)
    score = 0
    details = {}

    # Section count (30%)
    section_score = min(n_sections / len(SECTION_KEYWORDS), 1.0) * 30
    score += section_score
    details['Sections Present'] = f"{n_sections}/{len(SECTION_KEYWORDS)} ({section_score:.1f}%)"

    # Skills (30%)
    skill_score = min(n_skills / len(COMMON_SKILLS), 1.0) * 30
    score += skill_score
    details['Skills Matched'] = f"{n_skills}/{len(COMMON_SKILLS)} ({skill_score:.1f}%)"

    # Contact Info (20%)
    contact_score = 20 if contact else 0
    score += contact_score
    details['Contact Info Present'] = f"{'Yes' if contact else 'No'} ({contact_score}%)"

    # Length (20%)
    length_score = 20 if good_length else 0
    score += length_score
    details['Recommended Length'] = f"{'Yes' if good_length else 'No'} ({length_score}%)"

    score = round(score, 1)
    return score, details
