from setuptools import setup, find_packages

setup (
    name="Inputron",
    version="1.2.2",
    description="Control your Outputs as if they were your",
    author="dotxavierket",
    author_email="xavier.gabriel3728@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/G4brielXavier/Inputron.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',    
)