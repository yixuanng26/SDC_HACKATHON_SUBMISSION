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
| **GitHub Repository** | [https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION](https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION) |
| **Replit Project** | [https://replit.com/@yixuanng26/MyFuture-Career-Guidance](https://replit.com/@yixuanng26/MyFuture-Career-Guidance) |
| **Live Demo** | [https://my-future-career-guidance.replit.app](https://my-future-career-guidance.replit.app) |
| **Demo / Pitch Video** | [https://youtu.be/-wAynwGt6dQ](https://youtu.be/-wAynwGt6dQ) |
| **Slide Deck** | [https://1drv.ms/p/c/df5b92a3986471d6/IQCnuGvJRLWSS6Eg7SC-qSuSAR21gKeJE1xloz4MjYDEnpE?e=5QEAAf](https://1drv.ms/p/c/df5b92a3986471d6/IQCnuGvJRLWSS6Eg7SC-qSuSAR21gKeJE1xloz4MjYDEnpE?e=5QEAAf) |
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

* **AI Career Guidance:** Helps users discover suitable career paths aligned with their interests, technical skills, and long-term career goals.
* **CV / Resume Import:** Provides a convenient workflow for users to quickly initialize their professional profile (currently simulated in prototype).
* **Target Career Selection:** Enables users to select desired target roles and establish a structured career development goal.
* **Career Match & Gap Analysis:** Performs deep side-by-side comparisons between users' existing skills and the required competencies for target roles.
* **Personalised Learning Roadmap:** Generates actionable learning tasks, key milestones, and estimated completion timelines to bridge skill gaps.
* **PathFinder AI Coach (Professional Advice):** Offers real-time AI career guidance and actionable next steps (unlocked via the demo checkout flow).
* **Career Fit Assessment:** Evaluates users' role-specific knowledge and practical skills through dynamic assessments to identify growth areas.
* **Explore Careers Taxonomy:** Allows users to explore comprehensive career options, estimated salaries, industry trends, and potential AI-driven job transformations.


## Tech Stack

| Layer | Technology |
| :--- | :--- |
| Frontend | e.g. Vite, React |
| Backend | e.g. Python, Flask |
| Database | e.g. N/A |
| AI / Compute | RunPod (GPU), Deepseek, Gemini Plus |
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
│   ├── SDC2026_ByteMe_Preliminary.pdf      # Preliminary submission
│   ├── SDC2026_ByteMe_TechDeclaration.pdf  # Technology declaration
│   ├── SDC2026_ByteMe_Replit_POU.pdf       # Replit proof of use
│   └── SDC2026_ByteMe_Runpod_POU.pdf       # RunPod proof of use
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
User / Browser
   │
   ▼
Replit Full-Stack App (Frontend & Backend API)
   │
   ├──► RunPod Serverless 1: vLLM DeepSeek-R1-Distill-Qwen-7B
   │      └── (Handles AI Career Guidance, Assessments & Recommendations)
   │
   └──► RunPod Serverless 2: Wan2.2-I2V-A14B-Lightning
          └── (Generates Custom Video Content)
   │
   ▼
Response Rendered & Returned to User
```

## How to Run

### Option 1 — Run on Replit (Recommended)

1. Open the [https://replit.com/@yixuanng26/MyFuture-Career-Guidance](https://replit.com/@yixuanng26/MyFuture-Career-Guidance), or import this repository via **Create Repl → Import from GitHub**.
2. Open the **Secrets** tab (🔒) and add the variables listed in `.env.example`:
   * `RUNPOD_API_KEY`
   * `RUNPOD_ENDPOINT_ID`
3. Click **Run**. Replit uses the `.replit` file to start `python src/main.py`.

### Option 2 — Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION.git
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

Our team utilized Replit as the primary environment for rapid development, full-stack integration, and cloud hosting:

- **Full-Stack Development:** Engineered the user interface (React/TypeScript) and API routing within Replit's unified workspace, leveraging built-in developer tools to accelerate component iteration and testing.
- **Production Hosting & Deployment:** Deployed the live web application using Replit Deployments (`https://my-future-career-guidance.replit.app`), providing high availability and real-time accessibility for end-to-end user testing.
- **Security & Secrets Management:** Managed all sensitive backend credentials—including RunPod API keys and serverless endpoint IDs—strictly through Replit Secrets, ensuring total isolation from the public codebase.
- **Environment & Build Configuration:** Customized runtime dependencies, scripts, and build pipelines using `.replit` and configuration files for seamless continuous execution.

📄 Proof of use: [submission/SDC2026_ByteMe_Replit_POU.pdf](https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION/blob/main/submission/SDC2026_ByteMe_Replit_POU.pdf)

## How We Use RunPod

Our project leverages RunPod’s serverless infrastructure to power scalable GPU compute and high-performance LLM inference:

- **Workload:** Executed LLM model inference (`deepseek-r1-distill-qwen-7b`) on RunPod GPU instances to dynamically process career assessments, generate skill gap analyses, and produce personalized learning pathways across 63 roles.
- **Serverless Architecture:** Configured and deployed `runpod/handler.py` as a **RunPod Serverless Endpoint**, enabling automatically scaled, on-demand compute without maintaining persistent server overhead.
- **API Integration:** Connected our Replit web application securely with RunPod using backend requests authenticated via `RUNPOD_API_KEY` and targeted through `RUNPOD_ENDPOINT_ID`.

Example request:

```bash
curl -X POST https://api.runpod.ai/v2/rg88ptje13dkwa/runsync \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{"input":{"prompt":"Write a short poem about artificial intelligence."}}'
```

📄 Proof of use: [submission/SDC2026_ByteMe_Runpod_POU.pdf](https://github.com/yixuanng26/SDC_HACKATHON_SUBMISSION/blob/main/submission/SDC2026_ByteMe_Runpod_POU.pdf)

## Challenges & Learnings

- **Challenges Faced & Solutions:**
  - **Integrating Open-Source LLM into Live App:** Integrating the heavy `deepseek-r1-distill-qwen-7b` model into a real-time web application presented challenges with cold-start latency and response formatting. We solved this by hosting the model on RunPod Serverless GPU with custom handlers (`handler.py`) and implementing structured API routing to ensure smooth user feedback.
  - **Multi-Disciplinary Skill Matching:** Initially, strict string matching caused 0% match rates for non-tech career roles (e.g., Medical, Arts, Business). We resolved this by expanding our taxonomy to support 63 distinct roles and implementing flexible fuzzy matching logic to accurately map cross-disciplinary user skill sets.

- **Key Team Learnings:**
  - **Cloud Workspace & Version Control:** Mastered cloud-based version control by seamlessly linking Visual Studio Code with GitHub, enabling automatic local-to-cloud workspace synchronization, commit workflows, and smooth deployment trigger pipelines.
  - **Serverless AI Inference:** Learned how to optimize open-source LLM inference (`deepseek-r1-distill-qwen-7b`) on serverless GPU infrastructure for cost-effective, real-time assessment generation.
  - **Secrets & Credentials Management:** Gained hands-on experience in securely decoupling configuration settings and API keys via environment variables and Replit Secrets.

    
## Future Improvements

- [ ] **Adaptive Dynamic Questioning:** Upgrade the skill test engine to dynamically adjust question difficulty based on real-time user answers.
- [ ] **Interactive Milestone Tracking:** Introduce detailed analytics and visual progress dashboards for user learning pathways.
- [ ] **AI Avatar Integration:** Incorporate an interactive 3D/2D AI Avatar mentor to conduct real-time conversational career mock interviews and personalized guidance.
- [ ] **Multi-Language Support:** Expand localized skill assessments and career guidance to support broader global student demographics.
- [ ] **Expanded Role Taxonomy:** Further expand the multi-disciplinary database beyond 63 roles to cover specialized niche fields and emerging industries.

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











