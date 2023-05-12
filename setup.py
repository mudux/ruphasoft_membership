from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ruphasoft_membership/__init__.py
from ruphasoft_membership import __version__ as version

setup(
	name="ruphasoft_membership",
	version=version,
	description="Frappe App to manage association membership",
	author="mohamud@rupha.co.ke",
	author_email="mohamud@rupha.co.ke",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
