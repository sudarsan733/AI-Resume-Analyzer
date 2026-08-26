def generate_recommendations(score, missing, matched):
    tips = []
    if missing:
        tips.append("Consider learning or highlighting: " + ", ".join(missing[:8]) + ".")
    if score < 50:
        tips.append("Tailor your resume with relevant job keywords and supporting projects.")
    elif score < 75:
        tips.append("Strengthen your resume with measurable achievements and relevant missing skills.")
    else:
        tips.append("Your textual alignment is strong. Keep matching skills and achievements easy to find.")
    if matched:
        tips.append("Support matched skills with evidence from projects, internships, or work experience.")
    return tips
