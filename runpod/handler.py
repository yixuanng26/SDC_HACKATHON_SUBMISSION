import runpod

def handler(job: dict) -> dict:
    prompt = job.get("input", {}).get("prompt", "")
    
    ai_response = {
        "status": "success",
        "user_query": prompt,
        "recommendation": {
            "target_role": "Data Analyst / Engineer",
            "market_demand": "High Growth (Malaysia Tech Sector)",
            "match_score": "88%",
            "top_skills_needed": ["SQL (Advanced)", "Python (Pandas/PySpark)", "Data Visualization"],
            "suggested_next_step": "Complete the 'Build SQL foundations' quest."
        }
    }
    
    return {"output": ai_response}

runpod.serverless.start({"handler": handler})
