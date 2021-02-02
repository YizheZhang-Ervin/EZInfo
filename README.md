# YZGame  
Unity Game  
  
# Features 
- Online Coding with output and charts  
- Translator  
- Unity Games  
- FinTech Algorithms  
- VideoChat

# Architecture  
Front End: Vue CLI + Vue router + ElementUI + Axios + Echarts + PeerJS  
Back End: Flask  
Game Engine: Unity  
  
# Run  
python -m flask run  
  
# If Update Game  
1. create new folder "gamexx" under folder "static"  
  
2. put folder "TemplateData" & "Build" in folder "gamexx"  
  
# If Update FrontEnd  
1. cd yzgame  > npm run build  
  
2. move all files under temp_static to static (except favicon.svg/game1/gam1.html)  
  
3. adjust each href and src add /static in index.html  
  