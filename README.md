# YZGame  
Unity Game  
  
# Architecture  
Front End: Vue+ElementUI+Axios  
Back End: Flask  
Game Engine: Unity  
  
# Run  
python -m flask run  
  
# If Update Game  
1. change static/game1/index.html  
<link rel="stylesheet" href={{ url_for('static', filename='game1/TemplateData/style.css')}}>    
<script src={{ url_for('static', filename="game1/TemplateData/UnityProgress.js")}}></script>    
<script src={{ url_for('static', filename="game1/Build/UnityLoader.js")}}></script>    
<script>var unityInstance = UnityLoader.instantiate("unityContainer", "static/game1/Build/Build.json", {onProgress: UnityProgress});</script>   
  
2. cut static/game1/index.html and paste static/game1/html  
  
# If Update FrontEnd  
1. cd yzgame  > npm run build  
  
2. static/index.html
each href and src add /static  
