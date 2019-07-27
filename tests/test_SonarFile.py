import SMSONAR._SonarFile as SF
import pytest


SonarFileSamplePath = 'FilePath'
SonarFileSamplePathInt = 3


def test_test():
    assert True


def test_call_file_super_class():
    assert bool(SF.SonarFile()) is True


def test_open_sonar_file():
    assert bool(SF.SonarFile(SonarFileSamplePath)) is True


def test_open_sonar_file_passing_none_str_input_as_file_name_fails_to_open():
    with pytest.raises(ValueError) as e:
        assert SF.SonarFile(SonarFileSamplePathInt)
    assert str(e.value) == ('Unexpected type of input for filePath.' +
                            ' Expected string, but integer was given.')


# def test_open_sonar_file_given_invalid_path_fails():
#     assert False


if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.getcwd())
