import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
# 快速导包快捷键  alt+enter
from django.views import View
import json
from consumption.models import LifeInfo


# def index(request):
#     return HttpResponse('index')

class LifeView(View):
    def get(self,request):
        all_life = LifeInfo.objects.all()  # 获取所有数据
        return render(request, 'index.html', context={'lifelist':all_life})

    def post(self, request):
        data = request.POST   # 接收数据
        try:
            # 创建对象
            life = LifeInfo(
                date = data.get('date'),
                consumption_matters = data.get('consumption_matters'),
                amount = data.get('amount'),
                total = data.get('total'),
            )
            life.save()
            return JsonResponse({'data':"添加成功"})
        except Exception as e:
            return JsonResponse({'data': "添加失败"})


    def put(self, request):
        data = json.loads(request.body.decode()) # 接收数据
        life_id = data.get('id')   # 根据id获取对象
        try:
            life = LifeInfo.objects.get(id=life_id)
            # 修改更新数据
            life.date = datetime.datetime.strptime(data.get('date'), '%Y年%m月%d日')
            life.consumption_matters = data.get('consumption_matters')
            life.amount = data.get('amount')
            life.total = data.get('total')

            life.save()
            return JsonResponse({'data':'修改成功'})
        except Exception as e:
            return JsonResponse({'data': '修改失败'})

    def delete(self, request):
        life_id = json.loads(request.body.decode()).get('id') # 拿到消费id
        try:
            life = LifeInfo.objects.get(id=life_id)   # 获取该ID的对象
            life.delete()
            return JsonResponse({'data':'删除成功'})
        except Exception as e:
            return JsonResponse({'data': '删除失败'})
        finally:
            pass






