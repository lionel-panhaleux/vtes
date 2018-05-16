from setuptools import find_packages
from setuptools import setup


setup(
    name="fame",
    version='1.0.0',
    author="lionelpx",
    author_email="lionel.panhaleux@gmail.com",
    description="A tool for Vampire: The Eternal Struggle",
    license="MIT",
    keywords="VTES CCG Jyhad",
    url="",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fame = fame.cli:main",
        ],
    },
    package_data={'': ['TWDA.diff']},
    include_package_data=True,
    long_description=open("README.md").read(),
    install_requires=[
        "arrow",
        "python-Levenshtein",
        "requests",
    ],
    python_requires='>=3.5',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Players",
        "Natural Language :: English",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        "Topic :: Software Development",
    ],
)
