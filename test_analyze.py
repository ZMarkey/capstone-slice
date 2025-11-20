from analyze_resume import extract_skills

def test_extract_skills():
    text = "Python, Java, project management"
    skills = extract_skills(text)
    assert "Python" in skills
    assert "Java" in skills
    assert "project management" in skills
