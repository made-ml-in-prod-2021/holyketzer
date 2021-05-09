from setuptools import setup

install_requires = [
    "pandas==1.2.4",
    "PyYAML",
    "scikit-learn==0.24.2",
    "fastapi",
    "uvicorn",
]

extras = {
    'testing': [
        "pytest==6.2.3",
        "requests",
    ],
}

# Meta dependency groups.
all_deps = []
for group_name in extras:
    all_deps += extras[group_name]
extras['all'] = all_deps


setup(
    install_requires=install_requires,
    extras_require=extras,
    tests_require=extras['testing'],
)
