# 🧘‍♂️ CalmMind - AI-Powered Mental Health Counseling Bot 🧘‍♂️

A `Django-based AI chatbot` leveraging `OpenAI's NLP` to offer empathetic mental health support.

## 🌟 Overview

**CalmMind** is a conversational chatbot designed to provide empathetic, AI-driven support for mental health and emotional well-being. Built with `Django`, `OpenAI's NLP`, and a user-friendly `HTML/CSS/JavaScript` interface, it enables secure, real-time conversations to help users feel heard, supported, and guided.

## 🔧 Tech Stack

- **Backend:** Django (Python)
- **AI Engine:** OpenAI API (GPT-based models with fine-tuning)
- **Frontend:** HTML, CSS, JavaScript (with Tailwind CSS)
- **Data Processing:** Jupyter Notebooks for model training

## 🚀 Key Features

- 💬 **Conversational AI** for mental health support
- 🧠 **Context-aware responses** powered by fine-tuned OpenAI models
- 🔒 **Secure, scalable Django backend**
- 🌐 **Responsive web interface**
- 🛠️ **Easily customizable** for future enhancements

## 🎨 UI Preview

![UI First Look](./docs/images/UIFirstLook.PNG)

## 🏗️ Project Structure

The project is organized into the following components:

### 1. Django Web Application (`src/`)
- **Main Project:** `calmmind_portal_main`
- **App:** `calmmind` - Contains views, templates, and URLs for the chatbot interface
- **Templates:** Responsive UI with chat interface, navigation, and styling

### 2. Model Fine-tuning (`notebooks/`)
- **`calmmindbot.ipynb`:** Jupyter notebook for fine-tuning the OpenAI GPT model
- Processes mental health counseling datasets
- Creates and submits fine-tuning jobs to OpenAI
- Tests and validates the fine-tuned model

### 3. Training Data (`data/`)
- **`train.jsonl`:** Training dataset in JSONL format
- **`validation.jsonl`:** Validation dataset for model evaluation

## 🛠️ Installation & Setup

### 1. Clone & Setup Environment

```bash
# Clone the repository
git clone https://github.com/Swamy-s-Tech-Skills-Academy-AI-ML-Data/CalmMind.git
cd CalmMind

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file in the root directory with:

```
OPENAI_API_KEY=your_openai_api_key
```

### 3. Run the Django Server

```bash
cd src
python manage.py runserver
```

👉 **Access your chatbot** at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🧠 Model Fine-tuning

To fine-tune the OpenAI model:

1. Navigate to the `notebooks/` directory
2. Open `calmmindbot.ipynb` in Jupyter Notebook or Jupyter Lab
3. Follow the instructions in the notebook to:
   - Load and process the mental health counseling dataset
   - Prepare the data for fine-tuning
   - Submit the fine-tuning job to OpenAI
   - Test the fine-tuned model

## 📝 Sample Prompts

Try asking the bot questions like:
```
Every winter I find myself getting sad because of the weather. How can I fight this?
I've been feeling anxious about my upcoming job interview. Any advice?
What are some simple mindfulness techniques I can practice daily?
```

## 🤝 Contribution Guidelines

We welcome contributions to CalmMind! To contribute:

1. **Fork the repository** on GitHub
2. **Clone your fork** to your local machine
3. **Create a new branch** for your feature or bug fix
4. **Make your changes** and commit them with clear messages
5. **Push your changes** to your fork
6. **Submit a pull request** to the main repository

## 📋 Todo List

- [ ] Create a new Django app for external service logic
- [ ] Define API endpoints using Django REST Framework (DRF)
- [ ] Implement authentication for API endpoints
- [ ] Write unit tests for the application
- [ ] Implement session management for conversations
- [ ] Add support for conversation history

## 🌐 Deployment Instructions

To deploy CalmMind to a production environment:

1. **Set up a production server** (e.g., AWS, Azure, or Heroku)
2. **Configure environment variables** for sensitive data
3. **Run database migrations:** `python manage.py migrate`
4. **Collect static files:** `python manage.py collectstatic`
5. **Start the server** using a production-ready WSGI server (e.g., Gunicorn)

## 💡 Vision

CalmMind is built with compassion and cutting-edge technology to bridge the gap between emotional support and digital accessibility—making mental health care more approachable, one chat at a time.

## 📚 References

1. [Mental Health Counseling Conversations Dataset](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
2. [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/chat/create)
3. [Django Framework](https://www.djangoproject.com/)
4. [Tailwind CSS](https://tailwindcss.com/docs/installation)
5. [Favicon Source](https://favicon.io/emoji-favicons/)
