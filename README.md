# Edge Case Testing

Used in the now closed [Poetry-PR955](https://github.com/sdispater/poetry/pull/955) (23Jun2019) to test Poetry lock file behavior between Mac/Windows

## Reproduction Script

On Mac/Linux, then on Windows, run:

```sh
git clone https://github.com/KyleKing/Poetry-EdgeCaseTesting.git
cd Poetry-EdgeCaseTesting
poetry install
git status
poetry run python main.py
```
