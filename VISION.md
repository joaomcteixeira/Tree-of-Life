The motivation and vision that drives the Tree-of-Life project.

## Aim

- Provide an independent and straightforward installer of Python-dependencies for user-oriented projects (host projects)
- Manage the configuration of the host project's executable files.
- Provide independent updating routines to keep the user's installation up to date.
- Be platform independent.
- Built to be easily implementable within other projects (host projects), either open or closed source, following [LGPL 3 license](https://github.com/joaomcteixeira/Tree-of-Life/blob/master/LICENSE).

## Identifying the problem

After performing several workshops on [Farseer-NMR](https://github.com/Farseer-NMR/FarSeer-NMR), I found that software installation is a crucial bottle neck between users and developers.

When asking users to install a software package, there is a clear difference between those with programming skills, regardless of their level, and those without any of these skills. For the later group, simple steps such as installing [Anaconda](https://www.anaconda.com/) and configuring a [Python environment](https://conda.io/docs/user-guide/tasks/manage-environments.html) are definitively not straightforward and can hinder users from using the software or even drive them away.

Therefore, when developing a software for a community of users that is not expected (nor required) to have any programming skills to actually use the software, it is necessary to keep, as much as possible, the installation process within the most universal standards, and these have been for decades:

1. download
1. unpack
1. _single-click_ install
1. _single-click_ run

Maintaining these standards can be challenging if one considers the diversity of computer platforms available - each user has a different computer/OS/configuration.

## Solving the problem

### the installer

Tree-of-Life is a simple and universal platform that automatically configures the required Python dependencies and executable files for your Python-based project - thus bridging the gap between developers and users. To setup the software (host project), users should simply type:

```
python tree_of_life.py
```

#### Python to solve Python

Python itself provides a flawless interface between developers and the different OS platforms, therefore, Tree-of-Life is written fully in Python an is compatible with Python 2.7 and 3.x series. I consider safe to rely on Python because nowadays (year 2018) virtually every computer has Python installed and the above command can be executed straightforwardly; installing Python from scratch in the user's computer lies outside this project.

### the updater

Tree-of-Life provides also an independent updater that can be used by users to maintain their project's installation up to date, without requiring Git or performing any other task outside those provided by the project. The UPDATER script is created during the installation.

## User interface

When running the installation script (`tree_of_life.py`) the user will be prompt with two installation routines: _automatic_ and _manual_. 
 
- The **automatic** (recommended) option will install a [Miniconda](https://conda.io/miniconda.html) distribution in the project's folder with all the required Python libraries, this Miniconda installation will not conflict with the user system's Python installation. Also, the executable files will be configured accordingly.
- The **manual** installation will create TEMPLATE executable files. The user should manually configure all the required Python libraries as well as the compatibility between the executable files and the Python dependencies, for example via _shebangs_. Users can use the `template_env.yml` file inside the `install` folder as a guide to the required Python dependencies.

The installation process is recorded in a `install.log` file.
