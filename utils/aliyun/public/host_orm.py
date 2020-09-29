import datetime
from host.models import Host
from cloud_cmdb.settings import logger


class HostOrm():


    @classmethod
    def update_or_create(cls,cloud_access_obj,region_obj,instance_id,*args,**kwargs):
        """
        创建或者更新主机
        :param cloud_access_obj: CloudAccess obj
        :param region_obj:  CloudRegion obj
        :param instance_id: 主机ID
        :param args:
        :param kwargs:  其他额外参数
        :return:
        """
        os = kwargs.get("os","")
        memory = kwargs.get("memory", 0)
        cpu = kwargs.get("cpu", 0)
        start_detetime = kwargs.get("start_detetime", datetime.datetime.now())
        expire_detetime = kwargs.get("expire_detetime", datetime.datetime.now())
        image = kwargs.get("image", "")
        name = kwargs.get("name", "")
        instance_type = kwargs.get("instance_type", "")
        zone = kwargs.get("zone", "")
        meta = kwargs.get("zone", {})
        try:
            host_obj,flag = Host.objects.update_or_create(
                instance_id=instance_id,
                os = os,
                memory = memory,
                cpu = cpu,
                start_detetime = start_detetime,
                expire_detetime = expire_detetime,
                image = image,
                name = name,
                instance_type = instance_type,
                zone = zone,
                region = region_obj,
                cloud_access = cloud_access_obj,
                meta = meta
            )
            return host_obj
        except Exception as e:
            logger.error(e)
            return None





