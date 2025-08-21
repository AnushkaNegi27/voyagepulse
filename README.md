# VoyagePulse

VoyagePulse is an intelligent system designed to streamline SoF (Statement of Facts) Event Extraction – Laytime Intelligence.
It helps shipping companies and operators by automatically extracting operational events from SoF documents (PDF/Word), ensuring accuracy, consistency, and efficiency.

🚢 Problem Statement

Thousands of SoF documents are generated daily worldwide, often in inconsistent formats.
These documents capture vital port operations like cargo loading, shifting, anchorage, etc., along with start and end times.

# Challenges

Format variations across different ports and agencies.

Risk of missed events due to unstructured data.

Manual processing delays affecting voyage performance.

# Our Solution – VoyagePulse

VoyagePulse provides an AI-driven system that:

📂 Accepts SoFs in PDF and Word formats.

🔍 Extracts all events with start & end times (template-agnostic).

🛑 Ensures no events are missed, regardless of formatting.

📊 Outputs structured data in JSON/CSV for downstream use.

🖥️ Includes a user-friendly web interface for uploads and reports.

# Why VoyagePulse is Unique

Unlike existing SoF parsing tools, VoyagePulse goes beyond basic extraction by:

Integrating Azure OpenAI + spaCy pipelines for context-aware event detection.

Supporting real-time validation to prevent missing critical port activities.

Providing visual dashboards & analytics for better laytime intelligence.

Designed with scalable cloud infrastructure (Azure) for enterprise adoption.

# Core Tech Stack

🔹 Frontend (User Interface)

HTML5, CSS3, JavaScript (ES6+)

React.js or Vue.js – for responsive, component-based UIs

Bootstrap / TailwindCSS – for styling

🔹 Backend (Application Logic)

PHP (Laravel or Symfony) – for scalable web applications (preferred at IME)

Node.js (optional) – for asynchronous services / microservices

Python – for ML pipelines, document parsing, and NLP

🔹 Database & Storage

MySQL / PostgreSQL – relational data (contracts, voyages, events)

Azure Blob Storage / Amazon S3 – for uploading & storing documents

🔹 AI / Machine Learning / NLP Tools

Azure Cognitive Services – OCR, form recognition, document analysis

Azure OpenAI – summarization, clause matching, negotiation intelligence

spaCy, Transformers (Hugging Face) – event & clause extraction

Scikit-learn / TensorFlow – ML models (classification / prediction)

🔹 DevOps & Cloud Infrastructure

Microsoft Azure – hosting and cloud services

Azure Web Apps, Azure Functions, Azure SQL, Azure Logic Apps

GitHub Actions / Azure DevOps – CI/CD pipeline automation

# System Architecture Overview

The architecture is designed for modularity, scalability, and maintainability:

Client Layer (Frontend)

Web app for uploading SoF files, dashboards, and reports.

Communicates with backend via REST APIs.

Application Layer (Backend/API)

Endpoints for document processing, AI-based extraction, and authentication.

Queue system (Azure Queue Storage / Redis) for background processing.

Processing & Intelligence Layer

OCR + NLP pipelines for event detection.

AI models for summarization, clause mapping, and anomaly detection.

Database & Storage Layer

SQL database for structured voyage/event data.

Cloud storage for documents and outputs.

Caching (Redis/Memcached) for faster access.

Reporting & Export Layer

Export to JSON/CSV for integrations.

Automated PDF/Excel report generation.
