from setuptools import find_packages, setup


setup(
    name='shapes',
    version='1.1',
    description='Python shapes',
    author='Eitan Peretz',
    author_email='eitanperetz@gmail.com',
    packages=find_packages(),
    install_requires=['six', 'test'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
