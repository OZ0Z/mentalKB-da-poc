from setuptools import setup, find_packages

setup(
    name="docassemble-mentalkb",
    version="1.0.0",
    description="MentalkB Docassemble interview backed by Postgres",
    long_description="Dynamic interview that reads questions, pages, and options from the MentalkB database.",
    long_description_content_type="text/markdown",
    author="Your Name",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "docassemble-base",
        "SQLAlchemy>=2.0",
        "psycopg2-binary>=2.9",
    ],
    include_package_data=True,
    zip_safe=False,
)
