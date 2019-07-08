import sys
import os
sys.path.append(os.getcwd())
import pytest 
import SMSONAR._SonarFile as SF


def test_test():
    _=SF.SonarFile()
    assert True
