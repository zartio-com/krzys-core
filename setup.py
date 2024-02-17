from setuptools import setup, find_namespace_packages

setup(
    name='krzys-core',
    version='1.0.0',
    author='iTokajo',
    packages=find_namespace_packages(where='src/', include=['krzys.core']),
    package_dir={
        '': 'src'
    },
    install_requires=['discord', 'python-dotenv'],
    entry_points={
        'console_scripts': [
            'krzys = krzys.core:run'
        ]
    }
)
