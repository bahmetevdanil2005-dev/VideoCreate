# Architecture decisions

## Trust boundary
The LLM is an untrusted creative planner. It returns JSON only. FastAPI validates the payload against strict Pydantic models; the shared TypeScript contract validates the same shape for client-side use. No generated JavaScript, HTML, CSS, SVG, or arbitrary component names are executed.

## Services
- Web: Next.js app, project brief, format selection, Remotion Player preview.
- API: FastAPI, provider adapter, prompt orchestration, schema validation.
- Renderer: Remotion composition library and CLI render entrypoint.
- Schema: versioned data contract shared across frontend and renderer.

## Next milestones
1. Add a real export endpoint/worker using Remotion renderMedia and a persistent job queue.
2. Expand the renderer registry with reusable text, transition, shape, UI-mockup and asset components.
3. Add TTS/audio tracks and word-level caption timing.
4. Add media asset storage, project persistence, retries and render QA.
5. Add visual regression tests and golden-frame fixtures for animation components.

## Important implementation rule
New effects are added as typed, registered components. The AI may select only effect IDs advertised by the schema; it cannot author code for the renderer.
