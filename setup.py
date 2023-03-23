from distutils.core import setup


def main():
    setup(name='a_vine',
          version='1.0',
          description='azotobacter_vinelandii_dj',
          author='?',
          author_email='?',
          packages=['syn_elong'],
          requires=['cobra'],
          keywords=['systems', 'biology', 'model', 'rules'],
          classifiers=[
            'Intended Audience :: Science/Research',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Mathematics',
            ],
          )


if __name__ == '__main__':
    main()