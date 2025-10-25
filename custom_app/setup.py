# Contenido de custom_app/setup.py

from setuptools import setup, find_packages

setup(
    name='custom_app',
    version='0.0.1',
    description='My Custom App for ERPNext/Frappe',
    author='Deepzide',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    zip_safe=False
)
