import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyfastq_reader',
    version='1.0.1',
    author='Andy Hauser',
    author_email='Andreas.Hauser@LMU.de',
    license='LICENSE',
    description='FASTQ file reader',
    long_description='Pure python reader for the FASTQ format used in sequencing',
    url='https://github.com/ahcm/pyfastq_reader',
    packages=setuptools.find_packages(),
    scripts=['pyfastq_reader.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
