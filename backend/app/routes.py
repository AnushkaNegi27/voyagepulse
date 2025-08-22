from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, StreamingResponse
from app.services import parse_document, extract_events
import io
import pandas as pd
import json

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await parse_document(file)
    events = extract_events(content)
    return JSONResponse(content={"events": events})

@router.post("/download/json")
async def download_json(file: UploadFile = File(...)):
    content = await parse_document(file)
    events = extract_events(content)
    data = json.dumps(events, indent=2)
    return StreamingResponse(io.BytesIO(data.encode()), media_type="application/json", headers={
        "Content-Disposition": "attachment; filename=events.json"
    })

@router.post("/download/csv")
async def download_csv(file: UploadFile = File(...)):
    content = await parse_document(file)
    events = extract_events(content)
    df = pd.DataFrame(events)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = io.BytesIO(stream.getvalue().encode())
    return StreamingResponse(response, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=events.csv"
    })
