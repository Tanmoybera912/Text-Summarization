import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

_version = "0.0.1"

REPO_NAME = "Text-Summarization"
AUTHOR_USER_NAME = "Tanmoybera912"
AUTHOR_EMAIL = "tanmoybera.1998@gmail.com"
SRC_REPO = "textsummarizer"

setuptools.setup(
    name=REPO_NAME,
    version=_version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)   