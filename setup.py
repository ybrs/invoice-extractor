from setuptools import setup, find_packages

# Read the dependencies from requirements.txt
with open('requirements.txt', 'r') as file:
    install_requires = file.read().splitlines()

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='InvoiceExtractor',
    version='0.1.0',
    author='Aybars Badur',
    description='A Python package for extracting data from invoices.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ybrs/invoice-extractor',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'invoice-extractor=invoice_extractor.main:cli',
        ],
    },
)
