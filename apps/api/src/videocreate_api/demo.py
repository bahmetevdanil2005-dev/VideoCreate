def demo_scenario(fmt: str = "9:16") -> dict:
    width,height = (1080,1920) if fmt=="9:16" else (1920,1080) if fmt=="16:9" else (1080,1080)
    return {"schemaVersion":1,"title":"Идея становится видео","format":fmt,"fps":30,"width":width,"height":height,"scenes":[
      {"id":"hook","durationInFrames":75,"background":"ink","transition":"flash","layers":[
        {"id":"a","type":"text","text":"ИДЕЯ","x":0.5,"y":0.39,"fontSize":150,"color":"white","weight":900,"animation":"pop","startFrame":0,"durationInFrames":24},
        {"id":"b","type":"text","text":"СТАНОВИТСЯ","x":0.5,"y":0.49,"fontSize":74,"color":"lime","weight":900,"animation":"wipe","startFrame":12,"durationInFrames":30},
        {"id":"c","type":"text","text":"ВИДЕО.","x":0.5,"y":0.59,"fontSize":148,"color":"white","weight":900,"animation":"rise","startFrame":24,"durationInFrames":26}]},
      {"id":"motion","durationInFrames":90,"background":"grid","transition":"wipe","layers":[
        {"id":"ring","type":"shape","shape":"ring","x":0.5,"y":0.43,"size":470,"color":"lime","startFrame":0,"durationInFrames":80},
        {"id":"d","type":"text","text":"НЕ ШАБЛОН.","x":0.5,"y":0.43,"fontSize":106,"color":"white","weight":900,"animation":"pop","startFrame":12,"durationInFrames":28},
        {"id":"e","type":"text","text":"МОУШН-ДИЗАЙН","x":0.5,"y":0.53,"fontSize":62,"color":"lime","weight":900,"animation":"rise","startFrame":34,"durationInFrames":30}]},
      {"id":"end","durationInFrames":75,"background":"lime","transition":"flash","layers":[
        {"id":"f","type":"text","text":"ТВОЯ ИДЕЯ.","x":0.5,"y":0.43,"fontSize":128,"color":"ink","weight":900,"animation":"wipe","startFrame":0,"durationInFrames":26},
        {"id":"g","type":"text","text":"ТВОЁ ВИДЕО.","x":0.5,"y":0.53,"fontSize":92,"color":"ink","weight":900,"animation":"rise","startFrame":20,"durationInFrames":30}]}]}
