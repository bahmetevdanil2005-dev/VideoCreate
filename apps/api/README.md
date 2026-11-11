# VideoCreate API

FastAPI service for AI-directed scenario generation. Configuration is read from environment variables (see .env.example). The Gemini key is server-side only and must never be exposed to the browser.

- GET /health
- POST /api/v1/director

The API validates every generated scenario with Pydantic models before returning it. When GEMINI_API_KEY is absent, it returns a deterministic demo scenario for local UI development.
