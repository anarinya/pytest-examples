def hello():
    with open("hello.txt", "w") as f:
        f.write("Hello World!\n")


if __name__ == "__main__":
    hello()


def test_hello_output():
    # hello()
    with open("hello.txt", "r") as f:
        assert f.readline() == "Hello World!\n"


def test_hello_output_with_temp_dir(tmp_path, monkeypatch):
    print(tmp_path)
    monkeypatch.chdir(tmp_path)
    hello()
    with open("hello.txt", "r") as f:
        assert f.readline() == "Hello World!\n"
