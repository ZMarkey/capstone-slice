# analyze_resume.py

def extract_skills(text):
    # simple split by commas and strip spaces
    skills = [skill.strip() for skill in text.split(",")]
    return skills

if __name__ == "__main__":
    sample_text = open("sample_resume.txt").read()
    # assume skills line starts with "Skills:"
    skills_line = [line for line in sample_text.split("\n") if line.startswith("Skills:")][0]
    skills_text = skills_line.replace("Skills:", "").strip()
    skills = extract_skills(skills_text)
    print("Skills found:", skills)

