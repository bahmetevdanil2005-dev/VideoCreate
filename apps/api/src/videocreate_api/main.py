from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .schemas import DirectorRequest, DirectorResponse
from .director import create_scenario

app = FastAPI(title="VideoCreate API", version="0.1.0")
origins = [item.strip() for item in settings.allowed_origins.split(",") if item.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["GET","POST"], allow_headers=["Content-Type","Authorization"])

@app.get("/health")
async def health():
    return {"ok": True, "service": "videocreate-api", "aiConfigured": bool(settings.gemini_api_key)}

@app.post("/api/v1/director", response_model=DirectorResponse)
async def director(request: DirectorRequest):
    try:
        scenario, source = await create_scenario(request)
        return DirectorResponse(scenario=scenario, source=source)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Не удалось подготовить сценарий: {str(exc)[:400]}") from exc
