import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-using-NLP"
AUTHOR_NAME = "Naman0998"
SRC_REPO = "textSummarizer"

setuptools.setup(
    name = REPO_NAME,
    version = __version__,
    author = AUTHOR_NAME,
    description = "Efficient NLP-based text summarizer condenses content for easy comprehension.",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where = "src")

)