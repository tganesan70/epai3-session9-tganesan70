##########################################################################
# Session9 assignment for EPAi3
#
# Ganesan Thiagarajan, 4th July 2021
##########################################################################
#
from functools import wraps
from collections import namedtuple
from functools import reduce
import random
import operator

# Timed decorator for all functions - but using a global variable for elapsed time in case we want it at __main__ level
elapsed_time = 0


def timed(fn: 'Function name') -> 'Time for execution of the function':
    """
    A function decorator to compute the execution time for all the functions in this module when called
    from the test script.
    Params:
    fn - Function name
    Returns:
        Time for execution in seconds
    """
    from time import perf_counter
    @wraps(fn)
    def inner(*args, **kwargs):
        global elapsed_time
        start_time = perf_counter()
        result = fn(*args, **kwargs)
        end_time = perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function {fn.__name__}() took {elapsed_time} secs to execute")
        return result

    return inner


# Function decorator for checking the docstring of functions
def check_doc_string(
        fn: 'Function name that needs to be parsed') -> 'Returns True if the function has 50 words of description':
    """
    This function checks whether the function passed on to this has atleast 50 words of
    description.
    :param fn: Function name that is passed to this function
    :return: Returns a closure which allows the free variables can be accessed later
             The inner function Returns True if it has 50 or more words in its docstring description, else False
    Question: Will the docstring include the argument description function as well?  A BIG NO!
    """
    comment_len = 50
    """
    Doc string for inner function
    :param args: Positional arguments for the function
    :param kwargs:Function arguments for the function
    :return: The function output
    """
    if fn.__doc__ is None:
        return False
    else:
        fn_doc_string = fn.__doc__.split(sep=" ")
        # print(f'No. of words in the docstring comment for {fn.__name__}() is : {len(fn_doc_string)}')
        if len(fn_doc_string) < comment_len:
            return False
        else:
            return True


@timed
def create_fake_profile_tuples(num: 'Int - No. of profiles') -> 'Returns the list of Fake profiles (namedtuples)':
    """
    Params:
        num - No. of profiles
    Returns:
        list of namedtuples with the following fields in them:
              profile = namedtuple('profile', 'name, age, latt, ,long, blood_group')
    """
    from faker import Faker
    profile = namedtuple('Profile', 'name, age, lattitude, longitude, blood_group')
    profile_list = []
    for i in range(num):
        fake = Faker()
        profile_list.append(profile(fake.name(),
                                    round(random.uniform(1, 120)),
                                    fake.coordinate(),
                                    fake.longitude(),
                                    random.choice(['a', 'b', 'ab', 'o']) + random.choice(['+', '-'])))
    return profile_list


@timed
def find_max_blood_group_tuples(profile_list: 'list of Fake profiles (namedtuples)'):
    """
    Find the largest blood group in the list of profiles (namedtuples) with the format given as below
    Params: List of profiles of type
         profile = namedtuple('profile', 'name, age, latt, ,long, blood_group')
    Returns: The largest blood group in all the profiles
    """
    aplus_cnt = sum([profile_list[i].blood_group == 'a+' for i in range(len(profile_list))])
    aminus_cnt = sum([profile_list[i].blood_group == 'a-' for i in range(len(profile_list))])
    bplus_cnt = sum([profile_list[i].blood_group == 'b+' for i in range(len(profile_list))])
    bminus_cnt = sum([profile_list[i].blood_group == 'b-' for i in range(len(profile_list))])
    oplus_cnt = sum([profile_list[i].blood_group == 'o+' for i in range(len(profile_list))])
    ominus_cnt = sum([profile_list[i].blood_group == 'o-' for i in range(len(profile_list))])
    abplus_cnt = sum([profile_list[i].blood_group == 'ab+' for i in range(len(profile_list))])
    abminus_cnt = sum([profile_list[i].blood_group == 'ab-' for i in range(len(profile_list))])

    max_cnt = max([aplus_cnt, aminus_cnt, bplus_cnt, bminus_cnt, abplus_cnt, abminus_cnt, oplus_cnt, ominus_cnt])
    if max_cnt == aplus_cnt:
        return 'a+', max_cnt
    elif max_cnt == aminus_cnt:
        return 'a-', max_cnt
    elif max_cnt == bplus_cnt:
        return 'b+', max_cnt
    elif max_cnt == bminus_cnt:
        return 'b-', max_cnt
    elif max_cnt == abplus_cnt:
        return 'ab+', max_cnt
    elif max_cnt == abminus_cnt:
        return 'ab-', max_cnt
    elif max_cnt == oplus_cnt:
        return 'o+', max_cnt
    else:
        return 'o-', max_cnt


@timed
def find_mean_latt_long_tuples(
        profile_list: 'list of Fake profiles (namedtuples)') -> 'The mean lattitude and longitude of the location of the group':
    """
    Find the mean location (latt, long) for all people in the random group
    Params: List of profiles of type
         profile = namedtuple('profile', 'name, age, latt, ,long, blood_group')
    Returns: The mean location for the group
    """
    mean_latt = sum([profile_list[i].lattitude for i in range(len(profile_list))]) / len(profile_list)
    mean_long = sum([profile_list[i].longitude for i in range(len(profile_list))]) / len(profile_list)
    return mean_latt, mean_long


@timed
def find_max_avg_age_tuples(profile_list: 'list of Fake profiles (namedtuples)') -> 'The maximum age among the group':
    """
    Find the mean location (latt, long) for all people in the random group
    Params: List of profiles of type
         profile = namedtuple('profile', 'name, age, latt, ,long, blood_group')
    Returns: The maximum and average age in the group
    """
    max_age = max([profile_list[i].age for i in range(len(profile_list))])
    avg_age = round(sum([profile_list[i].age for i in range(len(profile_list))]) / len(profile_list))
    return max_age, avg_age


# The above functions recreated using list of dictionary instead namedtuples
@timed
def create_fake_profile_dict(num: 'Int - No. of profiles') -> 'Returns the list of Fake profiles (dictionaries)':
    """
    Params:
        num - No. of profiles
    Returns:
        list of dictionaries with the following fields in them:
              profile = dictionary('profile', 'name, age, latt, ,long, blood_group')
    """
    from faker import Faker
    # profile = dict(name = "",
    #               age = "",
    #               lattitude = "",
    #               longitude = "",
    #               blood_group = "")
    profile_list = []
    for i in range(num):
        fake = Faker()
        profile_list.append(dict(name=fake.name(),  # name
                                 age=round(random.uniform(1, 120)),  # age
                                 lattitude=fake.coordinate(),  # latt
                                 longitude=fake.longitude(),  # long
                                 blood_group=random.choice(['a', 'b', 'ab', 'o']) + random.choice(['+', '-'])
                                 # bloodgroup
                                 ))
    return profile_list


@timed
def find_max_blood_group_dict(profile_list: 'list of Fake profiles (dictionaries)'):
    """
    Find the largest blood group in the list of profiles (dictionaries) with the format given as below
    Params: List of profiles of type
         profile = namedtuple('profile', 'name, age, latt, ,long, blood_group')
    Returns: The largest blood group in all the profiles
    """
    aplus_cnt = sum([profile_list[i]['blood_group'] == 'a+' for i in range(len(profile_list))])
    aminus_cnt = sum([profile_list[i]['blood_group'] == 'a-' for i in range(len(profile_list))])
    bplus_cnt = sum([profile_list[i]['blood_group'] == 'b+' for i in range(len(profile_list))])
    bminus_cnt = sum([profile_list[i]['blood_group'] == 'b-' for i in range(len(profile_list))])
    oplus_cnt = sum([profile_list[i]['blood_group'] == 'o+' for i in range(len(profile_list))])
    ominus_cnt = sum([profile_list[i]['blood_group'] == 'o-' for i in range(len(profile_list))])
    abplus_cnt = sum([profile_list[i]['blood_group'] == 'ab+' for i in range(len(profile_list))])
    abminus_cnt = sum([profile_list[i]['blood_group'] == 'ab-' for i in range(len(profile_list))])

    max_cnt = max([aplus_cnt, aminus_cnt, bplus_cnt, bminus_cnt, abplus_cnt, abminus_cnt, oplus_cnt, ominus_cnt])
    if max_cnt == aplus_cnt:
        return 'a+', max_cnt
    elif max_cnt == aminus_cnt:
        return 'a-', max_cnt
    elif max_cnt == bplus_cnt:
        return 'b+', max_cnt
    elif max_cnt == bminus_cnt:
        return 'b-', max_cnt
    elif max_cnt == abplus_cnt:
        return 'ab+', max_cnt
    elif max_cnt == abminus_cnt:
        return 'ab-', max_cnt
    elif max_cnt == oplus_cnt:
        return 'o+', max_cnt
    else:
        return 'o-', max_cnt


@timed
def find_mean_latt_long_dict(
        profile_list: 'list of Fake profiles (dictionaries)') -> 'The mean lattitude and longitude of the location of the group':
    """
    Find the mean location (latt, long) for all people in the random group
    Params: List of profiles of type
         profile = namedtuple('profile', 'name, age, latt, ,long, blood_group')
    Returns: The mean location for the group
    """
    mean_latt = sum([profile_list[i]['lattitude'] for i in range(len(profile_list))]) / len(profile_list)
    mean_long = sum([profile_list[i]['longitude'] for i in range(len(profile_list))]) / len(profile_list)
    return mean_latt, mean_long


@timed
def find_max_avg_age_dict(profile_list: 'list of Fake profiles (dictionaries)') -> 'The maximum age among the group':
    """
    Find the mean location (latt, long) for all people in the random group
    Params: List of profiles of type
         profile = namedtuple('profile', 'name, age, latt, ,long, blood_group')
    Returns: The maximum and average age in the group
    """
    max_age = max([profile_list[i]['age'] for i in range(len(profile_list))])
    avg_age = round(sum([profile_list[i]['age'] for i in range(len(profile_list))]) / len(profile_list))
    return max_age, avg_age


# @timed
def create_fake_stocks_tuples(num: 'Int - No. of profiles') -> 'Returns the list of Fake profiles (namedtuples)':
    """
    Params:
        num - No. of profiles
    Returns:
        list of namedtuples with the following fields in them:
              Stock = namedtuple('stock', 'name, symbol, open, high, low, close')
    """
    from faker import Faker
    from random import uniform

    if num <= 0:
        raise TypeError("No. of stocks must be greater than 0")
    elif type(num) is not int:
        raise TypeError("No. of stocks must be positive integer")

    Stock = namedtuple('stock', 'name, symbol, open, high, low, close')
    stock_list = []
    for i in range(num):
        fake = Faker()
        name = fake.company()
        open_price = uniform(10, 1000)  # open price
        hi_price = open_price + uniform(10, 100)  # High price
        lo_price = open_price - uniform(10, 100)  # Low price
        close_price = uniform(lo_price, hi_price)  # close price
        stock_list.append(Stock(name,  # Company
                                "^" + str(name[:5]).upper(),  # Symbol
                                open_price,  # Open price
                                hi_price,  # high
                                lo_price,  # low
                                close_price))  # close price
    return stock_list


# Select random weight values for the stocks
def set_stock_weights(stocks_list: 'List of stocks (namedtuples)') -> 'Returns the weights of stocks in index value':
    """
    Function to select the random weights for the stocks to compute the index value
    Params:
        stock_list - List of stocks (namedtuples)
    Returns:
        weights - Weight for each company ticker symbol
    """
    num_stocks = len(stocks_list)
    weights = random.choices([i for i in range(100)], k=num_stocks)
    sum_weights = sum(weights)
    weights = [weights[i] / sum_weights for i in range(num_stocks)]  # make it 100 %
    return weights


def calc_index_value(stock_list: 'List of stocks (namedtuples)',
                     wt: 'index weights for company') -> 'Returns the index value':
    """
    Function to compute the value of the stock exchange based on the values stocks and their weights in the index
    Params:
        stock_list - List of stocks (namedtuples)
        weights - Weight for each company ticker symbol
    Returns:
        index - stock index value at open,hi, low and close
    """
    stocks_range = range(len(stock_list))
    index_open = reduce(operator.add, [x * y for (x, y) in list(zip([stock_list[i].open for i in stocks_range], wt))])
    index_close = reduce(operator.add, [x * y for (x, y) in list(zip([stock_list[i].close for i in stocks_range], wt))])
    index_hi = reduce(operator.add, [x * y for (x, y) in list(zip([stock_list[i].high for i in stocks_range], wt))])
    index_lo = reduce(operator.add, [x * y for (x, y) in list(zip([stock_list[i].low for i in stocks_range], wt))])
    return index_open, index_hi, index_lo, index_close

# def dummy_func():
#    # No comments to check docstring test fail case
#    pass

# End of file
