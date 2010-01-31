FABRIC_TASK_MODULE = True

from d51.fabric.tasks.rabbitmq import ctl

__all__ = ["set", "clear", "list", "list_user",]

def set(vhost=None, user=None, configure=None, read=None, write=None):
    vhost = vhost and "-p %s" % vhost or ""
    ctl("set_permissions %s %s %s %s %s" % (vhost, user, configure, read, write))

def clear(vhost=None, user=None):
    vhost = vhost and "-p %s" % vhost or ""
    ctl("clear_permissions %s %s" % (vhost, user))

def list(vhost=None):
    vhost = vhost and "-p %s" % vhost or ""
    ctl("list_permissions %s" % vhost)

def list_user(user):
    ctl("list_user_permissions %s" % user)



