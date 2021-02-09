from translate import Translator
from imp import reload
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,QueryDict
from django.views import View
from pathlib import Path
from django.shortcuts import render
from ezinfo.visualization import initEngine

BASE_DIR = Path(__file__).resolve().parent

# Common Response
# def index(request):
#     return render(request, 'index.html')

# RESTful Response
# class RestApi(View):
#     @csrf_exempt
#     def dispatch(self, request, *args, **kwargs):
#         if request.method.lower() in self.http_method_names:
#             handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
#         else:
#             handler = self.http_method_not_allowed
#         return handler(request, *args, **kwargs)
#     def get(self,request):
#         try:
#             pkg = request.GET.get("pkg","")
#             return JsonResponse({"result":pkg})
#         except Exception:
#             return JsonResponse({"error":"error"})

#     def post(self,request):
#         try:
#             jsonDict = eval(request.body)
#             pkg = jsonDict['pkg']
#             return JsonResponse({"result":pkg})
#         except Exception:
#             return JsonResponse({"error":"error"})

#     def put(self,request):
#         values = QueryDict(request.body)
#         return JsonResponse({"status":200,"data":"这是PUT请求"})
#     def delete(self,request):
#         values = QueryDict(request.body)
#         return JsonResponse({"status":200,"data":"这是DELETE请求"})

class translatorApi(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
    def get(self,request):
        try:
            sentence = request.GET.get("sentence","")
            fromlang = request.GET.get("fromlang","")
            tolang = request.GET.get("tolang","")
            translator_ec = Translator(from_lang=fromlang, to_lang=tolang)
            translatedSentence = translator_ec.translate(sentence)
            return JsonResponse({"result":translatedSentence})
        except Exception:
            return JsonResponse({"error":"error"})

class codingApi(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    # sql terminal
    def get(self,request):
        try:
            pkg = request.GET.get("pkg","")
            engine = initEngine("fromDB")
            cursor = engine.cursor()
            sql = pkg
            rows = cursor.execute(sql)  
            data = cursor.fetchall()
            rst = "\n".join([str(d) for d in data])
            engine.commit()
            cursor.close()
            engine.close()
            return JsonResponse({"result":rst})
        except Exception:
            return JsonResponse({"error":"error"})

    # python terminal
    def post(self,request):
        # try:
        jsonDict = eval(request.body)
        inputs = jsonDict['input']
        # 写入文件
        f = open(f'{BASE_DIR}/online_codes.py', 'w+')
        f.write(eval(inputs))
        f.close()
        # 重新导入文件中函数
        import ezinfo.online_codes as oc
        reload(oc)
        # 返回运行结果
        temp = oc.Run.run()
        if type(temp) == dict:
            rst = {"x":temp.get("x",[]),"y":temp.get("y",[]),"y2":temp.get("y2",[]),"other":temp}
        else:
            rst = {"other":temp}
        return JsonResponse({"result":rst})
        # except Exception:
        #     return JsonResponse({"error":"error"})