from distutils.core import setup
import os

# Borrowed and modified from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

def build_package(dirpath, dirnames, filenames):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    pkg = dirpath.replace(os.path.sep, '.')
    if os.path.altsep:
        pkg = pkg.replace(os.path.altsep, '.')
    packages.append(pkg)

[build_package(dirpath, dirnames, filenames) for dirpath, dirnames, filenames in os.walk('d51')]

setup(
    name='d51.fabric.tasks.rabbitmq',
    version='0.1', # TODO: move this into Dolt.get_version()
    description='Fabric tasks for handling basic management tasks on RabbitMQ',
    author='Domain51',
    author_email='official@domain51.com',
    url='http://github.com/domain51/d51.fabric.tasks.rabbitmq/',
    packages=packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Common Development and Distribution License (CDDL)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
    ],
)



