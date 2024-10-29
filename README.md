# Python Package Index

This repository serves as a toolset for building and indexing Python packages.

## Supported Platforms

- **OS**: `windows-2019`, `ubuntu-24.04`, `macos-12(X64)`, `macos-14(ARM)`
- **Platforms**: `cpu`, `cuda`, `rocm` (see: `pytorch/get_jobs.py`)
- **Python**: `3.9` – `3.13`
- **PyTorch**: `1.11.0` – `2.5.1` (see: `pytorch/get_jobs.py`)

## Workflows

1. **PyTorch Packages Builder Workflow:**
   - Automates the building of PyTorch-based packages with custom ops on common architectures.
   - Publishes the built packages on GitHub releases.

2. **PEP 503 Compliant Package Index Builder Workflow:**
   - Creates a PEP 503-compliant package index.
   - Publishes the index using GitHub Pages for seamless integration with pip.

## Usage

You can install packages with :

```bash
pip install <package_name> --extra-index-url https://d-k-ivanov.github.io/packages-py
pip install <package_name> --find-links https://d-k-ivanov.github.io/torch_packages_builder/<pep 503 normalized name>

# Download and Install
pip install <package_path>
```

Example:

```bash
pip install pytorch3d==0.7.8+pt2.5.1cu124 --extra-index-url https://d-k-ivanov.github.io/packages-py
pip install pytorch3d==0.7.8+pt2.5.1cu124 --find-links https://d-k-ivanov.github.io/packages-py/pytorch3d/

# Download and Install
pip install ./pytorch3d-0.7.8+pt2.5.1cu124-cp311-cp311-linux_x86_64.whl
pip install ./pytorch3d-0.7.8+pt2.5.1cu124-cp311-cp311-win_amd64.whl
```

Make sure to include the full version, including the local version identifier (part after `+`). The repository follows this version template:

## Miscellaneous

**Package name**:

```bash
<package_name>-<version>+<OPTIONAL_commit_hash>pt<PyTorch_version><compute_platform>
```

Where:`<compute_platform>` is `cpu`, `cu<CUDA_version>`, `rocm<ROCM_version>`.

**No Support for Pip Cache:**
`pip` relies on http cache, and GitHub generates on-the-fly redirections for release links, so they are probably not playing nicely together.

## References

This repository is inspired by:

- [Miroslav Psota](https://github.com/MiroPsota/torch_packages_builder)
- [Matthias Fey](https://github.com/rusty1s/pytorch_cluster)
- [Nicolas Rémond](https://github.com/astariul/github-hosted-pypi)
- [PEP 503 – Simple Repository API](https://peps.python.org/pep-0503)
- [How to use GitHub as a PyPi server](https://www.freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2)
- [PyTorch Builder](https://github.com/pytorch/builder)
