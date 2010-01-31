FABRIC_TASK_MODULE = True

from d51.fabric.tasks.rabbitmq import ctl
from fabric.decorators import task

__all__ = ["add", "delete", "list"]

def add(user, password):
    ctl("add_host %s %s" % (user, password))

def delete(user):
    ctl("delete_host %s" % user)

def list():
    ctl("list_hosts")


