from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as f:
    long_desc = f.read()

setup(
    name='lang2json',
    description='Simple python library that converts .lang files to json, and vice versa.',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version='1.0',
    url='https://github.com/s4300/lang2json-python',
    author='s4300',
    author_email='',
    license='MIT',
    keywords='lang json',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires='>=3.6',
)