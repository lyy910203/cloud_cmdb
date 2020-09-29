from django.db import models
from cloud.models import CloudProduct,CloudAccess
from host.models import Host
# Create your models here.

class IpType(models.IntegerChoices):
    PRIVILEGE = 1,"私网"
    PUBLIC = 2,"公网"

class CloudIp(models.Model):
    product = models.IntegerField(choices=CloudProduct.choices, default=CloudProduct.ECS, verbose_name="云商代码")
    ip = models.GenericIPAddressField(verbose_name="ip",db_index=True)
    mac = models.CharField(max_length=50,verbose_name="mac",default="")
    type = models.IntegerField(choices=IpType.choices,default=IpType.PRIVILEGE,verbose_name="IP类型")
    host = models.ForeignKey("host.Host",on_delete=models.SET_NULL,null=True,blank=True)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_datetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    cloud_access = models.ForeignKey("cloud.CloudAccess",on_delete=models.SET_NULL,null=True,blank=True,verbose_name="主机账户")
    def __str__(self):
        return self.ip
    class Meta:
        verbose_name = "公共IP"
        verbose_name_plural = verbose_name
        db_table = "cloud_ip"
