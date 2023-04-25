# This is my repository

## Project

### Documentation
The requirements definition can be found [here](https://github.com/kirkeruusalu/ot-practice/blob/master/documentation/requirements_specification.md)
The timekeeping document can be found [here](https://github.com/kirkeruusalu/ot-practice/blob/master/documentation/timekeeping.md)
The changelog file can be found [here](https://github.com/kirkeruusalu/ot-practice/blob/master/documentation/changelog.md) The arhitektuuri file can be found [here](https://github.com/kirkeruusalu/ot-practice/blob/master/documentation/arhitektuuri.md).

The release can be found [here](https://github.com/kirkeruusalu/ot-practice/releases/tag/week5).

### Running project code
Installing dependencies:
```
poetry install
```
Initalizing the code:
```
poetry run invoke begin
```
Starting the code:
```
poetry run invoke start
```

Running tests:
```
poetry run invoke test
```
Test coverage report:
```
poetry run invoke coverage-report
```
Pylint:
```
poetry run invoke lint
```






