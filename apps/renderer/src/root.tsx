import {Composition} from "remotion";
import {DEMO_SCENARIO,getScenarioDurationInFrames} from "@videocreate/video-schema";
import {VideoComposition} from "./VideoComposition";
export const RemotionRoot:React.FC=()=> <Composition id="Main" component={VideoComposition} durationInFrames={getScenarioDurationInFrames(DEMO_SCENARIO)} fps={DEMO_SCENARIO.fps} width={DEMO_SCENARIO.width} height={DEMO_SCENARIO.height} defaultProps={{scenario:DEMO_SCENARIO}}/>;
