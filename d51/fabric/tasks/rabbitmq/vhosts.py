FABRIC_TASK_MODULE = True

from d51.fabric.tasks.rabbitmq import ctl
from fabric.decorators import task

__all__ = ["add", "delete", "list"]

def add(host_name):
    ctl("add_vhost %s" % host_name)

def delete(host_name):
    ctl("delete_vhost %s" % host_name)

def list():
    ctl("list_vhosts")


