# 🧘‍♂️ Calm Mind – AI Powered Mental Health Counseling bot 🧘‍♂️

A Django-based AI-powered mental health counseling chatbot using OpenAI.

---

## 🌟 Overview

**CalmMindBot** is a conversational chatbot designed to provide empathetic, AI-driven support for mental health and emotional well-being. Built with **Django**, **OpenAI’s NLP**, and a user-friendly **HTML/CSS/JavaScript** interface, it enables secure, real-time conversations to help users feel heard, supported, and guided.

## 🔧 Tech Stack

- **Backend:** Django (Python)
- **AI Engine:** OpenAI API (GPT-based models)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment Ready:** Scalable and secure for real-world use

## 🚀 Key Features

- 💬 **Conversational AI** for mental health support
- 🧠 **Context-aware responses** powered by OpenAI
- 🔒 **Secure, scalable Django backend**
- 🌐 **Responsive web interface**
- 🛠️ **Easily customizable** for future enhancements

## 📦 Deliverables

- ✅ Fully functional Django web app with real-time AI chatbot
- ✅ Seamless OpenAI integration for rich NLP-based conversations
- ✅ Flexible foundation for future mental health tech innovations

## 💡 Vision

CalmMindBot is built with compassion and cutting-edge technology to bridge the gap between emotional support and digital accessibility—making mental health care more approachable, one chat at a time.

## Reference(s)

> 1. [Datasets: Mental Health Counseling Conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
> 1. [Favicon](https://favicon.io/emoji-favicons/)
> 1. [OpenAI API](https://platform.openai.com/docs/api-reference/chat/create)
> 1. [Django](https://www.djangoproject.com/)
> 1. [Tailwind CSS](https://tailwindcss.com/docs/installation)

## Prompts

```text
Every winter I find myself getting sad because of the weather. How can I fight this?
```

## UI First Look

![UI First Look](./docs/images/UIFirstLook.PNG)

## Project Setup

```powershell
python --version
pip --version
(.venv) PS D:\STSAAIMLDT\calmmindbot> python --version
Python 3.12.5
(.venv) PS D:\STSAAIMLDT\calmmindbot> pip --version
pip 25.0.1 from D:\STSAAIMLDT\calmmindbot\.venv\Lib\site-packages\pip (python 3.12)
(.venv) PS D:\STSAAIMLDT\calmmindbot>

pip install virtualenv
python -m venv .venv
.venv/Scripts/activate
python -m pip install --upgrade pip

pip install flask openai python-dotenv flask_sqlalchemy

pip freeze > requirements.txt
pip install -r .\requirements.txt
```

## Overview

CalmMindBot is an AI-driven chatbot designed to provide empathetic and insightful mental health support. Built using **Django**, **OpenAI’s NLP models**, and web technologies (**HTML, CSS, JavaScript**), it enables users to engage in meaningful conversations, offering guidance, emotional support, and wellness resources.

## **Project Scope**

This project consists of two main phases:

1. **AI Model Training** – Utilizing OpenAI’s API to equip the chatbot with intelligent, context-aware responses tailored to mental health concerns.
2. **Django Integration** – Embedding the trained model into a secure, scalable Django web application for real-time user interactions.

## **Key Features**

✔️ AI-powered chatbot for mental health counseling  
✔️ OpenAI-driven NLP for thoughtful, context-aware responses  
✔️ Secure and scalable **Django framework**  
✔️ User-friendly web interface (**HTML, CSS, JavaScript**)  
✔️ Customizable chatbot behavior for personalized interactions

## **Project Description**

This project develops an AI-powered mental health chatbot using OpenAI's API and Django. The chatbot provides empathetic, real-time support through meaningful conversations, addressing diverse mental health concerns. It combines advanced NLP with a secure, scalable web application to deliver a user-friendly tool for mental well-being.

## **Installation & Usage**

1. Clone the repository:

   ```bash
   git clone https://github.com/vishipayyallore/CalmMindBot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CalmMindBot
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django server:

   ```bash
   python manage.py runserver
   ```

5. Access the chatbot in your browser and start a conversation!

## **Data Files**

The `data` folder contains the following files:

1. **`train.jsonl`**: This file stores the training dataset in JSONL format, which is used to fine-tune the chatbot model. Each line in the file represents a JSON object containing structured data for training.

2. **`validation.jsonl`**: This file contains the validation dataset in JSONL format, used to evaluate the chatbot model's performance during fine-tuning. Each line represents a JSON object for validation.

> **Note**: These files are excluded from version control using `.gitignore` to ensure sensitive or large data is not committed to the repository.

Here's a clean, **consolidated version** of your CalmMindBot README that combines clarity, structure, and professionalism, while staying concise and impactful:

---

## Creation of a Virtual Environment and clammind_main project

### 1. Create a Virtual Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/Swamy-s-Tech-Skills-Academy-AI-ML-Data/calmmindbot.git
   cd calmmindbot
   ```

2. Create a Virtual Environment and activate it:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   pip freeze  # Should show no packages installed
   ```

3. Install dependencies:

   ```bash
   pip install django
   pip install --upgrade pip
   pip install python-dotenv
   pip freeze # It should show the installed packages
   pip freeze > requirements.txt
   ```

4. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. Create the Django project:

> 1. (.venv) PS D:\STSAAIMLDT\calmmindbot\src>
> 2. Create a new Django project

```bash
    django-admin startproject calmmind_portal_main .
    cd src
```

6. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Creating the "calmmind" App

To create the `calmmind` app for managing student-related features, follow these steps:

1. Navigate to the `src` directory:

   ```bash
   cd src
   ```

2. Create the `calmmind` app using Django's `startapp` command:

   ```bash
   python manage.py startapp calmmind
   ```

3. Add the `calmmind` app to the `INSTALLED_APPS` list in `student_portal_main/settings.py`:

   ```python
   INSTALLED_APPS = [
       ...existing apps...
       'calmmind',
   ]
   ```

4. Define models for the `calmmind` app in `calmmind/models.py`.

5. Run migrations to apply any changes:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create views, serializers, and URLs for the `calmmind` app as needed.

> 1. [calmmind endpoints](http://127.0.0.1:8000/calmmind/) - This URL will be used to access the student portal.

# CalmMindBot

---

## 🛠️ Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/vishipayyallore/CalmMindBot.git

# 2. Navigate to the project folder
cd CalmMindBot

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Django development server
python manage.py runserver
```

👉 Open your browser and visit: [http://127.0.0.1:8000](http://127.0.0.1:8000) to start a session.

---
