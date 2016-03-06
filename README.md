# image-overlay
A python flask and Pillow based repo for generating overlay images

![Example graph](https://i.imgflip.com/79i.jpg)

The repo is intended to provide a quick example for overlaying an image with text and returning a complete image via a GET request. The repo provides the ability to:

- Program in Python 2.7
- Return a customized image

# Developing

To get started with developing on this repo:

- Clone the repository.
- Create a virtualenv for the repo.
- pip install -r requirements.txt in the virtualenv.
- ```python run.py```
- Open a browser and pass in the apropriate URL with QueryString params:  ```http://127.0.0.1:5000/?i=some%20name&g=1234567```

We want you to succeed and to succeed easily! We're happy to give you this stuff rather than making you "deduce" it somehow. Probably a half hour together setting this up would square you away to start up.

# Contributing

This repository requires 1 Code Review before new code can be added to Master. If you'd like to commit to this repo:

- Create a branch off master.
- Make your changes until your new report or feature works.
- Test (if possible) that all other pre-existing features work. If this seems hard or mysterious, let us know and we can do it.
- Check that your Python reasonably meets pep8 standards: $ pep8 #your_file#
- If your code editor has an Inspect Code feature, inspect it and make any reasonable changes.
- Combine the code with the current master branch. While on your branch, type in: $ git merge master
- Submit a Pull Request, and drop it into the #implementations channel

For smaller pull requests, it will likely take a few days to thoroughly go over it and test it. For larger pull requests, it could take up to a week to fully review the code, test it, and make comments. 

When code is approved for merging, we'll plus one it, and it'll be up to you to merge the code and delete the branch