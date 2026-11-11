export const SCHEMA_VERSION = 1 as const;
export type VideoFormat = "9:16" | "16:9" | "1:1";
export type Background = "ink" | "paper" | "lime" | "grid";
export type TextAnimation = "rise" | "pop" | "wipe" | "typewriter";
export type Transition = "cut" | "flash" | "wipe" | "zoom";
export interface TextLayer { id:string; type:"text"; text:string; x:number; y:number; fontSize:number; color:"white"|"ink"|"lime"; weight:600|700|800|900; animation:TextAnimation; startFrame:number; durationInFrames:number; highlight?:string }
export interface ShapeLayer { id:string; type:"shape"; shape:"circle"|"bar"|"ring"; x:number; y:number; size:number; color:"white"|"ink"|"lime"; startFrame:number; durationInFrames:number }
export type VideoLayer = TextLayer | ShapeLayer;
export interface VideoScene { id:string; durationInFrames:number; background:Background; transition:Transition; layers:VideoLayer[] }
export interface VideoScenario { schemaVersion:typeof SCHEMA_VERSION; title:string; format:VideoFormat; fps:number; width:number; height:number; scenes:VideoScene[] }
export const DEMO_SCENARIO:VideoScenario={schemaVersion:1,title:"The next frame",format:"9:16",fps:30,width:1080,height:1920,scenes:[
{id:"hook",durationInFrames:75,background:"ink",transition:"flash",layers:[
{id:"a",type:"text",text:"ИДЕЯ",x:.5,y:.39,fontSize:150,color:"white",weight:900,animation:"pop",startFrame:0,durationInFrames:24},
{id:"b",type:"text",text:"СТАНОВИТСЯ",x:.5,y:.49,fontSize:74,color:"lime",weight:900,animation:"wipe",startFrame:12,durationInFrames:30},
{id:"c",type:"text",text:"ВИДЕО.",x:.5,y:.59,fontSize:148,color:"white",weight:900,animation:"rise",startFrame:24,durationInFrames:26}]},
{id:"motion",durationInFrames:90,background:"grid",transition:"wipe",layers:[
{id:"ring",type:"shape",shape:"ring",x:.5,y:.43,size:470,color:"lime",startFrame:0,durationInFrames:80},
{id:"d",type:"text",text:"НЕ ШАБЛОН.",x:.5,y:.43,fontSize:106,color:"white",weight:900,animation:"pop",startFrame:12,durationInFrames:28},
{id:"e",type:"text",text:"МОУШН-ДИЗАЙН",x:.5,y:.53,fontSize:62,color:"lime",weight:900,animation:"rise",startFrame:34,durationInFrames:30}]},
{id:"end",durationInFrames:75,background:"lime",transition:"flash",layers:[
{id:"f",type:"text",text:"ТВОЯ ИДЕЯ.",x:.5,y:.43,fontSize:128,color:"ink",weight:900,animation:"wipe",startFrame:0,durationInFrames:26},
{id:"g",type:"text",text:"ТВОЁ ВИДЕО.",x:.5,y:.53,fontSize:92,color:"ink",weight:900,animation:"rise",startFrame:20,durationInFrames:30}]}]};
export const getScenarioDurationInFrames=(s:VideoScenario)=>s.scenes.reduce((n,x)=>n+x.durationInFrames,0);
export function validateScenario(input:unknown):VideoScenario { if(!input||typeof input!=="object")throw Error("Scenario must be an object"); const s=input as VideoScenario; if(s.schemaVersion!==1)throw Error("Unsupported schema version"); if(!Array.isArray(s.scenes)||s.scenes.length<1||s.scenes.length>40)throw Error("Scenario must have 1–40 scenes"); if(!["9:16","16:9","1:1"].includes(s.format)||![24,25,30,50,60].includes(s.fps))throw Error("Unsupported format or FPS"); for(const scene of s.scenes){if(!Number.isInteger(scene.durationInFrames)||scene.durationInFrames<24||scene.durationInFrames>600||!Array.isArray(scene.layers)||scene.layers.length>12)throw Error("Invalid scene duration or layers"); for(const l of scene.layers){if(!Number.isFinite(l.x)||l.x<0||l.x>1||!Number.isFinite(l.y)||l.y<0||l.y>1||!Number.isInteger(l.startFrame)||l.startFrame<0||!Number.isInteger(l.durationInFrames)||l.durationInFrames<1)throw Error("Invalid layer geometry or timing"); if(l.type==="text"&&(typeof l.text!=="string"||l.text.length>160))throw Error("Invalid text layer");}} return s; }
