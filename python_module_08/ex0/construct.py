import os
import sys
import site


def is_virtual_environment() -> bool:
    # sys.prefix points to the current python installation
    # sys.base_prefix always points to the original system python
    # if they are different, we are inside a virtual environment
    return sys.prefix != sys.base_prefix


def get_virtual_env_name() -> str:
    # when a venv is activated, the shell sets VIRTUAL_ENV to the venv path
    # os.path.basename extracts just the folder name from the full path
    venv_path = os.environ.get("VIRTUAL_ENV", "")
    if venv_path:
        return os.path.basename(venv_path)
    return "None detected"


def get_virtual_env_path() -> str:
    # returns the full path of the active venv
    # returns "None" if no venv is active
    return os.environ.get("VIRTUAL_ENV", "None")


def get_python_executable() -> str:
    # sys.executable is the full path to the python interpreter running this script
    # inside a venv it points to the venv's python, not the global one
    return sys.executable


def get_site_packages_path() -> str:
    # site.getsitepackages() returns a list of directories where packages are installed
    # this differs between global python and a virtual environment
    # which makes the isolation concept visible
    try:
        packages = site.getsitepackages()
        if packages:
            return packages[0]
        return "Unable to determine"
    except AttributeError:
        try:
            return site.getusersitepackages()
        except Exception:
            return "Unable to determine"


def display_outside_venv() -> None:
    # output shown when running outside a virtual environment
    # warns the user and provides instructions to create and activate one
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {get_python_executable()}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate    # On Windows")
    print()
    print("Then run this program again.")


def display_inside_venv() -> None:
    # output shown when running inside a virtual environment
    # confirms isolation and shows where packages will be installed
    venv_name = get_virtual_env_name()
    venv_path = get_virtual_env_path()
    site_pkgs = get_site_packages_path()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {get_python_executable()}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()
    print("Package installation path:")
    print(site_pkgs)


def main() -> None:
    try:
        # detect the environment and route to the correct display function
        if is_virtual_environment():
            display_inside_venv()
        else:
            display_outside_venv()
    except Exception as e:
        print(f"ERROR: Failed to inspect environment: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
