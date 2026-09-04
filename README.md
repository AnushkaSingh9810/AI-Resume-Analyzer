# 🤖 AI Resume Analyzer

A Generative AI based application that analyzes a resume against a job description and provides insights about the candidate's suitability for the role.

## 📌 About the Project

**AI Resume Analyzer** is a Generative AI-powered web application designed to help candidates evaluate their resumes against a specific job description.

The application extracts information from a resume PDF and uses **Google Gemini API** to analyze the resume, identify matching and missing skills, calculate a match score, and provide personalized improvement suggestions.

## 🎯 Objective

The main objective of this project is to make the resume screening and job-matching process easier for candidates by providing AI-powered feedback.

## ✨ Features

* 📄 Upload resume in PDF format
* 📝 Analyze job description
* 🎯 Generate resume-job match score
* ✅ Identify matching skills
* ❌ Detect missing skills
* 💪 Analyze resume strengths
* 💡 Provide improvement suggestions
* 🎤 Generate AI-based interview questions

## 🛠️ Tech Stack

* **Python** – Application development
* **Streamlit** – Web application interface
* **Google Gemini API** – Generative AI-powered resume analysis
* **PyPDF** – PDF text extraction

## 🔄 How It Works

```text
Resume PDF + Job Description
            ↓
     PDF Text Extraction
            ↓
    Gemini Generative AI
            ↓
      Resume Analysis
            ↓
Match Score + Skills + Recommendations
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AnushkaSingh9810/AI-Resume-Analyzer.git
```

### 2. Navigate to the Project

```bash
cd AI-Resume-Analyzer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a Google Gemini API key and configure it in the project according to the application's configuration.

> **Note:** Never upload or expose your API key publicly on GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Example Analysis

The application provides insights such as:

* Resume-job compatibility score
* Skills that match the job description
* Skills that are missing
* Resume strengths
* Areas that need improvement
* AI-generated interview questions

## 💡 Use Cases

This project can be useful for:

* Students and freshers preparing for placements
* Job seekers tailoring resumes for specific roles
* Candidates identifying skill gaps
* Preparing for interviews
* Understanding how Generative AI can be applied to recruitment

## 🔮 Future Improvements

* Support for multiple resume formats
* Resume keyword optimization
* ATS compatibility analysis
* Resume improvement suggestions with downloadable output
* Job-role recommendations
* Resume comparison with multiple job descriptions

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes**. The AI-generated analysis should be treated as guidance and may not always be completely accurate.

## 👩‍💻 Author

**Anushka Singh**

GitHub:
https://github.com/AnushkaSingh9810

