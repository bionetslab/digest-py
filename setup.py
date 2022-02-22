import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="digest",
    version="0.0.1",
    author="Klaudia Adamowicz",
    author_email='klaudia.adamowicz@uni-hamburg.de',
    description="Disease and Gene Set and Clustering Validation Tool (DIGEST)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['digest', 'digest.evaluation', 'digest.evaluation.d_utils', 'digest.evaluation.mappers'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.8',
    py_modules=["bio-digest"],
    package_dir={'': 'digest'},
    install_requires=[]
)
