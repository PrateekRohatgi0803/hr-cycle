def skill_gap_analysis(required_skills, employee_skills):
    req = set([s.strip().lower() for s in required_skills.split(",")])
    emp = set([s.strip().lower() for s in employee_skills.split(",")])
    
    missing = req - emp
    matched = req & emp
    
    return list(matched), list(missing)