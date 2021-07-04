##########################################################################
# pytest script for Session9 assignment
#
# Ganesan Thiagarajan, 4th July 2021
##########################################################################
#
import session9
import pytest
import inspect
import os
import re
import decimal
from math import isclose


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


# test cases for namedtuples random group
# Test 1: Create the random population of 10000 people
def test_profile_create_tuples():
    num_profiles = 100
    profile_list = session9.create_fake_profile_tuples(num_profiles)
    assert profile_list != None, "Profile creation failed"
    assert len(profile_list) == num_profiles, "No. of created profiled do not match"
    assert all([1 <= profile_list[i].age <= 120 for i in range(num_profiles)]), "The age of profile exceeds the limits"


# Test 2: Check for the blood group type
# Find the majority blood group
def test_blood_group_tuples():
    num_profiles = 100
    profile_list = session9.create_fake_profile_tuples(num_profiles)
    max_bg_type, max_cnt = session9.find_max_blood_group_tuples(profile_list)
    assert max_bg_type in ['a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-'], "Blood group is invalid"
    assert max_cnt <= num_profiles, "No. of people with same blood group exceeds the max. number"
    assert max_bg_type != None, "Blood group is invlaid"


# Test 3: Check for mean location
def test_mean_location_tuples():
    # Get the mean location
    num_profiles = 100
    profile_list = session9.create_fake_profile_tuples(num_profiles)
    mean_latt, mean_long = session9.find_mean_latt_long_tuples(profile_list)
    assert mean_latt != 0 and mean_long != 0, "Highly improbable event"
    assert abs(mean_latt) < 90, "Mean lattitude is wrong"
    assert abs(mean_long) < 180, "Mean longitude is wrong"


# Test 4: Check for the mean and average age
def test_mean_max_age_tuples():
    # Get the mean location
    num_profiles = 100
    profile_list = session9.create_fake_profile_tuples(num_profiles)
    max_age, avg_age = session9.find_max_avg_age_tuples(profile_list)
    assert avg_age > 0 and max_age > 0, "Maximum and average age must be +ve"
    assert max_age > avg_age, "Mean age cannot be more than the avg age"
    assert max_age != avg_age, "Age conundrum"


# Test 5: Check the contents of the profiles created
def test_profile_contents_tuples():
    num_profiles = 100
    profile_list = session9.create_fake_profile_tuples(num_profiles)
    assert all([1 <= profile_list[i].age <= 120 for i in range(num_profiles)]), "The age of profile exceeds the limits"
    assert all([type(profile_list[i].name) is str for i in range(num_profiles)]), "Name must be a string"
    assert all([type(profile_list[i].lattitude) is decimal.Decimal for i in
                range(num_profiles)]), "Lattitude must be a decimal number"
    assert all([type(profile_list[i].longitude) is decimal.Decimal for i in
                range(num_profiles)]), "Longitude must be a decimal number"
    assert all([type(profile_list[i].age) is int for i in range(num_profiles)]), "Longitude must be a number"
    assert all([type(profile_list[i].blood_group) is str for i in range(num_profiles)]), "blood_group must be a string"


# Test 6: Check the docstrings for all functions in session9 module
def test_func_doc_strings():
    # Get all functions from session9
    func_list = [o for o in inspect.getmembers(session9) if inspect.isfunction(o[1])]
    for fn in [f[0] for f in func_list]:
        assert session9.check_doc_string(
            getattr(session9, fn)) == True, "Not enough details in the docstring for function " + fn


# test cases for dictionaries random group
# Test 1: Create the random population of 10000 people
def test_profile_create_dict():
    num_profiles = 100
    profile_list = session9.create_fake_profile_dict(num_profiles)
    assert profile_list != None, "Profile creation failed"
    assert len(profile_list) == num_profiles, "No. of created profiled do not match"
    assert all(
        [1 <= profile_list[i]['age'] <= 120 for i in range(num_profiles)]), "The age of profile exceeds the limits"


# Test 2: Check for the blood group type
# Find the majority blood group
def test_blood_group_dict():
    num_profiles = 100
    profile_list = session9.create_fake_profile_dict(num_profiles)
    max_bg_type, max_cnt = session9.find_max_blood_group_dict(profile_list)
    assert max_bg_type in ['a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-'], "Blood group is invalid"
    assert max_cnt <= num_profiles, "No. of people with same blood group exceeds the max. number"
    assert max_bg_type != None, "Blood group is invlaid"


# Test 3: Check for mean location
def test_mean_location_dict():
    # Get the mean location
    num_profiles = 100
    profile_list = session9.create_fake_profile_dict(num_profiles)
    mean_latt, mean_long = session9.find_mean_latt_long_dict(profile_list)
    assert mean_latt != 0 and mean_long != 0, "Highly improbable event"
    assert abs(mean_latt) < 90, "Mean lattitude is wrong"
    assert abs(mean_long) < 180, "Mean longitude is wrong"


# Test 4: Check for the mean and average age
def test_mean_max_age_dict():
    # Get the mean location
    num_profiles = 100
    profile_list = session9.create_fake_profile_dict(num_profiles)
    max_age, avg_age = session9.find_max_avg_age_dict(profile_list)
    assert avg_age > 0 and max_age > 0, "Maximum and average age must be +ve"
    assert max_age > avg_age, "Mean age cannot be more than the avg age"
    assert max_age != avg_age, "Age conundrum"


# Test 5: Check the contents of the profiles created
def test_profile_contents_dict():
    num_profiles = 100
    profile_list = session9.create_fake_profile_dict(num_profiles)
    assert all(
        [1 <= profile_list[i]['age'] <= 120 for i in range(num_profiles)]), "The age of profile exceeds the limits"
    assert all([type(profile_list[i]['name']) is str for i in range(num_profiles)]), "Name must be a string"
    assert all([type(profile_list[i]['lattitude']) is decimal.Decimal for i in
                range(num_profiles)]), "Lattitude must be a decimal number"
    assert all([type(profile_list[i]['longitude']) is decimal.Decimal for i in
                range(num_profiles)]), "Longitude must be a decimal number"
    assert all([type(profile_list[i]['age']) is int for i in range(num_profiles)]), "Longitude must be a number"
    assert all(
        [type(profile_list[i]['blood_group']) is str for i in range(num_profiles)]), "blood_group must be a string"


# Test case 1: Test for invalid inputs for creating the stock list
def test_stock_list_create1():
    with pytest.raises(TypeError, match=r".*No. of stocks must be greater than 0*"):
        stocks_list = session9.create_fake_stocks_tuples(0)


def test_stock_list_create2():
    with pytest.raises(TypeError, match=r".*No. of stocks must be positive integer*"):
        stocks_list = session9.create_fake_stocks_tuples(1.1)


def test_stock_list_create3():
    stocks_list = session9.create_fake_stocks_tuples(1)
    assert len(stocks_list) == 1, "No. of stocks in the list not matching"


# Test case 2: Test for invalid data type values in the stock list
def test_stock_list_data_type():
    stocks_list = session9.create_fake_stocks_tuples(5)
    for i in range(len(stocks_list)):
        assert ((type(getattr(stocks_list[i], 'name')) is str) and (type(getattr(stocks_list[i], 'symbol')) is str) and
                (type(getattr(stocks_list[i], 'open')) is float) and (
                            type(getattr(stocks_list[i], 'close')) is float) and
                (type(getattr(stocks_list[i], 'high')) is float) and (
                            type(getattr(stocks_list[i], 'low')) is float)) == True, "Wrong data type in stock list"


# Test case 3: Test for invalid length in the symbol string
def test_stock_symbol_len():
    stocks_list = session9.create_fake_stocks_tuples(50)
    for i in range(len(stocks_list)):
        # print(len(getattr(stocks_list[i],'symbol')))
        assert len(getattr(stocks_list[i], 'symbol')) == 6, "Symbol length is wrong"


# Test case 4: Test for invalid values of open, close, hi and lo
def test_stock_hi_lo_values():
    stocks_list = session9.create_fake_stocks_tuples(100)
    for i in range(len(stocks_list)):
        # print(stocks_list[i].open, stocks_list[i].high, stocks_list[i].low, stocks_list[i].close)
        assert ((stocks_list[i].high > stocks_list[i].low) or
                (stocks_list[i].high > stocks_list[i].open) or
                (stocks_list[i].high > stocks_list[i].close)), "Stock high value is wrong"
        assert ((stocks_list[i].low < stocks_list[i].high) or
                (stocks_list[i].low < stocks_list[i].open) or
                (stocks_list[i].low < stocks_list[i].close)), "Stock low value is wrong"


# Test case 5: Test for invalid number of entries in the stock list
def test_num_stock_values():
    stocks_list = session9.create_fake_stocks_tuples(17)
    assert (len(stocks_list) == 17), "No. of stocks in index is not correct"


# Test case 6: Test for invalid weights used in the index
def test_stock_weight_values():
    stocks_list = session9.create_fake_stocks_tuples(17)
    wts = session9.set_stock_weights(stocks_list)
    # print(f'Sum of weights = {sum(wts)}, No. of weights = {len(wts)}')
    assert isclose(sum(wts), 1.0), "All weights must constitute 100%"


# Test case 7: Test for invalid range of the weight values
def test_stock_weight_range():
    stocks_list = session9.create_fake_stocks_tuples(17)
    wts = session9.set_stock_weights(stocks_list)
    assert all([0 <= wts[i] < 1 for i in range(len(wts))]) == True, "All weights must be less than 100%"


# Test case 8: Test for -ve values in weight values
def test_stock_weight_sign():
    stocks_list = session9.create_fake_stocks_tuples(17)
    wts = session9.set_stock_weights(stocks_list)
    # print([wts[i] for i in range(len(wts))])
    assert all([wts[i] >= 0 for i in range(len(wts))]) == True, "Weights cannot be negative"


# Test case 9: Test for zero values in stock values
def test_stock_zero_values():
    stocks_list = session9.create_fake_stocks_tuples(10)
    for i in range(len(stocks_list)):
        assert all([[stocks_list[i].low > 0, stocks_list[i].open > 0, stocks_list[i].close > 0, stocks_list[i].high > 0]
                    for i in range(len(stocks_list))]) == True, "Zero stock values not expected"


# Test case 10: Test for rounding errors in index computation
def test_index_round_off():
    stocks_list = session9.create_fake_stocks_tuples(10)
    wts = session9.set_stock_weights(stocks_list)
    Sopen, Shi, Slow, Sclose = session9.calc_index_value(stocks_list, wts)
    index_close, index_open, index_high, index_low = 0, 0, 0, 0

    for i in range(len(stocks_list)):
        index_close += stocks_list[i].close * wts[i]
        index_open += stocks_list[i].open * wts[i]
        index_high += stocks_list[i].high * wts[i]
        index_low += stocks_list[i].low * wts[i]
        #print(i, index_low, index_high, index_high, index_close)

    assert (isclose(index_close, Sclose) and isclose(Sopen, index_open) and
            isclose(index_high, Shi) and isclose(index_low, Slow)), "Rounding error is too high"

# End of file

# End of test_session9
