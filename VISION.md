The motivation and vision that drives the Tree-of-Life project.

Vocabulary:
- the *host project* is that project that uses/implements/adapts/hosts Tree-of-Life for its benefit.
- *non-developer* users, are those users that lack programming/scripting skills.

## Aim

- Provide an independent and straightforward installer of Python-dependencies for projects oriented to **non-developer** users.
- Manage the configuration of the host project's executable files.
- Provide independent updating routines to keep the user's installation up to date.
- Be platform independent.
- Built to be easily implementable, within host projects, either open or closed source, following the [LGPL 3 license](https://github.com/joaomcteixeira/Tree-of-Life/blob/master/LICENSE).
- Tree-of-Life is developed aiming mostly at Scientific Software but it can be extended by all means to software packages any area of interest.

## Identifying the problem

After performing several workshops on [Farseer-NMR](https://github.com/Farseer-NMR/FarSeer-NMR), I found that software installation is a crucial bottle neck between users and developers.

When asking users to install a software package, there is a clear difference between those with programming skills, regardless of their level, and those without any of these skills. For the later group, simple steps such as installing [Anaconda](https://www.anaconda.com/) and configuring a [Python environment](https://conda.io/docs/user-guide/tasks/manage-environments.html) are definitively not straightforward and can create a great barrier between the user and the software or even drive the users completely away.

Therefore, when developing a software for a community of users that is not expected (nor required) to have any programming skills to actually use the software, it is necessary to keep, as much as possible, the installation process within the most universal standards, and these have been for decades:

1. download
1. unpack
1. _single-click_ install
1. _single-click_ run

Maintaining these standards can be challenging if one considers the diversity of computer platforms available - each user has a different computer/OS/configuration.

## Solving the problem

### the installer

**Tree-of-Life** is a simple and universal platform that automatically configures the required Python dependencies and executable files for your Python-based project - thus bridging the gap between developers and users. Therefore, to install a project that hosts Tree-of-Life, the users must simply type:

```
python tree_of_life.py
```

#### Python to solve Python

Python itself provides an excellent interface between developers and the different OS platforms, therefore, Tree-of-Life is written fully in Python an is compatible with Python 2.7 and 3.x series. I consider safe to rely on Python because nowadays (year 2018) virtually every computer has Python installed and the above command can be executed straightforwardly; installing Python from scratch in the user's computer lies outside this project.

### the updater

Tree-of-Life provides also an independent updater that can be used by users to maintain their project's installation up to date, without requiring Git or performing any other task outside those provided by the project. The UPDATER script is created during the installation.

## User interface

When running the installation script (`tree_of_life.py`) the user will be prompt with two installation routines: **automatic** and **manual**. 
 
- The _automatic_ (recommended) option will install a [Miniconda](https://conda.io/miniconda.html) distribution in the project's folder with all the required Python libraries, this Miniconda installation will **not** conflict with the user system's Python installation. Also, the executable files will be configured accordingly.
- The _manual_ installation will create TEMPLATE executable files. The user should manually configure all the required Python libraries as well as the compatibility between the executable files and the Python dependencies, for example via _shebangs_. Users can use the [template_env.yml](https://github.com/joaomcteixeira/Tree-of-Life/blob/master/install/template_env.yml) file inside the [install](https://github.com/joaomcteixeira/Tree-of-Life/tree/master/install) folder as a guide to the required Python dependencies.

The installation process is recorded in a `install.log` file.
