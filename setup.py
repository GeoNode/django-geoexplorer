import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-geoexplorer',
    version='4.0.43',
    author='Alessio Fabiani',
    author_email='alessio.fabiani@gmail.com',
    url='https://github.com/GeoNode/django-geoexplorer',
    download_url="http://pypi.python.org/pypi/django-geoexplorer/",
    description="Use GeoExplorer in your django projects",
    long_description=open(os.path.join(here, 'README.md')).read(),
    license='LGPL, see LICENSE file.',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Topic :: Utilities',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Development Status :: 5 - Production/Stable',
                 'Programming Language :: Python :: 2.7'],
)
