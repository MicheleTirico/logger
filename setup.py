# from setuptools import setup, find_packages
#
# pkgs = find_packages('src')
#
# setup_kwds = dict(
#     name='logger',
#     version="1.0.1",
#     author="Michele Tirico",
#     author_mail="tirico.michele@outlook.com",
#     python_required="3.10",
#     zip_safe=False,
#     packages=pkgs,
#     package_dir={'': 'src'},
#     entry_points={},
#     )
#
# setup(**setup_kwds)
#

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='logger',
    version='0.0.1',
    author='Michele Tirico',
   # author_mail="tirico.michele@outlook.com",
    description='glogger',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MicheleTirico/logger',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    # },
    license='MIT',
    packages=['src/logger'],
    install_requires=['requests'],
)