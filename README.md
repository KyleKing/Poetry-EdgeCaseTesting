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
# deactivate
conda activate base
poetry shell
# poetry run pyinstaller main.py --clean --noconfirm
poetry run pyinstaller main.py --clean --noconfirm --additional-hooks-dir hooks

# Try running the output
./dist/main/main
```

> FYI: hot reload doesn't work on frozen imports!
>
> `app.run_server(debug=False, dev_tools_hot_reload=not getattr(sys, 'frozen', False))`
