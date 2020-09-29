import abc


class EcsBase(object):

    @abc.abstractmethod
    def describeInstances(self):
        ...

    @abc.abstractmethod
    def sync(self):
        """
        sync入口函数，执行start
        :return:
        """
        ...