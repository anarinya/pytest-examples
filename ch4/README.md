# Notes

### Built-in Fixtures
*capfd*
Like capsys, but captures file descriptors 1 and 2, which usually is the same as stdout and stderr.

*capsysbinary*
Where capsys captures text, capsysbinary captures bytes.

*capfdbinary*
Captures bytes on file descriptors 1 and 2.

*caplog*
Captures output written with the logging package.

### What is a monkey patch?
A dynamic modification of a class or module during runtime. During testing, it's a convenient way of taking over part of the runtime environment of the code under test and replace either input dependencies or output dependencies with objects or functions that are more convenient for testing. Mini version of mocking.

Provides the following functions:

*setattr(target, name, value, raising=True)* - sets an attribute

*delattr(target, name, raising=True)* - deletes an attribute

*setitem(dic, name, value)* - sets a dictionary entry

*delitem(dic, name, raising=True)* - deletes a dictionary entry

*setenv(name, value, prepend=None)* - sets an environment variable

*delenv(name, raising=True)* - deletes an environment variable

*syspath_prepend(path)* - prepends path to sys.path, which is Python's list of import locations

*chdir(path)* - changes the current working directory

The raising parameter tells pytest whether or not to raise an exception if the item doesn't already exist. The prepend parameter to setenv() can be a character. If it is set, the value of the environment variable will be changed to value + prepend + old value.

### Other Fixtures
*capfd, capfdbinary, capsysbinary* - variants of capsys that work with file descriptors and/or binary output

*caplog* - similar to capsys, used for messages created with Python's logging system

*cache* - used to store and retrieve values across pytest runs. The most useful part of this fixture is that it allows for --last-failed, --failed-first, and similar flags

*doctest_namespace* - useful if you like to use pytest to run doctest-style tests

*pytestconfig* - used to get access to configuration values, pluginmanager, and plugin hooks

*record_property, record_testsuite_property* - used to add extra properties to the test or test suite. Especially useful for adding data to an XML report to be used by continuous integration tools

*recwarmn* - used to test warning messages

*request* - used to provide information on the executing test function. Most commonly used during fixture parameterization

*pytester, testdir* - used to provide a temporary test directory to aid in running and testing pytest plugins. pytester is the pathlib based replacement for the py.path based testdir

*tmpdir, tmpdir_factory* - similar to tmp_path and tmp_path_factory; used to return a py.path.local object instead of a pathlib.Path object