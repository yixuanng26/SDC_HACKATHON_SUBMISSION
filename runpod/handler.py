import runpod

def handler(job: dict) -> dict:
    # 1. Extract input sent from your Replit app
    job_input = job.get("input", {})
    prompt = job_input.get("prompt", "")

    # 2. Process the input using your app's logic
    # Replace this section with your actual function output
    result_data = {
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

    # 3. Return the result back to Replit
    return {"output": result_data}

runpod.serverless.start({"handler": handler})
