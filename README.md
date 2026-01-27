![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![AI](https://img.shields.io/badge/AI-Gemini_2.5_Flash-blue)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![Input](https://img.shields.io/badge/Input-PDF_+_Text-orange)
![Mode](https://img.shields.io/badge/Analysis-Multimodal-purple)

---

```md
# 📄 RESUMEIQ - Smart ATS Resume Analyzer

A modern AI-powered ATS (Applicant Tracking System) resume analyzer built with Streamlit and Google Gemini 2.5 Flash.  
The application performs **native multimodal analysis** by evaluating PDF resumes directly against job descriptions—without OCR or manual text extraction.

---

## 🚀 Features
- Resume vs Job Description analysis
- Native PDF understanding using Gemini (no OCR required)
- ATS match percentage (0–100%)
- Matching & missing skills detection
- Strengths and improvement suggestions
- Final hiring verdict (Hire / Review / Reject)
- Clean, responsive Streamlit UI

---

## 🛠️ Tech Stack

- **Frontend & App Framework:** Streamlit  
- **AI Model:** Google Gemini 2.5 Flash (`google-generativeai`)  
- **Language:** Python  
- **Environment Management:** python-dotenv  

---

## 🧠 How It Works
```

Job Description (Text)
+
Resume (PDF Upload)
↓
Prompt Engineering
↓
Gemini 2.5 Flash (Multimodal)
↓
ATS Evaluation & Insights

```

---

## 📂 Project Structure
```

├── app.py                # Streamlit application
├── .env                  # Environment variables
├── requirements.txt      # Dependencies
└── README.md

````

---

## 🔐 Environment Setup

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
````

### 2️⃣ Configure API Key

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## ⚙️ Model Details

* **Model Used:** `gemini-2.5-flash`
* **Capabilities:** Native multimodal input (text + PDF)
* **Advantage:** No OCR, faster analysis, higher semantic accuracy

---

## 📌 Use Cases

* ATS resume optimization
* Job-specific resume evaluation
* Internship & placement preparation
* AI-assisted hiring screening

---

## 🚧 Future Enhancements

* Resume score visualization
* Multi-job comparison
* Exportable ATS reports
* Resume ranking for bulk uploads

---

## 👩‍💻 Author

**Shreya Rawat**
B.Tech CSE | AI-Driven Applications & Web Development

```

---



