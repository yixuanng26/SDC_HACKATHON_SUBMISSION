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
            "market_demand": "High Growth",
            "match_score": "85%",
            "top_skills_needed": ["Core Professional Competencies", "Domain Knowledge", "Communication"],
            "suggested_next_step": f"Enhance core skills and practical projects for {target_role}"
        }
    }

    return {"output": result_data}
    # 3. Return the result back to Replit
    return {"output": result_data}

runpod.serverless.start({"handler": handler})
