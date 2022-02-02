# Notes

### What fixtures do tests use?
The --setup-show option will output used fixtures and when teardown and setup happens.
```
$ pytest --setup-show test_count.py
```

### Scope
The default scope for fixtures is 'function' scope, which means the setup runs before each function that needs it.
It's expensive to setup and tear down a database after every test so it isn't suggested.

With a fixture defined within a test module, the *session* and *package* scopes act just like module scope. In order to make use of other scopes, they have to go into a *conftest.<area>py* file.

#### Types of scope:
**scope='function'**
Runs once per test function. The setup portion is rum before each test using the fixture. The teardown portion is run after each test using the fixture. This is the default scope used when no scope parameter is specified.

**scope='class'**
Runs once per test class, regardless of how many test methods are in the class.

**scope='module'**
Run once per module, regardless of how many test functions or methods or other fixtures in the module use it.

**scope='package'**
Run once per package, or test directory, regardless of how many test functions or methods or other fixtures in the package use it.

**scope='session'**
Run once per session. All test methods and functions using a fixture of session scope share one setup and teardown call.

### Note: Don't import conftest.<area>py
Although conftest.<area>py is a Python module, it should not be imported by test files. The conftest.<area>py file gets read by pytest automatically, so you dont have *import conftest* anywhere.

### Where is a fixture coming from?
Conftest.<area>py files can be anywhere, so how do you tell where a fixture is coming from?
```
$ pytest --fixtures -v
$ pytest --fixtures-per-test test_count.py::test_empty
```

### Autouse
Instead of passing in named fixtures to tests, it's possible to set *autouse=True* to get a fixture to run all the time without passing it in. This is meant to be used when tests don't depend on any system state or data from the fixture.
```
@pytest.fixture(autouse=True, scope="session")
def fixture_with_session_scope():
```

### Command line flag review
```
# order of execution:
pytest --setup-show

# list of available fixtures and their location:
pytest --fixtures

# allow print statements to be seen in passing tests
-s and --capture=no
```