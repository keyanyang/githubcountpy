from setuptools import setup

setup(name='githubcountpy',
      version='0.0.0',
      description='No user, password and access token needed.',
      url='https://github.com/keyanyang/githubcountpy',
      author='Kyle Yang',
      author_email='keyanyoung@gmail.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'beautifulsoup4==4.6.0', 'requests==2.18.4'
      ],
      zip_safe=False)