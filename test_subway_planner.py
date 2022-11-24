import pytest

from subway_planner import find_line, stops, fares

def test_find_line():
    assert find_line("bajcsy-zsilinszky út", "deák ferenc tér") == "Line 1"
    assert find_line("kossuth lajos tér", "deák ferenc tér") == "Line 2"
    assert find_line("bikás park", "kálvin tér") == "Line 4"



def test_stops():
    assert stops("bikás park") == 5
    assert stops("bajcsy-zsilinszky út") == 1
    assert stops("lehel tér") == 3


def test_fares():
    assert fares(3, 5, "Line 3", "Line 4") == (8, "30-minute")
    assert fares(7, 4, "Line 1", "Line 2") == (11, "30-minute")
    assert fares(9, 7, "Line 3", "Line 1") == (16, "90-minute")