# PyInstaller Test Case

Debugging PyInstaller

```sh
git clone https://github.com/KyleKing/Poetry-EdgeCaseTesting.git
cd Poetry-EdgeCaseTesting
git checkout dev/pyinstaller

poetry install

# Check that it works
poetry run python main.py
# > 1.9.0
# > Running package_name!

# Build with PyInstaller
poetry shell
pyinstaller main.py --clean --noconfirm

# Try running the output
./build/main/main
# > Error that flask-compress isn't found...
```

---

```py
# Modify and test with flask-compress versions
git clone https://github.com/KyleKing/flask-compress.git
cd flask-compress
git checkout fix/version

python setup.py bdist_wheel
```
