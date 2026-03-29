import sys
import importlib
import importlib.util


required_packages = ["pandas", "numpy", "matplotlib", "requests"]


def get_package_version(package_name: str) -> str:
    module = importlib.import_module(package_name)
    return getattr(module, "__version__", "unknown")


def is_package_installed(package_name: str) -> bool:
    return importlib.util.find_spec(package_name) is not None


def check_dependencies() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_installed = True

    for package in required_packages:
        try:
            if not is_package_installed(package):
                print(f"  [MISSING] {package} - not installed")
                all_installed = False
            else:
                version = get_package_version(package)
                print(f"  [OK] {package} ({version})")
        except Exception as error:
            print(f"  [ERROR] {package} - {error}")
            all_installed = False

    return all_installed


def show_install_instructions() -> None:
    print("\nMissing dependencies. Install them:\n")
    print("  pip:    pip install -r requirements.txt")
    print("  Poetry: poetry install")


def show_pip_vs_poetry() -> None:
    print("\nDependency Management Comparison:")
    print("  pip + requirements.txt  -> no sub-dependency locking")
    print("  Poetry + pyproject.toml -> locks ALL versions in poetry.lock")
    print("  Poetry guarantees identical installs across all machines.\n")


def generate_matrix_data() -> tuple:
    import numpy as np
    import pandas as pd

    np.random.seed(42)
    num_points = 1000
    print(f"Processing {num_points} data points...")

    raw_values = np.random.randint(0, 100, size=num_points)
    matrix_df = pd.DataFrame({"values": raw_values})

    return matrix_df, num_points


def save_visualization(matrix_df: object) -> str:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    output_path = "matrix_analysis.png"

    print("Generating visualization...")
    matrix_df.plot()
    plt.savefig(output_path)
    plt.close()

    return output_path


def run_analysis() -> None:
    try:
        print("\nAnalyzing Matrix data...")

        matrix_df, _ = generate_matrix_data()
        output_path = save_visualization(matrix_df)

        print("\nAnalysis complete!")
        print(f"Results saved to: {output_path}")

    except ImportError as error:
        print(f"Import failed: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"Analysis failed: {error}")
        sys.exit(1)


def main() -> None:
    all_installed = check_dependencies()

    if all_installed:
        show_pip_vs_poetry()
        run_analysis()
    else:
        show_install_instructions()
        show_pip_vs_poetry()
        sys.exit(1)


if __name__ == "__main__":
    main()
