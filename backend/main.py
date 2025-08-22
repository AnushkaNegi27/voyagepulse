from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="VoyagePulse Backend - SoF Event Extractor")

# Register routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "VoyagePulse Backend Running 🚀"}
