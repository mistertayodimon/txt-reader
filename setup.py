from setuptools import setup, find_packages

setup(
    name='txt_reader',
    version='0.3.0-beta',
    description='Библиотека для чтения данных из txt-файлов',
    author='mistertayodimon',
    author_email='dimondimonych1@outlook.com',
    packages=find_packages(),  # Ищет все пакеты (включая txt_reader/)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
