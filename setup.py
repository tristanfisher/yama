import os
from pip.req import parse_requirements

from config_loader import VERSION

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

main_script = "yama.py"

install_requirements = parse_requirements("./requirements.txt", session=False)
install_requirements = [str(ir.req) for ir in install_requirements]

setup(
    name="yama",
    version=VERSION,
    author="Tristan Fisher",
    author_email="code@tristanfisher.com",
    description="Yet Another Management Agent",
    long_description=open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "README.md"), "r").read(),
    scripts=[main_script],
    url= "http://github.com/tristanfisher/yama",
    license=open("LICENSE").read(),
    install_requires=install_requirements,
    setup_requires=[]
)
