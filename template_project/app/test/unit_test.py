import pytest
import pandas as pd
from src.main import function


@pytest.fixture
def df():
    filename = './test/data_test/train.csv'
    df = pd.read_csv(filename)
    return df


def test_readcsv(df):
    assert df.shape[0] == 50


def test_function_from_main():
    assert function() == "OK"
