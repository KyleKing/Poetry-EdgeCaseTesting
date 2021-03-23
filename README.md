# PyInstaller Test Case

Debugging PyInstaller

```sh
git clone https://github.com/KyleKing/Poetry-EdgeCaseTesting.git
cd Poetry-EdgeCaseTesting

poetry install

# Check that it works
poetry run python main.py
# > Running package_name!

# Build with PyInstaller
poetry shell
pyinstaller main.py --clean --noconfirm

# Try running the output
./build/main/main
```

```text
❯ ./dist/main/main
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    import package_name
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "PyInstaller/loader/pyimod03_importers.py", line 531, in exec_module
  File "package_name/__init__.py", line 3, in <module>
    pkg_resources.get_distribution('flask-compress').version
  File "pkg_resources/__init__.py", line 465, in get_distribution
  File "pkg_resources/__init__.py", line 341, in get_provider
  File "pkg_resources/__init__.py", line 884, in require
  File "pkg_resources/__init__.py", line 770, in resolve
pkg_resources.DistributionNotFound: The 'flask-compress' distribution was not found and is required by the application
[96148] Failed to execute script main
```
