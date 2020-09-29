from django.db import models

# Create your models here.
def defaultJson():
    return {}

class CloudCode(models.IntegerChoices):
    ALIYUN = 1, "阿里云"
    AWS_CN = 2, "AWS国内"
    AWS_EN = 3, "AWS海外"
    HUAWEI = 4, "华为云"
    QCLOUD = 5, "腾讯云"

class CloudStatus(models.IntegerChoices):
    START  = 1, "启动"
    STOP   = 2, "停止"
    DELETE = 3, "删除"

class CloudProduct(models.IntegerChoices):
    ECS = 1, "ECS"
    LB =  2, "LB"



class CloudRegion(models.Model):
    name = models.CharField(max_length=20, verbose_name="地区名")
    region_code = models.CharField(max_length=20, verbose_name="区域代码",db_index=True)
    cloud_code = models.IntegerField(choices=CloudCode.choices, default=CloudCode.ALIYUN, verbose_name="云商代码")
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_datetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    def __str__(self):
        return self.cloud_code - self.region_code
    class Meta:
        verbose_name = "云商区域"
        verbose_name_plural = verbose_name
        unique_together = ["cloud_code","region_code"]
        db_table = "cloud_region"




class CloudFunc(models.Model):
    name = models.CharField(max_length=20, verbose_name="云商执行函数名")
    code = models.IntegerField( choices=CloudCode.choices, default=CloudCode.ALIYUN, verbose_name="云商代码")
    func = models.CharField(max_length=50, verbose_name="云商执行函数路径")
    product = models.IntegerField(choices=CloudProduct.choices, default=CloudProduct.ECS, verbose_name="云商代码")
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_datetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "云商函数"
        verbose_name_plural = verbose_name
        db_table = "cloud_func"


class CloudAccess(models.Model):
    name    = models.CharField(max_length=20,verbose_name="云商名")
    code    = models.IntegerField(choices=CloudCode.choices,default=CloudCode.ALIYUN,verbose_name="云商代码")
    secret  = models.JSONField(default=defaultJson,verbose_name="JSON秘钥")
    status  = models.IntegerField(choices=CloudStatus.choices,default=CloudStatus.START,verbose_name="状态")
    add_datetime = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    modify_datetime = models.DateTimeField(auto_now=True,verbose_name="修改时间")
    remarks = models.TextField(verbose_name="备注",default="")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "云商账号"
        verbose_name_plural = verbose_name
        db_table = "cloud_access"