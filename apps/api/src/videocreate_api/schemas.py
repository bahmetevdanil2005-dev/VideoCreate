from typing import Literal, Annotated
from pydantic import BaseModel, Field, ConfigDict

Format = Literal["9:16", "16:9", "1:1"]
Color = Literal["white", "ink", "lime"]
class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
class TextLayer(StrictModel):
    id: str = Field(min_length=1, max_length=80)
    type: Literal["text"]
    text: str = Field(min_length=1, max_length=160)
    x: float = Field(ge=0, le=1)
    y: float = Field(ge=0, le=1)
    fontSize: int = Field(ge=12, le=300)
    color: Color
    weight: Literal[600,700,800,900]
    animation: Literal["rise","pop","wipe","typewriter"]
    startFrame: int = Field(ge=0)
    durationInFrames: int = Field(ge=1)
    highlight: str | None = None
class ShapeLayer(StrictModel):
    id: str = Field(min_length=1, max_length=80)
    type: Literal["shape"]
    shape: Literal["circle","bar","ring"]
    x: float = Field(ge=0, le=1)
    y: float = Field(ge=0, le=1)
    size: int = Field(ge=8, le=1000)
    color: Color
    startFrame: int = Field(ge=0)
    durationInFrames: int = Field(ge=1)
Layer = Annotated[TextLayer | ShapeLayer, Field(discriminator="type")]
class Scene(StrictModel):
    id: str
    durationInFrames: int = Field(ge=24, le=600)
    background: Literal["ink","paper","lime","grid"]
    transition: Literal["cut","flash","wipe","zoom"]
    layers: list[Layer] = Field(max_length=12)
class Scenario(StrictModel):
    schemaVersion: Literal[1] = 1
    title: str = Field(max_length=120)
    format: Format
    fps: Literal[24,25,30,50,60] = 30
    width: Literal[1080,1920] = 1080
    height: Literal[1080,1920] = 1920
    scenes: list[Scene] = Field(min_length=1,max_length=40)
class DirectorRequest(StrictModel):
    brief: str = Field(min_length=3,max_length=1800)
    format: Format = "9:16"
    durationSeconds: int = Field(default=20,ge=5,le=60)
class DirectorResponse(StrictModel):
    scenario: Scenario
    source: Literal["gemini","demo"]
