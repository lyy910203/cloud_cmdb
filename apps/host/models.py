from django.db import models
from cloud.models import CloudRegion
# Create your models here.

class Host(models.Model):
    instance_id = models.CharField(max_length=30,db_index=True,unique=True,verbose_name="InstanceId")
    os = models.CharField(max_length=100,verbose_name="OS",default="")
    memory  = models.IntegerField(verbose_name="内存,M",default=0)
    cpu = models.IntegerField(verbose_name="CPU",default=0)
    start_detetime = models.DateTimeField(verbose_name="启动时间")
    expire_detetime = models.DateTimeField(verbose_name="过期时间")
    image = models.CharField(max_length=100,verbose_name="镜像IMAGE",default="")
    name = models.CharField(max_length=20,verbose_name="自己定义的名字",default="")
    instance_type = models.CharField(max_length=30,verbose_name="实例类型",default="")
    zone = models.CharField(max_length=30,verbose_name="区域",default="")
    region = models.ForeignKey("cloud.CloudRegion",on_delete=models.CASCADE,verbose_name="区域")
    cloud_access = models.ForeignKey("cloud.CloudAccess", on_delete=models.SET_NULL, null=True, blank=True,verbose_name="主机账户")
    meta = models.JSONField(default=dict,verbose_name="元数据")
    is_upload = models.BooleanField(default=True,verbose_name="是否更新")

    def __str__(self):
        return self.instance_id
    class Meta:
        verbose_name = "主机信息"
        verbose_name_plural = verbose_name
        db_table = "cloud_host"


