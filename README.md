# VoyagePulse – SoF Event Extractor & Laytime Intelligence

VoyagePulse is an intelligent system designed to streamline SoF (Statement of Facts) Event Extraction – Laytime Intelligence.
It helps shipping companies and operators by automatically extracting operational events from SoF documents (PDF/Word), ensuring accuracy, consistency, and efficiency.

## Problem Statement

Thousands of SoF documents are generated daily worldwide, often in inconsistent formats.
These documents capture vital port operations like cargo loading, shifting, anchorage, etc., along with start and end times.

### Challenges

Format variations across different ports and agencies

Risk of missed events due to unstructured data

Manual processing delays affecting voyage performance

### Our Solution – VoyagePulse

VoyagePulse provides an AI-driven system that:

📂 Accepts SoFs in PDF and Word formats

🔍 Extracts all events with start & end times (template-agnostic)

🛑 Ensures no events are missed, regardless of formatting

📊 Outputs structured data in JSON/CSV for downstream use

🖥️ Provides a simple user-friendly web interface for uploading files and previewing results


### Tech Stack (Used)

Frontend: HTML, CSS, JavaScript (ES6+)

Backend / Processing: Python

NLP / AI Tools: spaCy, Azure OpenAI

Output: JSON / CSV


### System Overview

Upload Layer: Users upload SoF PDF/Word documents via the web interface

Processing Layer: OCR + NLP pipelines detect events and extract start/end times

Output Layer: Structured data is generated in JSON/CSV format for reporting or further use


### Getting Started

Clone the repository:
```bash
git clone https://github.com/AnushkaNegi27/voyagepulse.git
cd voyagepulse

Install Python dependencies:
```bash
pip install -r requirements.txt

Run the application:
```bash
python app.py

Contributors

Anushka Negi

Abhinav Khatana
