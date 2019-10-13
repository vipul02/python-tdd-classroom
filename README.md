# python-tdd-classroom
A hand-on session with TDD and unit testing in python.

Note it's preferred to use Git bash terminal when on Windows. You can download it from [here](https://git-scm.com/downloads). 

Also, Python3.7 should be installed and added to PATH.
 
    $ python --version
    Python 3.7.3


### Goal
* Fork the project.
* Clone the repo.
* Create a child(feature) branch from master branch.
* In the child(feature) branch, implement missing functions to make the unit tests pass (run tests locally).
* Push the child(feature) branch from local to the remote.
* Share the link to your repo.

### How to run tests locally
Before running tests locally make sure, you have forked the project to create your own copy of the repo. Then clone the repo into your local machine.

Cd into your local repo
     
    $ cd python-tdd-classroom
    User@DESKTOP-M5KJ2CI MINGW64 /f/Learnings/TDD/python-tdd-classroom (master)
    
As can be seen above, currently the local repo points to the `master` branch. Create a chile branch with name `feature/impelement-functions`

    $ git checkout -b feature/implement-functions
    Switched to a new branch 'feature/implement-functions'
    
Now that you are checked in to child branch, you can start working on code.

     
Make sure you are in the root directory of the project

    $ ls
    src/  tests/
    
Then create a virtual environment for the project.

On Linux

    $ virtualenv -p python venv
    $ . venv/bin/activate

On Windows
Powershell
  
    > virtualenv -p python venv
    > .\venv\Scripts\activate

Git Bash

    $ virtualenv -p python venv
    $ . venv/Scripts/activate

    
Run the tests

    $ python -m unittest
    
You should see the following failing output

    ----------------------------------------------------------------------
    Ran 7 tests in 0.002s

    FAILED (failures=6)
    
Implement all the functions to make the tests pass.

You need to make all tests work and achieve the following output.

    $ python -m unittest
    ----------------------------------------------------------------------
     Ran 7 tests in 0.002s

     OK
     
Commit all the code changes and push the feature branch to the remote.