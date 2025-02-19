from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rsmb_auth/__init__.py
from rsmb_auth import __version__ as version

setup(
	name="rsmb_auth",
	version=version,
	description="Authentication app for frappe api calling",
	author="Royalsmb",
	author_email="momodou.khan@royalsmb.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
