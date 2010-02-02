from d51.fabric.tasks import rabbitmq
from fabric.api import local

def install():
    local("python setup.py install")

