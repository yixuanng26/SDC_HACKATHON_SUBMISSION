# SDC_HACKATHON_SUBMISSION

> myfuture is an AI-powered career guidance platform designed to help working adults and fresh graduates navigate AI-driven job market changes through personalized skill assessments, career recommendations, and tailored learning pathways.

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
Artificial Intelligence (AI) is changing the job market and affecting both working adults and fresh graduates. As AI technology continues to develop, people need to understand how these changes may affect their careers and future opportunities.
Working adults who perform data entry and basic office tasks may face the risk of having some of their tasks automated by AI. This may change their job responsibilities and reduce the demand for certain skills. As a result, they may need to learn new skills and improve their knowledge to remain relevant in the workplace. Without proper training, they may find it difficult to adapt to changes in their jobs.
Fresh graduates also face challenges when entering the job market. They may feel uncertain about which career path to choose because AI is changing job requirements and creating new skill demands. Some graduates may struggle to identify suitable jobs that match their interests, abilities, and qualifications. Without proper career guidance, they may choose a career that has fewer future opportunities.
These challenges matter because employment affects people's income, financial stability, and future development. Therefore, working adults need opportunities to improve their skills, while fresh graduates need guidance to make better career decisions.
Our solution aims to use AI to help working adults identify skills they need to improve and help fresh graduates discover suitable future careers. By providing personalised career recommendations, future job trends, and step-by-step learning pathways, we hope to help people prepare for changes in the job market and build a more future-ready workforce.


## Solution
Our proposed application is an AI-powered career guidance platform designed to help working adults and fresh graduates prepare for future job opportunities. The application uses artificial intelligence to analyse users' skills, interests, and career preferences to provide suitable career recommendations.
The application includes a personality and skills assessment to help users understand their strengths and identify areas for improvement. It also provides information about the latest global job trends to help users understand how AI is changing the job market. Based on the assessment results, the application recommends suitable future careers and identifies the skills users need to develop. It also provides personalised learning pathways to help users improve their skills and prepare for future employment.
To support these functions, our project will use an AI API with the model DeepSeek-R1-Distill-Qwen-7B to process information and assist in generating career-related recommendations. The AI will help analyse user inputs and provide relevant suggestions based on the available data.
For development, we plan to use Replit to build the web application, RunPod to support API deployment, and GitHub to store and manage our source code. These technologies will help us develop a functional prototype that is accessible and easy to use.
Our goal is to use AI to make career guidance more accessible, help users identify future opportunities, and encourage lifelong learning in support of SDG 4: Quality Education, SDG 5: Gender Equality, SDG 8: Decent Work and Economic Growth, SDG 9: Industry, Innovation And Infrastructure, SDG 10: Reduced Inequalities.


## Key Features

* **Feature 1:** 

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| Frontend | e.g. Vite, React |
| Backend | e.g. Python, Flask |
| Database | e.g. N/A |
| AI / Compute | RunPod (GPU), Deepseek |
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
git clone [https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION.git](https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION.git)
cd SDC_HACKATHON_SUBMISSION

# 2. Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# Copy the example environment file to .env
cp .env.example .env    # On macOS/Linux
# copy .env.example .env # On Windows

# Open .env and replace the placeholders with actual API keys.

# 5. Run the app
python src/main.py
```

## Run Tests

```bash
python -m unittest discover tests
```
## How We Use Replit 

Describe how your team used Replit. For example:

- **Development:** Collaborative coding in a shared Repl using Multiplayer.
- **Hosting:** The app is deployed with Replit Deployments at the Live Demo link above.
- **Secrets:** API keys are stored in Replit Secrets, never in the code.

📄 Proof of use: [submission/SDC2026_ByteMe_Replit_POU.pdf](https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION/blob/main/submission/SDC2026_ByteMe_Replit_POU.pdf)

## How We Use RunPod  

Describe how your team used RunPod. For example:

- **Workload:** Model inference (e.g. text generation, image processing) runs on a RunPod GPU.
- **Setup:** `runpod/handler.py` is deployed as a **RunPod Serverless Endpoint**.
- **Integration:** The Replit app sends requests to the endpoint using `RUNPOD_API_KEY` and `RUNPOD_ENDPOINT_ID`.

Example request:

```bash
curl -X POST https://api.runpod.ai/v2/rg88ptje13dkwa/runsync \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{"input":{"prompt":"Write a short poem about artificial intelligence."}}'
```

📄 Proof of use: [submission/SDC2026_ByteMe_Runpod_POU.pdf](https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION/blob/main/submission/SDC2026_ByteMe_Runpod_POU.pdf)

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











