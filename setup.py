from distutils.core import setup

from monthday import __version__ as version


setup(
    name='monthday',
    version=version,
    description='Date without year',
    license='LGPLv3+',
    author='Hong Minhee',
    author_email='hongminhee' '@' 'member.fsf.org',
    py_modules=['monthday'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved'
        ' :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
