# 🤝 Personalized Networking Assistant

An AI-powered web application that generates personalized conversation starters for networking events based on the user's interests and event details.

---

## 📌 Project Overview

The Personalized Networking Assistant helps users create meaningful conversations during professional events, conferences, and networking sessions. The application analyzes event topics, extracts important themes, and generates AI-powered conversation starters.

The project also includes fact-checking using Wikipedia, conversation history management, and a feedback system.

---

## ✨ Features

✅ Event theme extraction

✅ AI-powered conversation starters

✅ Topic generation using NLP

✅ Wikipedia fact-checking

✅ Conversation history tracking

✅ Feedback management

✅ User-friendly Streamlit interface

---

## 🏗️ Tech Stack

| Category | Technology |
|----------|-------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Language | Python |
| NLP Model | DistilBERT |
| Text Generation | GPT-2 |
| Fact Checking | Wikipedia API |
| Testing | Pytest |
| Version Control | Git & GitHub |

---

## 📂 Repository Structure

```text
Personalized-Networking-Assistant/

├── 1. Brainstorming & Ideation
├── 2. Requirement Analysis
├── 3. Project Design Phase
├── 4. Project Planning Phase
├── 5. Project Development Phase
├── 6. Project Testing
├── 7. Project Documentation
├── 8. Project Demonstration
│
├── app/
│   ├── models/
│   ├── routers/
│   ├── services/
│   ├── config.py
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│   ├── test_event_analyzer.py
│   ├── test_fact_checker.py
│   ├── test_routes.py
│   └── test_topic_generator.py
│
├── history.json
├── feedback.json
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ky1577359-cpu/personal-networking-assistant-solo.git
```

### 2️⃣ Open the project folder

```bash
cd personal-networking-assistant-solo
```

### 3️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 4️⃣ Activate the virtual environment

```bash
venv\Scripts\activate
```

### 5️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Start FastAPI server

```bash
uvicorn app.main:app --reload
```

### Start Streamlit frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🧠 Core Modules

### 📌 Event Analyzer

Analyzes the event description and extracts important themes.

### 💬 Topic Generator

Generates personalized conversation starters.

### 🔍 Fact Checker

Verifies information using Wikipedia.

### 📝 History Logger

Stores generated conversations.

### 👍 Feedback Logger

Stores user feedback.

---

## 📖 Project Phases

- Brainstorming & Ideation
- Requirement Analysis
- Project Design
- Project Planning
- Development
- Testing
- Documentation
- Demonstration

---

## 🚀 Future Enhancements

- User authentication
- Cloud deployment
- Database integration
- Multi-language support
- Improved AI models

---

## 🎥 Demo Video

🚧 Demo video link : https://drive.google.com/file/d/1Gf5c0laoiEt5XBggiroxcvyWldj31SAA/view?usp=sharing

---

## 📁 Project Documents

🚧 Google Drive link : https://drive.google.com/drive/folders/1PbTOlFAisKjYtjX6ouX_CPScpcHyBB4A?usp=sharing

---

## 👨‍💻 Developer

**Kajal Yadav**

BCA Student

---

## 📜 License

This project was developed as part of the SmartBridge / SkillWallet internship program.
