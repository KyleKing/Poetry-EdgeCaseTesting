# PR955-23Jun2019

Testing Poetry lock file behavior between Mac/Windows

Addresses: [Poetry-PR955](https://github.com/sdispater/poetry/pull/955). See comment in PR for full discussion, this is just a perma-linked demo

## Reproduction Script

```
# (On Mac)
# Build and install Poetry from Fork: https://github.com/KyleKing/poetry/tree/fix/944-select_wheel
poetry init
# Press Enter to all options
poetry add numpy

# (On Windows)
git clone https://github.com/KyleKing/Poetry-EdgeCaseTesting.git
cd Poetry-EdgeCaseTesting
poetry install
poetry lock

# Confirm that there is no text change to the poetry.lock file
```
