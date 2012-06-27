'''
Setup file for easy installation
'''
from os.path import join, dirname
from setuptools import setup

LONG_DESCRIPTION = '''
ilendyou-itemlists is an app for storing collections of items
belonging to users. This includes creating lists of lent, borrowed
items, a wishlist and a give-away list.
'''


def long_description():
    '''
    Return long description from README.rst if it's present
    because it doesn't get installed.
    '''
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(name='ilendyou-itemlists',
      version='0.0.1',
      author='Karol Majta',
      author_email='karolmajta@gmail.com',
      description='Lists of items for Ilendyou project.',
      license='BSD',
      keywords='django, user, account, merge',
      url='https://github.com/ilendyou/ilendyou-itemlists',
      package_dir={'': 'src'},
      packages=['ilendyou_itemlists',
                'ilendyou_itemlists.tests'],
      long_description=long_description(),
      install_requires=['django>=1.2.5'],
      classifiers=['Framework :: Django',
                   'Development Status :: 4 - Beta',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.7'])
