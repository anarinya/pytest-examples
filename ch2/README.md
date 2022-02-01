### Running a single test method, test class, or module
```
$ pytest test_classes.py::TestEquality::test_equality
$ pytest test_classes.py::TestEquality
$ pytest test_classes.py
```

### Running a single test function or module
```
$ pytest test_card.py::test_defaults
$ pytest test_card.py
```

### Run an entire directory
```
$ pytest ch2
```

### Run tests based on name keyword
```
$ pytest -v -k TestEquality
$ pytest -k TestEq
$ pytest -k equality
$ pytest -k "equality and not equality_fail"
$ pytest -k "(dict or ids) and not TestEquality"
```