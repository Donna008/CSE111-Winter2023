from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("marie","toussaint") == "toussaint;marie"
    assert make_full_name("olivier","toussanint") =="toussanint;olivier"
    assert make_full_name("g","wa") =="wa;g"
    assert make_full_name("","") ==";"


def test_extract_family_name():
    assert extract_family_name("marie; toussaint") =="marie"
    assert extract_family_name("olivier; toussaint") =="olivier"
    assert extract_family_name("george; washington") =="george"
    assert extract_family_name("; ") ==""

def test_extract_given_name():
    assert extract_given_name("Brown/ Sally") == "Sally"
    assert extract_given_name("Madison/ James") == "James"
    assert extract_given_name("Nel/ A") == "A"
    assert extract_given_name("/ ") == ""

pytest.main(["-v","--tb=line","-rN",__file__])