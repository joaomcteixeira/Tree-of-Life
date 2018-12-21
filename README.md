# Tree-of-Life

**Tree-of-Life** is a _Python-written_ and _stand-alone_ library that configures Python dependencies for Python-based and user-oriented projects. It also configures the _executable_ files.

## Identifying the problem

After performing several workshops on [Farseer-NMR](https://github.com/Farseer-NMR/FarSeer-NMR), I found that software installation is one of the crucial bottle necks between users and developers. When asking users to install a software package, there is a clear difference between users with programming skills, regardless of the level, and users without any of these skills. For the later group, simple steps like installing [Anaconda](https://www.anaconda.com/) and configuring a [Python environment](https://conda.io/docs/user-guide/tasks/manage-environments.html) are definitively not straightforward and can hinder users from using the software or even drive them away.

Therefore, when developing software for a community of users that is not expected (nor required) to have any programming skills, it is necessary to keep, as much as possible, the installation process within the most universal standards, and these have been for decades:

1. download
1. unzip
1. click single file to install
1. click single file to run

Maintaining these standards can be challenging if one considers the diversity of computer platforms available - each user has a different computer/OS/configuration.

## Aim

Tree-of-Life is a simple and universal platform that automatically configures the required Python dependencies and executable files for your Python-based project. To setup the software, users should simply type:

```
python tree_of_life.py
```

Python itself provides a flawless interface between developers and the different OS platforms, therefore, Tree-of-Life is written fully in Python an is compatible with Python 2.7 and 3.x series. I consider safe to rely on Python because nowadays (year 2018) virtually every computer has Python installed and the above command can be executed straightforwardly; installing Python from scratch in the user's computer lies outside this project.

Additionally, for the developer to have full control on what takes place during the installation process, the installation protocol (in this case, Tree-of-Life) should be completely independent of the previously installed Python settings, that is, not relying on [PyPI](https://pypi.org/) nor `conda install`.
