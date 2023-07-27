import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biodigest",
    version="0.2.10",
    author="Klaudia Adamowicz",
    author_email='klaudia.adamowicz@uni-hamburg.de',
    url='http://pypi.python.org/pypi/biodigest/',
    license='LICENSE',
    description="In silico Validation of Disease and Gene Sets, Clusterings or Subnetworks (DIGEST)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['biodigest', 'biodigest.evaluation', 'biodigest.evaluation.d_utils', 'biodigest.evaluation.mappers'],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Science/Research',
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.7',
    install_requires=[
        "pandas==1.5.2",
        "numpy==1.24.3",
        "scipy==1.8.0",
        "seaborn==0.12.2",
        "biothings_client==0.2.6",
        "gseapy==1.0.4",
        "psutil==5.9.0",
        "requests==2.28.2",
        "pycairo==1.21.0",
    ]
)
