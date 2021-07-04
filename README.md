# Session 9 Readme file 
# Assignment details:

# Problem #1
Use the Faker (Links to an external site.)library to get 10000 random profiles. 
Using namedtuple, 
    (a) calculate the largest blood type, 
    (b) mean-current_location, 
    (c) oldest_person_age,  and
    (d) average age (add proper doc-strings). 
    (e) include 5 test cases

# Solution 1
    * The profile was created with the namedtuple definition 
    profile = namedtuple('Profile', """ name, 
                                        age,
                                        lattitude,
                                        longitude,
                                        blood_group """)
    and faker() was used to fill in the details as follows
    profile_list.append(profile(fake.name(),                         # name
                                round(random.uniform(1,120)),        # age
                                fake.coordinate(),                   # latt
                                fake.longitude(),                    # long
                                random.choice(['a','b','ab','o'])+random.choice(['+','-'])  # bloodgroup
                           ))
    * The largest the blood group is calculated by counting the matching fields in a list expression
        aplus_cnt   = sum([profile_list[i].blood_group == 'a+'  for i in range(len(profile_list))])

    
# Solution 2
    * The following dictionary format was used to create a list of dictionaries similar to
    the namedtuples.     
    
    profile = dict(name = "sfsdf",
                   age = 12,
                   lattitude = Decimal(34.35),
                   longitude = Decimal(79.34),
                   blood_group = "o+")
    The following 5 tests are performed for the namestuples and dictionaries and the execution
    time is recorded
    a) Creation of the list of namedtuple profiles and length of the profiles list
    b) Validity of the content types in each field
    c) Maxinum and average age in the group.
    d) Average location as (latt, long)
    e) The bllod group with maximum number of people in the group
    
# Problem 2
   Create fake data (you can use Faker for company names) for imaginary stock exchange 
   for top 100 companies (name, symbol, open, high, close). 
   (a) Assign a random weight to all the companies. 
   (b) Calculate and show what value the stock market started at, 
       what was the highest value during the day, and where did it end. 
   (c) Make sure your open, high, close are not totally random. 
       You can *only use namedtuple*. 
   (d) include 10 test cases
   
# Solution

   * The following namedtuples were created with the template:
   
    o  Stock = namedtuple('stock', 'name, symbol, open, high, low, close')
    o A list of many such namedtuples were generated randomly for the given number of stocks
     in the index
    o A set of random weights chosen so that, total weights add upto 100% to represent
     the index
    o The stock index value is computed for open, high, low and close values from the 
     stock values and the weights function using a reduce function.
    o  index_open  = reduce(operator.add, [x*y for (x,y) in list(zip([stock_list[i].open for i in stocks_range],wt))])

# Test cases

   * The following test cases are added:
   
     o Test case 1: Test for invalid inputs for creating the stock list
     
     o Test case 2: Test for invalid data type values in the stock list
     
     o Test case 3: Test for invalid length in the symbol string
     
     o Test case 4: Test for invalid values of open, close, hi and lo
     
     o Test case 5: Test for invalid number of entries in the stock list
     
     o Test case 6: Test for invalid weights used in the index
     
     o Test case 7: Test for invalid range of the stock values
     
     o Test case 8: Test for -ve values in stock values
     
     o Test case 9: Test for zero values in stock values
     
     o Test case 10: Test for rounding errors in index computation
      
4. A readme file (this file) describes the code and solution approach and
   the test cases. 

5. A notebook which tests the above are given for varification in colab. 

# The following decorator functions are created for enabling the required functionalities

 * List of functions:
  
 1. timed() - Function decorator for checking run-time for critical functions
 2. check_doc_string() - Function which checks for valid docstring for all functions in the session9 module 
    This is used by the test script to evaluate.
 3. create_fake_profile_tuples() - Creates the list of random group of people using namedtuples
 4. find_max_blood_group_tuples() - Finds the bollg group with highest number of people in a group
 5. find_mean_latt_long_tuples() - Find the mean location of people in a group
 6. find_max_avg_age_tuples() - Finds the average age of people in a group
 7. create_fake_profile_dict() - Creates the list of random group of people using dictionary
 8. find_max_blood_group_dict() - Finds the bollg group with highest number of people in a group
 9. find_mean_latt_long_dict() - Find the mean location of people in a group
 10. find_max_avg_age_dict() - Finds the average age of people in a group
 11. create_fake_stocks_tuples() - Creates a list of stocks using namedtuples
 12. set_stock_weights() - Generates a set of random weights for the index
 13. calc_index_value() - Computes the index value based on the stocks and weights
 14. dummy_function() - To check the check_doc_string() failure test case - commented out to pass all test cases
 
 # End of file
 