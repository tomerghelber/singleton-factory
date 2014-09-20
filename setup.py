from setuptools import setup, find_packages


# Dynamically calculate the version based on singleton_factory.VERSION.
version = __import__('singleton_factory').get_version()


setup(
    name='singleton_factory',
    packages=find_packages(exclude=['test*']),
    version=version,
    description='A python implements of singleton factory.',
    url='https://github.com/tomerghelber/singleton_factory',
    keywords=["singleton", "factory", "singleton factory", ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
