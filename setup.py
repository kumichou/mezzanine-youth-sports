from setuptools import setup, find_packages
from mezzanine_youth_sports import __version__
import subprocess

def get_long_desc():
    """Use Pandoc to convert the readme to ReST for the PyPI."""
    try:
        return subprocess.check_output(['pandoc', '-f', 'markdown', '-t', 'rst', 'README.md'])
    except:
        print("WARNING: The long readme wasn't converted properly")


setup(
    name='mezzanine-youth-sports',
    version=__version__,
    url='https://github.com/kumichou/mezzanine-youth-sports',
    author='Eric Hankinson',
    author_email='eric.hankinson@gmail.com',
    license='MIT',
    description='Youth Sports management application for the Mezzanine CMS',
    long_description=get_long_desc(),
    keywords='django, mezzanine, youth, sports',
    packages=find_packages(),
    setup_requires=('setuptools'),
    install_requires=('setuptools', 'mezzanine'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',],
    zip_safe=False,
    include_package_data=True,
)
