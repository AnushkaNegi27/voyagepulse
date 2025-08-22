import pdfplumber
import docx
import re
from typing import List, Dict

# Step A: Parse file
async def parse_document(file) -> str:
    text = ""
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    else:
        raise ValueError("Unsupported file format")
    return text

# Step B: Extract events (basic regex for times)
def extract_events(text: str) -> List[Dict]:
    events = []
    lines = text.split("\n")

    time_pattern = r"(\d{1,2}:\d{2})"  # matches times like 10:00, 14:30

    for line in lines:
        times = re.findall(time_pattern, line)
        if times:
            events.append({
                "event": line.strip(),
                "start_time": times[0] if len(times) > 0 else None,
                "end_time": times[1] if len(times) > 1 else None
            })
    return events
