import json
from utils.base.ecs import EcsBase
from utils.aliyun.public.client_pub import get_aliyun_client
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest


class Ecs(EcsBase):

    def remote_describeInstances(self,client,instanceIds = []):
        """
        阿里云获取主机列表函数
        :param client:  aliclient obj
        :param instanceIds: default = []
        :return: json
        """

        retInstanceIds = []
        for page in range(1,999):  # 超过9990机器神人耶
            request = DescribeInstancesRequest()
            request.set_accept_format('json')
            request.set_PageNumber(page)
            request.set_PageSize(10)
            if instanceIds:
                request.set_InstanceIds(str(instanceIds))
            response = client.do_action_with_exception(request)
            # python2:  print(response)
            resp = json.loads(response)
            if not resp["Instances"]["Instance"]:
                break
            retInstanceIds.extend(resp["Instances"]["Instance"])
        return retInstanceIds

    def sync(self):
        ...


if __name__ == '__main__':
    ecs = Ecs()
    client = get_aliyun_client("XXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXX","cn-zhangjiakou")
    ret = ecs.remote_describeInstances(client)
    print(ret)