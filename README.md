# Tree-of-Life

**Tree-of-Life** is a _Python-written_ and _stand-alone_ library that configures the Python dependencies and the _executable files_ for Python-based and user-oriented projects.

## Identifying the problem

After performing several workshops on [Farseer-NMR](https://github.com/Farseer-NMR/FarSeer-NMR), I found that software installation is one of the crucial bottle necks between users and developers. When asking users to install a software package, there is a clear difference between users with programming skills, regardless of the level, and users without any of these skills. For the later group, simple steps like installing [Anaconda](https://www.anaconda.com/) and configuring a [Python environment](https://conda.io/docs/user-guide/tasks/manage-environments.html) are definitively not straightforward and can hinder users from using the software or even drive them away.

Therefore, when developing software for a community of users that is not expected (nor required) to have any programming skills, it is necessary to keep, as much as possible, the installation process within the most universal standards, and these have been for decades:

1. download
1. unzip
1. click single file to install
1. click single file to run

Maintaining these standards can be challenging if one considers the diversity of computer platforms available - each user has a different computer/OS/configuration.

## Aim

### the installer

Tree-of-Life is a simple and universal platform that automatically configures the required Python dependencies and executable files for your Python-based project. To setup the software, users should simply type:

```
python tree_of_life.py
```

Python itself provides a flawless interface between developers and the different OS platforms, therefore, Tree-of-Life is written fully in Python an is compatible with Python 2.7 and 3.x series. I consider safe to rely on Python because nowadays (year 2018) virtually every computer has Python installed and the above command can be executed straightforwardly; installing Python from scratch in the user's computer lies outside this project.

Additionally, for the developer to have full control on what takes place during the installation process, the installation protocol (in this case, Tree-of-Life) should be completely independent of the previously installed Python settings, that is, not relying on [PyPI](https://pypi.org/) nor `conda install`.

### the updated

Tree-of-Life provides also a quick updater that can be used by users to maintain their project's installation up to date; for example, with the `master` branch. The UPDATER script is created during the installation.

## User interface

When running the installation script (`tree_of_life.py`) the user will be prompt with two installation routines: _automatic_ and _manual_. 
 
- The **automatic** (recommended) option will install a [Miniconda](https://conda.io/miniconda.html) distribution in the project's folder with all the required Python libraries, this Miniconda installation will not conflict with the user system's Python installation. Also, the executable files will be configured accordingly.
- The **manual** installation will create TEMPLATE executable files. The user should manually configure all the required Python libraries as well as the compatibility between the executable files and the Python dependencies, for example via _shebangs_. Users can use the `template_env.yml` file inside the `install` folder as a guide to the required Python dependencies.

The installation process is recorded in a `install.log` file.

## How to implement Tree-of-Life in your projects

If you are a software developer, writing your projects in Python, and you wish to know how to implement Tree-of-Life in your project, find all information in the [Wiki page](https://github.com/joaomcteixeira/Tree-of-Life/wiki).

# LICENSE

Tree-of-Life is licensed under [LGPL version 3](https://github.com/joaomcteixeira/Tree-of-Life/blob/master/LICENSE), and you are allowed to modify and use it according to this license terms.

![LGPL](https://www.gnu.org/graphics/lgplv3-with-text-154x68.png)
