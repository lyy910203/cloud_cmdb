#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException



def get_aliyun_client(accessKeyId,accessSecret,region):
    client = AcsClient(accessKeyId, accessSecret, region)
    return client

