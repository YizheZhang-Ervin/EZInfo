# EZ_Info
  
## Features 
- Welcome Page  
- About Me   
- Visualization: CandleStick Charts  
- Tools: Geolocation with location  
- Tools: Translator   
- Tools: Excel with IO/New/ComputeExpression  
- Tools: VideoChat + Video Player with drag/drop + Status parameters  
- Tools: Manager login with Terminals of Python/Sql(update stock data)/JavaScript/HTML  
- Resources: Useful Links  
  
## Infrastructure  
Front End: Vue + ElementUI + Axios + Echarts + PeerJS  
Back End: Django RESTful + Mysql + translate  
  
## Run
cd frontend > npm install  
npm run build   
move files in backend/temp_static folder to backend/static folder  
workon env_develop  or source ./activate  
cd backend > pip install -r requirements.txt  
python manage.py runserver  
  
## FrontEnd: Vue
### start project  
vue create xxPrj  
  
### Modules
npm install vue-cli  
npm install vue-router  
npm install element-ui  
npm install echarts  
npm install axios  
  
### Other Commands  
vue ui -> set publicpath: /static/   
npm install  
npm serve   
npm build  
  
## BackEnd: Django  
### Start Project  
django-admin startproject xxSite  
python manage.py startapp xxApp  
  
### Libs
pip install django  
pip install djangorestframework  
pip install django-cors-headers   
pip install pymysql  
pip install sqlalchemy  
pip install pandas  
pip install translate  
pip install tushare  
  
### Database & Static files  
cd SharingBike  
python manage.py collectstatic  
python manage.py makemigrations
python manage.py migrate  
  
### Backend Management  
python manage.py createsuperuser(name:ez,password:ez)  
python manage.py runserver  
Browser: http://127.0.0.1:8000/  
  
### Dependency List  
Virtual Env libs: pip freeze > requirements.txt   
Dependency libs: pipreqs ./  
pip install -r requirements.txt   
  
