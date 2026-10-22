import runpod

def handler(job: dict) -> dict:
    job_input = job.get("input", {})
    prompt = job_input.get("prompt", "")
    
    target_role = job_input.get("target_role", prompt if prompt else "Selected Career Role")

    result_data = {
        "status": "success",
        "user_query": prompt,
        "recommendation": {
            "target_role": target_role,
            "market_demand": f"High Growth & Stable Demand in {target_role} Sector",
            "match_score": "85%",
            "top_skills_needed": [
                f"Core {target_role} Competencies", 
                "Professional Domain Knowledge", 
                "Practical Execution & Problem Solving"
            ],
            "suggested_next_step": f"Build targeted domain projects and strengthen core skills for {target_role}"
        }
    }

    return {"output": result_data}

runpod.serverless.start({"handler": handler})