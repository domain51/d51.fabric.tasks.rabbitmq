import pkg_resources
pkg_resources.declare_namespace(__name__)

FABRIC_TASK_MODULE = True

from fabric.api import sudo
import sys

RABBITMQCTL = 'rabbitmqctl'
RABBITMQ_PACKAGE_NAME = 'rabbitmq-server'
RABBITMQ_VERSION = '1.7.1'
DEBIAN_FILE = "rabbitmq-server_%s-1_all.deb" % RABBITMQ_VERSION
DEBIAN_URL = "http://www.rabbitmq.com/releases/rabbitmq-server/v%s/%s" % (RABBITMQ_VERSION, DEBIAN_FILE)


def install(url=DEBIAN_URL, file=DEBIAN_FILE, build_deps_for=RABBITMQ_PACKAGE_NAME):
    sudo("if [ ! -f %s ]; then wget %s; fi;" % (file, url))
    sudo("apt-get build-dep -y %s" % build_deps_for)
    sudo("dpkg --install %s" % file)

def ctl(cmd, rabbitmqctl=RABBITMQCTL):
    sudo("%s %s" % (rabbitmqctl, cmd))

def stop():
    ctl("stop")

def stop_app():
    ctl("stop_app")

def start_app():
    ctl("start_app")

def reset():
    ctl("reset")

def force_reset():
    ctl("force_reset")

def cluster(*args):
    ctl("cluster %s" % " ".join(args))

def status():
    ctl("status")

def rotate_logs(suffix=None):
    ctl("rotate_logs %s" % suffix)

from d51.fabric.tasks.rabbitmq import users
from d51.fabric.tasks.rabbitmq import vhosts
from d51.fabric.tasks.rabbitmq import permissions
