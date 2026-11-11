import json
import httpx
from .config import settings
from .schemas import DirectorRequest, Scenario
from .demo import demo_scenario

SYSTEM = """You are a senior motion-design creative director. Return only JSON matching the supplied scenario schema. Create a premium kinetic typography short, not a slideshow. Use concise Russian copy, 1-5 words per visual beat, varied compositions, strong hierarchy, dark ink backgrounds with lime accents and occasional paper/lime impact frames. Use only registered layer types text and shape; allowed animations rise/pop/wipe/typewriter. Keep all layer timings inside their scene. Use 5-12 scenes for a 20 second video. Never invent factual claims. JSON keys: schemaVersion,title,format,fps,width,height,scenes. Each scene: id,durationInFrames,background,transition,layers. Text layer: id,type='text',text,x,y,fontSize,color,weight,animation,startFrame,durationInFrames. Shape layer: id,type='shape',shape,x,y,size,color,startFrame,durationInFrames."""

async def create_scenario(req: DirectorRequest) -> tuple[Scenario,str]:
    if not settings.gemini_api_key:
        return Scenario.model_validate(demo_scenario(req.format)), "demo"
    prompt = f"BRIEF: {req.brief}\nFORMAT: {req.format}\nDURATION: {req.durationSeconds} seconds at 30 fps. Total scene duration should be close to {req.durationSeconds*30} frames."
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.gemini_model}:generateContent"
    payload = {"systemInstruction":{"parts":[{"text":SYSTEM}]},"contents":[{"role":"user","parts":[{"text":prompt}]}],"generationConfig":{"responseMimeType":"application/json","temperature":0.85,"maxOutputTokens":12000}}
    async with httpx.AsyncClient(timeout=httpx.Timeout(90,connect=10)) as client:
        response = await client.post(url,params={"key":settings.gemini_api_key},json=payload)
        response.raise_for_status()
    raw = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    data = json.loads(raw)
    data["format"] = req.format
    data["width"],data["height"] = (1080,1920) if req.format=="9:16" else (1920,1080) if req.format=="16:9" else (1080,1080)
    scenario = Scenario.model_validate(data)
    total = sum(scene.durationInFrames for scene in scenario.scenes)
    if total < req.durationSeconds*30*0.75 or total > req.durationSeconds*30*1.25:
        raise ValueError("AI returned a scenario with an invalid total duration; please retry")
    return scenario, "gemini"
