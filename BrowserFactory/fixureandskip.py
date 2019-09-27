import pytest
#use below coe to get xml rport
#py.test fixureandskip.py -v --junitxml="result.xml"
@pytest.mark.skipif(1<2, reason="i dont want too run")
def test_Fixure1():
    print("asser1 is success")
def test_Fixture2():
    print("assert2 is success")