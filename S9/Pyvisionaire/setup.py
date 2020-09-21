from setuptools import setup

with open('README.md', 'r', encoding='utf8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    required = fh.read().splitlines()


setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Visionaire',
    url='https://github.com/jladan/package_demo',
    author='Vignesh Babu P J',
    author_email='vigneshbabupj@gmail.com',

    # Needed to actually package something
    packages=setuptools.find_packages()
    
    python_requires='>=3.6'
    # Needed for dependencies
    install_requires=required,
    include_package_data=True,
    
    # *strongly* suggested for sharing
    version='0.0.1',
    # The license can be anything you like
    license='MIT',
    description='Extensive vision AI package',
   
    long_description=long_description,
    long_description_content_type="text/markdown",
)