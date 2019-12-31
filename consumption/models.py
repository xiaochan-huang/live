import datetime
from django.db import models


class LifeManage(models.Manager):
    def all(self):
        result = super()
        return result.filter(is_delete=False)

    def create_life(self, consumption_matters):
        model = self.model
        life = model(date=datetime.datetime.now(), consumption_matters=consumption_matters)
        life.save()
        return life


class LifeInfo(models.Model):
    date = models.DateField(verbose_name='日期')
    consumption_matters = models.CharField(verbose_name='消费事项', max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='消费金额')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='总计消费')

    # objects = LifeManage()

    class Meta:
        db_table = 'tb_life'
        verbose_name = '历史消费记录'
        verbose_name_plural = verbose_name