from __future__ import unicode_literals
from django.contrib import admin
from consumption.models import LifeInfo

class LifeManage(admin.ModelAdmin):
    # list_display = ['date', 'consumption_matters', 'amount', 'total']
    list_display = ['id', 'date']
    list_per_page = 20
    list_filter = ['is_delete']

    actions_on_top = True
    actions_on_bottom = True

    search_fields = ['date', 'consumption_matters', 'amount']


admin.site.register(LifeInfo)
admin.site.site_title = '日常生活消费'
admin.site.site_header = '资金流向监控'
admin.site.index_title = '欢迎进入'
