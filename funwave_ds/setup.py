from setuptools import setup, find_packages

setup(
    name='funwaveds',  # Replace with your project's name
    version='0.1.0',  # Replace with your project's version
    description='Python tools for FUNWAVE.',  # Replace with a description
    author='Ryan Schanta',  # Replace with your name
    author_email='rschanta@udel.edu',  # Replace with your email
    url='https://github.com/rschanta/FUNWAVE_DS',  # Replace with your project's URL
    packages=find_packages(),  # Automatically find all packages and subpackages
    install_requires=[
        'absl-py==2.1.0',
        'astunparse==1.6.3',
        'certifi==2024.7.4',
        'charset-normalizer==3.3.2',
        'contourpy==1.2.1',
        'cycler==0.12.1',
        'flatbuffers==24.3.25',
        'fonttools==4.53.1',
        'gast==0.6.0',
        'google-pasta==0.2.0',
        'grpcio==1.65.1',
        'h5py==3.11.0',
        'idna==3.7',
        'keras==3.4.1',
        'kiwisolver==1.4.5',
        'markdown==3.6',
        'markdown-it-py==3.0.0',
        'markupsafe==2.1.5',
        'matplotlib==3.9.1',
        'mdurl==0.1.2',
        'ml-dtypes==0.4.0',
        'namex==0.0.8',
        'numpy==1.26.4',
        'opencv-python==4.10.0.84',
        'opt-einsum==3.3.0',
        'optree==0.12.1',
        'packaging==24.1',
        'pandas==2.2.2',
        'pillow==10.4.0',
        'protobuf==4.25.3',
        'pygments==2.18.0',
        'pyparsing==3.1.2',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.1',
        'requests==2.32.3',
        'rich==13.7.1',
        'scipy==1.14.0',
        'setuptools==69.5.1',
        'six==1.16.0',
        'tensorboard==2.17.0',
        'tensorboard-data-server==0.7.2',
        'tensorflow==2.17.0',
        'tensorflow-io-gcs-filesystem==0.37.1',
        'termcolor==2.4.0',
        'typing-extensions==4.12.2',
        'tzdata==2024.1',
        'urllib3==2.2.2',
        'werkzeug==3.0.3',
        'wheel==0.43.0',
        'wrapt==1.16.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',  # Adjust the license classifier as needed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',  # Adjust the Python version as needed
)