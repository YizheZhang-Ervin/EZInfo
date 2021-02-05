# EZ_Info
EZ_Info  
  
# Run
cd frontend  
npm install  
npm run build  
cd backend  
workon env_develop  or source ./activate  
move temp_static folder contents to static folder  
pip install -r requirements.txt  
python manage.py runserver  
  
# Features 
- Welcome Page  
- About me  
- Visualization: Online Coding with output and charts  
- Visualization: CandleStick Charts  
- Tools: Geolocation with location  
- Tools: Translator   
- Tools: Excel with IO/New/ComputeExpression  
- Tools: VideoChat + Video Player with drag/drop + Status parameters  
- Resources: Useful Links    
  
# Architecture  
Front End: Vue CLI + Vue router + ElementUI  
Node Modules: Echarts + PeerJS  
Back End: Django RESTful + Mysql  
Python Libs: translate  
  
## BackEnd  
### install django framework
pip install django  
pip install djangorestframework  
pip install django-cors-headers   
pip install pymysql  
pip install sqlalchemy  
pip install pandas  
pip install translate  
pip install tushare  
  
### start project
django-admin startproject xxProject  
python manage.py startapp xxApp  

### other commands
python manage.py collectstatic  
python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser(ez-ez)  
python manage.py runserver  
   
### Dependency List  
Dependency libs: pipreqs ./   

## FrontEnd
### install 
npm install vue-cli  
npm install vue-router  
npm install element-ui  
npm install echarts  
npm install axios  
  
### start project  
vue create xxPrj  
  
### other commands  
vue ui -> set publicpath: /static/   
npm install  
npm serve   
npm build  
  