from setuptools import setup,find_packages
setup (
    author="Linto",
    author_email="lintopjohn000@gmail.com",
    packages=find_packages(),
    dependency_links=['https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl'],
    install_requires=['tensorflow','numpy','scipy','opencv-python','pillow','matplotlib','H5py','keras','imageai @ https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl']

)