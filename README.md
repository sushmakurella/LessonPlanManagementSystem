# 📚 Lesson Plan Management System

The **Lesson Plan Management System** is a web-based application designed to simplify and streamline the process of creating, updating, and exporting academic lesson plans. Whether you're building a plan from scratch or uploading a syllabus PDF to auto-generate one, this system offers the flexibility and tools educators need.

---

## ✨ Features


✅ **Create Lesson Plans Manually**  
Users can input the number of Course Outcomes (COs) and create lesson plans manually based on their structure.
![image](https://github.com/user-attachments/assets/f3c25369-8ef3-4eeb-b098-ed69066c9e05)
#### Home page


✅ **Upload & Auto-generate from PDF**  
Upload a syllabus PDF, and the system will intelligently extract data to automatically generate a lesson plan—saving time and reducing manual errors.
![image](https://github.com/user-attachments/assets/b75693ac-ee5e-4992-8a16-0a4b1a58fff4)
#### uploading PDF
![image](https://github.com/user-attachments/assets/afb5398f-eefc-4a83-b3d0-b08075a9bf36)
#### Syllabus Extracted from uploaded PDF



✅ **Update Existing Plans**  
Edit and update previously created lesson plans effortlessly to keep them aligned with curriculum updates.

✅ **Export as PDF**  
Download the finalized lesson plan in a clean, printable PDF format for easy sharing and archiving.
![image](https://github.com/user-attachments/assets/ab155611-56bc-45df-80fc-f87310dd7062)
#### viewing the existing lesson plan
![image](https://github.com/user-attachments/assets/7fce45ae-6dde-4acd-ad2c-dc70c032fbc1)
#### Exporting the Lesson plan as PDF



---

## 🛠️ Tech Stack

- **Backend:** Python Django  
- **Frontend:** HTML, CSS, JavaScript (can be extended with React)  
- **PDF Extraction:** PyMuPDF / PDFMiner / Custom Parsing  
- **PDF Generation:** ReportLab / WeasyPrint / xhtml2pdf  

---

## 🚀 Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/lesson-plan-management.git
   cd lesson-plan-management
   python -m venv venv
  source venv/bin/activate   # or venv\Scripts\activate for Windows
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver```
### To Access the app in your browser
```http://127.0.0.1:8000```

### Folder Structure
lesson-plan-management/
├── myapp/                  # Main Django app
├── templates/             # HTML Templates
├── static/                # Static Files (CSS/JS)
├── obe2                 # actual backend Logic
├── requirements.txt       # Python dependencies
├── manage.py
└── README.md

### If you have any Queries please reach out to me at "suahmakurella@gmail.com"

