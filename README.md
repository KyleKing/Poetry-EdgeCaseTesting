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
conda activate base
poetry shell
poetry run pyinstaller main.py --clean --noconfirm

# Try running the output
./build/main/main
```
