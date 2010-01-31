FABRIC_TASK_MODULE = True

from d51.fabric.tasks.rabbitmq import ctl

__all__ = ["add", "delete", "change_password", "list"]

def add(user, password):
    ctl("add_user %s %s" % (user, password))

def delete(user):
    ctl("delete_user %s" % user)

def change_password(user, new_password):
    ctl("change_password %s %s" % (user, new_password))

def list():
    ctl("list_users")


