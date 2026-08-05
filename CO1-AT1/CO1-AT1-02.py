import re
 
# ---------------------------------------------------------------------
# Sample resume database (in a real system these would be text files
# read from disk / a database; here they are simulated as strings)
# ---------------------------------------------------------------------
resumes = [
    """
    Name: Arjun Mehta
    Email: arjun.mehta92@gmail.com
    Mobile: +91 9876543210
    Skills: Python, Machine Learning, SQL
    Experience: 3 years of experience in Data Science
    """,
    """
    Name: Sneha Reddy
    Email: sneha_reddy@outlook.com
    Contact Number: 9123456780
    Skills: Java, NLP
    Experience: 1 year of experience as a backend developer
    """,
    """
    Name: Rahul Verma
    Email: rahul.verma@yahoo.com
    Mobile: 9988776655
    Skills: Python, SQL, NLP, Machine Learning
    Experience: 5 years of experience in AI research
    """,
]
 
# ---------------------------------------------------------------------
# Regular expression patterns
# ---------------------------------------------------------------------
NAME_PATTERN = re.compile(r"Name:\s*([A-Za-z.]+(?:\s[A-Za-z.]+)*)")
EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
MOBILE_PATTERN = re.compile(r"(?:\+91[\s-]?)?[6-9]\d{9}")
SKILL_PATTERN = re.compile(r"\b(Python|Java|SQL|Machine Learning|NLP)\b", re.IGNORECASE)
EXPERIENCE_PATTERN = re.compile(r"(\d+)\s*(?:\+)?\s*years?\s+of\s+experience", re.IGNORECASE)
 
 
def extract_candidate_info(resume_text):
    """Extracts structured candidate information from raw resume text."""
    name_match = NAME_PATTERN.search(resume_text)
    email_match = EMAIL_PATTERN.search(resume_text)
    mobile_match = MOBILE_PATTERN.search(resume_text)
    skills_found = sorted(set(s.title() if s.lower() != "sql" and s.lower() != "nlp"
                               else s.upper() for s in SKILL_PATTERN.findall(resume_text)))
    exp_match = EXPERIENCE_PATTERN.search(resume_text)
 
    candidate = {
        "name": name_match.group(1).strip() if name_match else "Not Found",
        "email": email_match.group(0).strip() if email_match else "Not Found",
        "mobile": mobile_match.group(0).strip() if mobile_match else "Not Found",
        "skills": skills_found if skills_found else ["Not Found"],
        "experience_years": int(exp_match.group(1)) if exp_match else 0,
    }
    return candidate
 
 
def is_eligible(candidate, min_experience=2, required_skill="Python"):
    """Checks minimum eligibility: required experience AND required skill."""
    return (candidate["experience_years"] >= min_experience and
            required_skill in candidate["skills"])
 
 
def print_summary(candidate, index):
    print(f"\nCandidate {index}")
    print("-" * 40)
    print(f"Name              : {candidate['name']}")
    print(f"Email             : {candidate['email']}")
    print(f"Mobile Number     : {candidate['mobile']}")
    print(f"Skills            : {', '.join(candidate['skills'])}")
    print(f"Experience (yrs)  : {candidate['experience_years']}")
    print(f"Eligible (>=2 yrs & Python) : {'YES' if is_eligible(candidate) else 'NO'}")
 
 
def main():
    print("=" * 55)
    print(" RESUME INFORMATION EXTRACTION SYSTEM")
    print("=" * 55)
 
    all_candidates = []
    for idx, resume in enumerate(resumes, start=1):
        candidate = extract_candidate_info(resume)
        all_candidates.append(candidate)
        print_summary(candidate, idx)
 
    print("\n" + "=" * 55)
    print(" SHORTLISTED CANDIDATES (Min 2 yrs experience + Python)")
    print("=" * 55)
    eligible_candidates = [c for c in all_candidates if is_eligible(c)]
 
    if eligible_candidates:
        for c in eligible_candidates:
            print(f" - {c['name']} | {c['experience_years']} yrs | {', '.join(c['skills'])}")
    else:
        print(" No candidates meet the eligibility criteria.")
 
 
if __name__ == "__main__":
    main()
