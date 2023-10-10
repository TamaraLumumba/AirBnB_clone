<div align="center">
<h1> 0x00. AIRBNB CLONE - THE CONSOLE</h1>
</div>
<img align="center" src="https://i.imgur.com/MQq3ABc.png" alt="Logo">

## Table of contents

* [Introduction](Introduction)
* [Requirments](Requirments)
* [Console](Console)
* [Storage](Storage)
* [Execution](Execution)
* [Tests](Tests)
* [Authors](Authors)

## Introduction
The AirBnB clone project is a year-long endeavor with the objective of deploying a simplified version of the AirBnB website on a personal server. This project will emphasize the fundamental concepts of higher-level programming and serve as a comprehensive learning experience.

Throughout the first four months of the project, participants will achieve the following milestones:

1. **Command Interpreter**: Develop a command-line interface (similar to a Shell) to manipulate data efficiently, facilitating development and debugging processes.

2. **Website (Front-end)**: Create a functional website with both static and dynamic components, offering users a preview of the final product.

3. **Data Storage**: Implement a database or file-based system to store and manage data, with a focus on data objects relevant to the project.

4. **API Integration**: Establish an API that acts as a communication bridge between the front-end and data storage, enabling essential operations such as data retrieval, creation, deletion, and updates.

This project represents a comprehensive journey into web development and programming, covering essential concepts and skills essential for creating complex web applications.

## Requirments
Python Scripts
Allowed editors: vi, vim, emacs
All files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files should end with a new line
The first line of files should be exactly #!/usr/bin/python3
Your code should use the pycodestyle (version 2.8.*)
All files must be executable
The length of files are tested using wc
All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
All files should use * [pycodestyle](https://pypi.org/project/pycodestyle/) to all files.

## Console
The console serves as the central hub for our project, fulfilling a vital role in the creation and management of data objects. Its primary functions include crafting the data model, overseeing operations such as creation, updating, and deletion of objects through a command interpreter, and persisting these objects into a JSON file.

## Storage
The storage component of our project plays a pivotal role in managing the persistence and retrieval of data objects. It serves as a foundational layer that abstracts the complexities of data storage and retrieval from the rest of the system. 
This storage system allows us to store and persist objects in a JSON file, providing a consistent and reliable means of data management.

## Execution
In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Tests
Python Unit Tests
Allowed editors: vi, vim, emacs
All files should end with a new line
All test files should be inside a folder tests
You have to use the unittest module
All test files should be python files (extension: .py)
All test files and folders should start by test_
File organization in the tests folder should be the same as your project
All tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Authors
<details>
    <summary>Tamara Lumumba</summary>
    <ul>
    <li><a href="https://www.github.com/TamaraLumumba">Github</a></li>
    <li><a href="mailto:aysuarex@gmail.com">e-mail</a></li>
    </ul>
</details>

<details>
    <summary>Brian Mwirigi</summary>
    <ul>
    <li><a href="https://www.github.com/Rigiih7">Github</a></li>
    <li><a href="mailto:mwirigihbrian@gmail.com">e-mail</a></li>
    </ul>
</details>
