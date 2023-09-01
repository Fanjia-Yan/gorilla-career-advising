import setuptools

setuptools.setup(
    name="gorilla-career-advising-api",
    version= "0.1",
    description="API for getting job postings",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    setup_requires=["lxml"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)