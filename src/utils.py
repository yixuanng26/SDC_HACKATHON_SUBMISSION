def format_user_profile(raw_data):
    """Formats raw user profile data."""
    name = raw_data.get("name", "Unknown")
    education = raw_data.get("education", "")
    display_title = f"{name} ({education}" if education else name
    if education and not display_title.endswith(")"):
        display_title += ")"
    return {
        "name": name,
        "age": raw_data.get("age"),
        "education": education,
        "display_title": display_title
    }

def calculate_milestone_progress(completed_tasks):
    """Calculates progress percentage from a list of booleans."""
    if not completed_tasks:
        return 0.0
    completed_count = sum(1 for task in completed_tasks if task)
    return (completed_count / len(completed_tasks)) * 100

def match_career_path(user_skills, target_role):
    """Matches user skills against a target role and returns a match score dictionary."""
    # 简单计算一个模拟的 match_score（例如根据技能数量或固定逻辑）
    score = min(len(user_skills) * 33, 100) if user_skills else 0
    return {
        "target_role": target_role,
        "match_score": score
    }
