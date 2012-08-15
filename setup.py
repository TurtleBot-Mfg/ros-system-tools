from distutils.core import setup
import os
import subprocess

"""
if os.path.exists("debian/changelog"):
    output=subprocess.check_output("parsechangelog | grep Version", shell=True)
    version = output.split(":")[1].strip()
"""

setup(name = "ros-system-tools",
#    version = version,
    version = "0.0.1",
    description = "System level ROS Tools",
    author = "I Heart Engineering",
    author_email = "code@iheartengineering.com",
    url = "http://www.iheartengineering.com",
    license = "BSD-3-clause",
    scripts = ["ros-network-id","rosmetalaunch"],
    data_files=[('/etc/init', ["ros-launch.conf"]),
               ],
    long_description = """These tools provide system support for ROS.""" 
    #classifiers = []     
) 
