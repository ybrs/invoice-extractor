from setuptools import setup, find_packages

install_requires = """
pdfplumber==0.10.1
langchain==0.0.238
openai==0.27.8
pdfplumber==0.10.1
pdfminer==20191125
click==8.1.6
openpyxl==3.1.2
""".strip().splitlines()

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='InvoiceExtractor',
    version='0.1.2',
    author='Aybars Badur',
    include_package_data=True,
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
