from setuptools import setup, find_packages

setup(
    name="docassemble-mentalkb",
    version="0.0.1",
    description="MentalkB interview driven by MentalkB CSV dataset",
    long_description="Docassemble package that renders interviews from MentalkB DB extracts.",
    long_description_content_type="text/markdown",
    author="Your Name",
    license="MIT",
    packages=find_packages(),
    install_requires=["docassemble-base","pandas"],
    include_package_data=True,
    zip_safe=False,
)
