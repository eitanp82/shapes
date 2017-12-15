from setuptools import find_packages, setup
# from distutils.core import setup
from distutils.command.clean import clean
from distutils.command.install import install as BaseInstall


class Install(BaseInstall):
    def run(self):
        # run install command.
        BaseInstall.run(self)
        # run post-install command.
        self.post_install()

    def post_install(self):
        self.clean_build()

    def clean_build(self):
        c = clean(self.distribution)
        c.all = True
        c.finalize_options()
        c.run()


setup(
    name='shapes',
    version='1.1',
    description='Python shapes',
    author='Eitan Peretz',
    author_email='eitanperetz@gmail.com',
    packages=find_packages(),
    install_requires=['six', 'test'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    cmdclass={'install': Install}
)
