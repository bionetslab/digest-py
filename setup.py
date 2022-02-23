import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biodigest",
    version="0.0.1",
    author="Klaudia Adamowicz",
    author_email='klaudia.adamowicz@uni-hamburg.de',
    url='http://pypi.python.org/pypi/biodigest/',
    license='LICENSE',
    description="Disease and Gene Set and Clustering Validation Tool (DIGEST)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['biodigest', 'biodigest.evaluation', 'biodigest.evaluation.d_utils', 'biodigest.evaluation.mappers'],
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.8',
    install_requires=[
        "pandas==1.4.1",
        "numpy==1.21.1",
        "scipy==1.7.1",
        "seaborn==0.11.2",
        "biothings_client==0.2.6",
        "gseapy==0.10.5",
        "psutil==5.9.0"
    ]
)
