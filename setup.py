from setuptools import setup, find_packages

setup(
    name="evalgotrade",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "quarto",
        "plotly",
        "tqdm",
        "ta-lib",
        "numpy",
        "pandas",
        "shinybroker",
        "scikit-learn",
        "statsmodels",
    ]
)