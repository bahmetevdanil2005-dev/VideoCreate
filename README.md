# VideoCreate

AI-directed motion-design video generation. A pnpm monorepo with separate web, API, renderer, and shared scenario contract.

## Architecture
- `apps/web`: Next.js interface and Remotion Player preview.
- `apps/api`: FastAPI prompt-to-scenario API and validation.
- `apps/renderer`: Remotion compositions and MP4 rendering.
- `packages/video-schema`: versioned scenario contract shared by UI and renderer.

AI produces validated data, never executable code. Only registered renderer components execute. This keeps animation upgrades independent from prompts and UI.

## Requirements
Node.js 20+, pnpm 10+, Python 3.11+, FFmpeg.

## Run
```bash
pnpm install
pnpm --filter @videocreate/web dev
```
In another terminal:
```bash
cd apps/api && python -m venv .venv && source .venv/bin/activate
pip install -e . && uvicorn videocreate_api.main:app --reload --port 8000
```
Renderer: `pnpm --filter @videocreate/renderer studio`.

Copy `apps/api/.env.example` to `.env` and set GEMINI_API_KEY for AI generation. Without a key, a deterministic demo scenario is returned.
