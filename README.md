# CareerMatchAI
> **The Intelligent Bridge Between Your Skills and Your Dream Job.**

**CareerMatchAI** is an AI-powered resume optimization platform built for the modern job market. It helps job seekers bypass the "Black Hole" of Applicant Tracking Systems (ATS) by providing deep semantic analysis and actionable feedback.



## The Problem
Most candidates fail at the initial screening stage because their resumes aren't optimized for specific job descriptions. Traditional keyword-matching tools are outdated; **CareerMatchAI** uses Deep Learning to understand the *meaning* behind your experience.

## Core Features
- **Semantic Match Scoring:** Uses Sentence-Transformers to calculate how well your resume aligns with a job description ($0-100\%$).
- **Intelligent Entity Extraction:** Automatically identifies Hard Skills, Soft Skills, and Experience using Spacy NER.
- **Gap Analysis:** Pinpoints exactly which requirements are missing from your profile.
- **AI-Driven Suggestions:** Provides real-time advice on how to rewrite bullet points for maximum impact.


## Tech Stack

### Frontend
- **React.js** (Vite) + **Tailwind CSS**
- **Axios** (for API communication)
- **Framer Motion** (for smooth UI animations)

### Backend
- **FastAPI** (Python)
- **PyMuPDF** (High-performance PDF parsing)

### Machine Learning
- **Sentence-Transformers** (SBERT - `all-MiniLM-L6-v2`)
- **Spacy** (Natural Language Processing)
- **Scikit-Learn** (Cosine Similarity)


## System Architecture

The system operates on a 3-layer architecture:
1. **Presentation Layer:** User-friendly React dashboard for file uploads and result visualization.
2. **Logic Layer:** FastAPI handles the orchestration between the UI and the ML models.
3. **Intelligence Layer:** The NLP pipeline that parses PDFs, extracts entities, and calculates similarity.


## Roadmap (8-Week Sprint)
- [x] **Week 1-2:** Project Setup, PDF Parsing, and API Skeleton.
- [ ] **Week 3-4:** ML Core (Vector Embeddings & Match Scoring).
- [ ] **Week 5-6:** NER Implementation & Keyword Highlighting.
- [ ] **Week 7:** AI Suggestion Engine & UI Refinement.
- [ ] **Week 8:** Final Testing & Cloud Deployment.


**© 2024 CareerMatchAI Team - CS Graduation Project**
