from setuptools import setup
import versioneer
import os

def main():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md'), 'r') as f:
        long_description = f.read()

    setup(
        name='rpi_videoplayer',
        version=versioneer.get_version(),
        description='Raspberry Pi GPIO-controlled video player',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Devin Despain',
        author_email='devin@dspa.in',
        packages=['rpi_videoplayer'],
        install_requires=['transitions'],
        # install_requires=['RPi.GPIO', 'transitions'],
        cmdclass=versioneer.get_cmdclass(),
        zip_safe=True,
        entry_points = {
            'console_scripts': ['videoplayer=rpi_videoplayer.videoplayer:main']
        }
    )


if __name__ == '__main__':
    main()