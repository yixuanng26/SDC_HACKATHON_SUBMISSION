# SDC_HACKATHON_SUBMISSION

> An AI-powered application built for the Software Development Club (SDC) Hackathon, hosted on Replit and leveraging GPU acceleration via RunPod.

---

## Team Information
* **Team Name:** Byte Me
* **Team Leader:** Ng Yi Xuan ([yixuan1161@gmail.com](mailto:yixuan1161@gmail.com))
* **University:** Universiti Teknologi Malaysia (UTM)
* **Number of Members:** 5

---

## Team Domain
* **Selected Domain:** Domain 1
* **SDG Track (1–17):**  
  SDG 4 - Quality Education  
  SDG 5 - Gender Equality  
  SDG 8 - Decent Work And Economic Growth  
  SDG 9 - Industry, Innovation And Infrastructure  
  SDG 10 - Reduced Inequalities  

---

## Necessary links (demo, pitch video)

| Resource | Link |
| :--- | :--- |
| **GitHub Repository** | `https://github.com/your-username/your-project` |
| **Replit Project** | `https://replit.com/@your-username/your-project` |
| **Live Demo** | `https://your-project.replit.app` |
| **Demo / Pitch Video** | `https://example.com/demo-video` |
| **Slide Deck** | `https://example.com/slides` |
| **RunPod Endpoint** | [https://api.runpod.ai/v2/rg88ptje13dkwa/runsync](mailto:https://api.runpod.ai/v2/rg88ptje13dkwa/runsync) |

---

## Overview

## Problem

## Solution

## Key Features

* **Feature 1:** 

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| Frontend | e.g. HTML, React |
| Backend | e.g. Python, Flask / FastAPI |
| Database | e.g. PostgreSQL, SQLite |
| AI / Compute | RunPod (GPU) |
| Hosting / Dev | Replit |

## Project Structure

```text
.
├── docs/                       # Screenshots, diagrams
├── runpod/
│   └── handler.py              # RunPod serverless handler (GPU workload)
├── src/
│   ├── main.py                 # Application entry point
│   └── utils.py                # Helper functions
├── submission/                 # Required submission documents
│   ├── SDC2026_TeamName_Preliminary.pdf      # Preliminary submission
│   ├── SDC2026_TeamName_TechDeclaration.pdf  # Technology declaration
│   ├── SDC2026_TeamName_Replit_POU.pdf       # Replit proof of use
│   └── SDC2026_TeamName_Runpod_POU.pdf       # RunPod proof of use
├── tests/
│   └── test_utils.py           # Unit tests
├── .env.example                # Example environment variables
├── .gitignore
├── .replit                     # Replit run configuration
├── LICENSE
├── requirements.txt            # Python dependencies
└── README.md
```

## Architecture

```text
User ⟶ Replit (App / API) ⟶ RunPod Endpoint (GPU model)
  │
  └─> Response returned to user
```

## How to Run

### Option 1 — Run on Replit (Recommended)

1. Open the [Replit Project](替换成你的Replit链接), or import this repository via **Create Repl → Import from GitHub**.
2. Open the **Secrets** tab (🔒) and add the variables listed in `.env.example`:
   * `RUNPOD_API_KEY`
   * `RUNPOD_ENDPOINT_ID`
3. Click **Run**. Replit uses the `.replit` file to start `python src/main.py`.

### Option 2 — Run Locally

```bash
# 1. Clone the repository
git clone [https://github.com/你的用户名/你的项目名.git](https://github.com/你的用户名/你的项目名.git)
cd 你的项目名

# 2. Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# (根据需要写上复制 .env.example 并配置 key 的步骤)

# 5. Run the app
python src/main.py
```

## Run Tests

```bash
python -m unittest discover tests
```
## How We Use Replit *(Required)*

Describe how your team used Replit. For example:

- **Development:** Collaborative coding in a shared Repl using Multiplayer.
- **Hosting:** The app is deployed with Replit Deployments at the Live Demo link above.
- **Secrets:** API keys are stored in Replit Secrets, never in the code.

📄 Proof of use: [submission/SDC2026_YourTeamName_Replit_POU.pdf](submission/SDC2026_YourTeamName_Replit_POU.pdf)

## How We Use RunPod *(Required)*

Describe how your team used RunPod. For example:

- **Workload:** Model inference (e.g. text generation, image processing) runs on a RunPod GPU.
- **Setup:** `runpod/handler.py` is deployed as a **RunPod Serverless Endpoint**.
- **Integration:** The Replit app sends requests to the endpoint using `RUNPOD_API_KEY` and `RUNPOD_ENDPOINT_ID`.

Example request:

```bash
curl -X POST [https://api.runpod.ai/v2/$RUNPOD_ENDPOINT_ID/runsync](https://api.runpod.ai/v2/$RUNPOD_ENDPOINT_ID/runsync) \
  -H "Authorization: Bearer $RUNPOD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input": {"prompt": "Hello"}}'
```

📄 Proof of use: [submission/SDC2026_YourTeamName_Runpod_POU.pdf](submission/SDC2026_YourTeamName_Runpod_POU.pdf)

## Challenges & Learnings

- What challenges did you face, and how did you overcome them?
- What did your team learn?

## Future Improvements

- [ ] Improvement 1
- [ ] Improvement 2

## Team

| Name | Role | GitHub |
| :--- | :--- | :--- |
| Ng Yi Xuan | Team Leader / Backend Developer | [@yixuanng26](https://github.com/yixuanng26) |
| Lee Xin Ying | Frontend Developer | [@xinying313](https://github.com/xinying313) |
| Siew Ming En | AI / Cloud Engineer | [@siewmingen](https://github.com/siewmingen) |
| Seah Jia Xuan | Frontend & UI/UX Designer | [@seahjiaxuan0364](https://github.com/seahjiaxuan0364) |
| Lucius Heng Du Meng | Prompt Engineer / Pitcher | [@luciusheng](https://github.com/luciusheng) |

## Submission Checklist

- [/] Team name, domain (Domain 1 / Domain 2) and SDG track filled in
- [/] Slide deck link added
- [/] Demo video link added
- [/] Replit used, with proof of use in `submission/`
- [/] RunPod used, with proof of use in `submission/`
- [/] Preliminary submission completed (`SDC2026_TeamName_Preliminary.pdf`)
- [/] Technology declaration completed (`SDC2026_TeamName_TechDeclaration.pdf`)
- [/] Submission files renamed with your team name (replace `TeamName`)
- [/] "How to Run" steps verified
- [/] No API keys or secrets committed to the repository

## License

This project is licensed under the [Apache License 2.0](LICENSE).











