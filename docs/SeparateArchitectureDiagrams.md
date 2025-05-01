# CalmMind Bot - Separate Architecture Components

This document provides focused Mermaid diagrams for three key aspects of the CalmMind architecture: Admin Flow, Django Application, and User Flow. You can use these diagrams separately in your presentation to focus on specific aspects of the system.

## A. Admin Flow Diagram

This diagram illustrates the workflow for administrators (developers) fine-tuning and managing the AI model.

```mermaid
graph TD
    Admin[Admin/Developer] --> Jupyter[Jupyter Notebook]
    Jupyter --> DataPrep[Data Preparation]
    DataPrep --> HF[HuggingFace Dataset]
    HF --> Process[Process Dataset]
    Process --> JSONL[Generate JSONL Files]
    JSONL --> FineTune[Fine-Tune Model via API]
    
    FineTune --> OpenAI[OpenAI API]
    OpenAI --> Model[Fine-tuned Model]
    Model --> Eval[Evaluate Model]
    Eval --> Deploy[Deploy to Production]
    
    style Admin fill:#4299E1,stroke:#2C5282,color:white
    style Jupyter fill:#4299E1,stroke:#2C5282,color:white
    style DataPrep fill:#4299E1,stroke:#2C5282,color:white
    style HF fill:#F6AD55,stroke:#C05621,color:white
    style Process fill:#4299E1,stroke:#2C5282,color:white
    style JSONL fill:#F6AD55,stroke:#C05621,color:white
    style FineTune fill:#4299E1,stroke:#2C5282,color:white
    style OpenAI fill:#805AD5,stroke:#553C9A,color:white
    style Model fill:#805AD5,stroke:#553C9A,color:white
    style Eval fill:#4299E1,stroke:#2C5282,color:white
    style Deploy fill:#48BB78,stroke:#2F855A,color:white
```

## B. Django Application Architecture

This diagram focuses on the internal structure of the Django application and how its components interact.

```mermaid
graph TD
    Client[Web Browser] --> URLs[URLs/Routes]
    URLs --> Views[Views]
    Views --> Templates[Templates]
    Templates --> Client
    
    Views --> Models[Models]
    Models --> DB[(Database)]
    
    Views --> OpenAIAPI[OpenAI API Client]
    OpenAIAPI --> FineTunedModel[Fine-tuned Model]
    FineTunedModel --> OpenAIAPI
    OpenAIAPI --> Views
    
    subgraph Django Application
        URLs
        Views
        Models
        Templates
    end
    
    style Client fill:#4299E1,stroke:#2C5282,color:white
    style URLs fill:#48BB78,stroke:#2F855A,color:white
    style Views fill:#48BB78,stroke:#2F855A,color:white
    style Templates fill:#48BB78,stroke:#2F855A,color:white
    style Models fill:#48BB78,stroke:#2F855A,color:white
    style DB fill:#F6AD55,stroke:#C05621,color:white
    style OpenAIAPI fill:#805AD5,stroke:#553C9A,color:white
    style FineTunedModel fill:#805AD5,stroke:#553C9A,color:white
    
    classDef django fill:#48BB78,stroke:#2F855A,color:white
    class URLs,Views,Models,Templates django
```

## C. User Flow Diagram

This diagram shows the user experience flow and how user interactions are processed through the system.

```mermaid
sequenceDiagram
    participant User
    participant Browser as Web Browser
    participant Django as Django Backend
    participant OpenAI as OpenAI API
    participant Model as Fine-tuned Model
    
    User->>Browser: Enter message
    Browser->>Django: Send HTTP request
    Django->>OpenAI: Forward request to API
    OpenAI->>Model: Process with fine-tuned model
    Model->>OpenAI: Generate response
    OpenAI->>Django: Return response
    Django->>Browser: Format and send response
    Browser->>User: Display bot message
    
    Note over User,Browser: User Interface Layer
    Note over Django: Application Layer
    Note over OpenAI,Model: AI Processing Layer
```

## Quick Steps for Using These Diagrams

1. Visit [Mermaid Live Editor](https://mermaid.live/)
2. Copy and paste each Mermaid code block separately
3. Download each diagram as PNG or SVG
4. Add each diagram to your presentation slides

## Presentation Tips

When presenting these diagrams:

1. **Admin Flow**: Use this when explaining the model fine-tuning process and how the model is prepared for the application.

2. **Django Application**: Present this when diving into the technical architecture of your web application, explaining how the components interact.

3. **User Flow**: Show this when demonstrating the user experience, walking through what happens from when a user types a message to when they receive a response.

You can also consider creating a slide that shows all three diagrams side by side to give a complete picture of your system, then focus on each component in subsequent slides.