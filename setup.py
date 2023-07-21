from setuptools import setup, find_packages

# Read the dependencies from requirements.txt
with open('requirements.txt', 'r') as file:
    install_requires = file.read().splitlines()

setup(
    name='InvoiceExtractor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'invoice-extractor=invoice_extractor.main:cli',
        ],
    },
)
