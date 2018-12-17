"""
Defines executables

Copyright © 2018-2019 Tree-of-Life

Contributors to this file:
- João M.C. Teixeira (https://github.com/joaomcteixeira)

Tree-of-Life is free software: you can redistribute it and/or modify
it under the terms of the LGPL - GNU Lesser General Public License
as published by the Free Software Foundation, either version 3
of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
LGPL - GNU Lesser General Public License for more details.

You should have received a copy of the this license along
with this library. If not, see <http://www.gnu.org/licenses/>.
"""

from install import system

# interesting readings:
# https://stackoverflow.com/questions/6943208/activate-a-virtualenv-with-a-python-script
# https://halotis.com/running-python-code-in-windows-batch-file-trick/
# https://docs.python.org/3.3/using/windows.html
# finally, shebangs can be used on Windows10
# allow double click execution

# define your executable scripts
exec1_code = r"""#! {}
# write your code here

import os

print(os.getcwd())

"""

exec2_code = r"""#! {}
# write the code of you 2nd exec file

sentense = "Hello World, I am Tree-of-Life!"

for word in sentense.split():
    print(word)

"""

update_script_code = r"""#! {}

import sys
import os
import importlib
from pathlib import Path

software_folder = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        os.pardir
        )
    )

sys.path.append(software_folder)

if sys.version_info[0] != 3:
    sys.stderr.write("Python 3 is required to run Updater")
    sys.exit(1)

from install import logger
from install import messages

try:
    import installation_vars
except ModuleNotFoundError as e:
    print("* ERROR * installation_vars.py file not found")
    print("* ERROR * this file has created during installation")
    print("* ERROR * and is required for UPDATING")
    print("* ERROR * Reinstall the SOFTWARE to repair updating functions")
    print(messages.additional_help)
    print(messages.abort)
    sys.exit(1)

update_log = installation_vars.install_dir.joinpath('update.log')

if update_log.exists():
    update_log.unlink()

log = logger.InstallLogger(__name__, log_file_name=update_log).gen_logger()

log.debug("start updating")

from install import updater
from install import commons
from install import condamanager

upf = updater.Updater(installation_vars.install_dir)
upf.run()

# reloads the updated version of system lib
from install import system
importlib.reload(system)

log.info("* Checking Conda environment...")

env_exec_new = installation_vars.python_exec
install_option_new = installation_vars.install_option

if system.latest_env_version > installation_vars.installed_env_version:

    log.info("* A NEW Python environment version is available")
    log.info("* Software's dependencies must be updated")
    
    if installation_vars.conda_exec and installation_vars.install_option == 1:
    
        log.info("* Miniconda installation found")
        log.info("   ... starting env update")
        
        upc = condamanager.CondaManager(cwd=installation_vars.install_dir)
        upc.set_conda_exec(installation_vars.conda_exec)
        upc.set_env_name(installation_vars.installed_env_name)
        upc.remove_env()
        upc.set_env_file(installation_vars.installed_env_file)
        upc.install_env()
        upc.logs_env_information()
        log.info("... Conda env UPDATED")
        
        env_exec_new = upc.get_env_python_exec()
        install_option_new = 1
    
    elif not(installation_vars.conda_exec) \
            and installation_vars.install_option == 2:
        log.info("* You have previously configured Python libraries mannually")
        log.info("* You should update software's Python dependencies")
        log.info("* consult .yml file in 'install' folder")
    
    else:
        log.info("* ERROR* We couldn't access install information")
        log.info(messages.something_wrong)
        log.info(messages.additional_help)
        log.info(messages.abort)
        sys.exit(1)
    
else:
    log.info("   ...Conda env already in latest version")
    log.info("")

log.info("* Updating executable files...")

commons.create_executables(
    installation_vars.install_dir,
    env_exec_new
    )

commons.register_install_vars(
    installation_vars.install_dir,
    env_exec=env_exec_new,
    install_option=install_option_new,
    conda_exec=installation_vars.conda_exec,
    env_name=system.latest_env_name,
    env_version=system.latest_env_version,
    miniconda_folder=system.miniconda_folder
    )

log.info(messages.update_completed)
commons.sys_exit()
"""

# executable scripts file names and extensions
exec1 = "exec_1{}".format(system.exec_file_extension)
exec2 = "exec_2{}".format(system.exec_file_extension)
updatescript = "update{}".format(system.exec_file_extension)

# dictionary listing the executable scripts
# keys are file names, values the string with code
executable_files = {
    exec1: exec1_code,
    exec2: exec2_code,
    updatescript: update_script_code
    }
