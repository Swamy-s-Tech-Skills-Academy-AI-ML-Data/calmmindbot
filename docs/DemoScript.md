# 🧘‍♂️ CalmMind Bot - Demo Script 🧘‍♂️

## Demo Overview

**Title**: Fine-tuning GPT Models for Mental Health Support: The CalmMind Bot Experience  
**Duration**: 45 minutes  
**Format**: In-person, demo-heavy presentation  
**Date**: May 3, 2025

## Presentation Outline (45 minutes)

### 1. Introduction (5 minutes)

- Welcome and introduce yourself
- Brief overview of mental health technology landscape
- Introduce the CalmMind project and its purpose
- Preview what will be demonstrated today

### 2. Project Architecture Overview (5 minutes)

- Present high-level architecture diagram
- Explain the two main components:
  - Model fine-tuning pipeline
  - Django web application
- Discuss technologies used (Django, OpenAI API, Tailwind CSS)

### 3. Understanding the Dataset (5 minutes)

- Show the mental health counseling conversations dataset
- Explain how the data is structured and processed
- Demonstrate loading a sample from the dataset

### 4. Model Fine-Tuning Demo (10 minutes)

- Open the Jupyter notebook (`notebooks/calmmindbot.ipynb`)
- Walk through the notebook sections:
  1. Data preparation and class structures
  2. Loading and exploring the dataset
  3. Creating the JSONL files for training
  4. Fine-tuning process with OpenAI API
  5. Testing the fine-tuned model

### 5. Django Web Application Demo (10 minutes)

- Show the project structure in VS Code
- Explain the main Django components:
  - `calmmind_portal_main` project settings
  - `calmmind` app structure
  - Templates and static files
- Live demo of the web interface:
  - Start the Django server
  - Navigate through the UI
  - Show the chat interface
  - Demonstrate bot responses

### 6. Comparison and Evaluation (5 minutes)

- Compare responses from:
  - Standard GPT model
  - Fine-tuned model
- Discuss improvements in context understanding and empathy
- Show sample evaluation metrics

### 7. Q&A and Next Steps (5 minutes)

- Open floor for questions
- Discuss potential improvements and extensions
- Share resources for attendees

## Detailed Demo Steps

### 1. Environment Setup (Pre-demo)

```bash
# Activate virtual environment
cd d:\STSAAIMLDT\calmmindbot
.venv\Scripts\activate

# Ensure requirements are installed
pip install -r requirements.txt

# Verify OpenAI API key is set in .env file
```

### 2. Jupyter Notebook Walkthrough

1. **Open Jupyter Lab/Notebook**:

```bash
cd d:\STSAAIMLDT\calmmindbot
jupyter lab
```

2. **Navigate to `notebooks/calmmindbot.ipynb`**

3. **Key cells to demonstrate**:
   - Installing packages (skip execution)
   - Importing libraries
   - RoleType, Role, and Message class definitions
   - Dataset loading and exploration
   - Training data preparation
   - Fine-tuning job creation
   - Model testing and comparison

### 3. Django Application Demo

1. **Start the Django server**:

```bash
cd d:\STSAAIMLDT\calmmindbot\src
python manage.py runserver
```

2. **Open browser** at [http://127.0.0.1:8000](http://127.0.0.1:8000)

3. **Demonstrate chat interface**:

   - Show UI components
   - Send sample messages
   - Highlight bot responses
   - Explain how responses are generated

4. **Sample queries to demonstrate**:
   - "Every winter I find myself getting sad because of the weather. How can I fight this?"
   - "I've been feeling anxious about my upcoming job interview. Any advice?"
   - "What are some simple mindfulness techniques I can practice daily?"
   - "I'm having trouble sleeping lately. What can I do to improve my sleep?"
   - "I've been feeling overwhelmed with work and personal commitments. How can I manage stress better?"

### 4. Code Walkthrough

1. **Key files to highlight**:

   - `src/calmmind/views.py` - Backend logic for chat processing
   - `src/calmmind/templates/calmmind/chat.html` - Chat interface
   - `src/calmmind_portal_main/settings.py` - Project settings
   - `data/train.jsonl` - Training data format

2. **Explain key code snippets**:
   - OpenAI API integration
   - Chat processing logic
   - Template rendering
   - Response handling

## Presentation Tips

1. **Before the Demo**:

   - Test all components
   - Ensure OpenAI API key is valid
   - Have sample queries ready
   - Prepare fallback screenshots in case of connection issues

2. **During the Demo**:

   - Speak clearly and at a moderate pace
   - Highlight practical applications
   - Emphasize the value for mental health support
   - Be prepared to explain technical concepts in simple terms

3. **Visual Aids**:
   - Have the README open for reference
   - Use VS Code to navigate code
   - Show UI screenshots in case live demo has issues

## Backup Plan

In case of technical difficulties:

- Have screenshots of key screens
- Prepare a video recording of the demo
- Have sample outputs ready to display

## Follow-up Resources

- GitHub repository link
- Documentation links:
  - OpenAI API documentation
  - Django documentation
  - Mental health datasets
- Your contact information for questions

---

_Note: This script is a guideline and can be adjusted based on audience engagement and time constraints during the presentation._
