# Contents 
1. [Introduction](README.md#Intro)
2. [Additional Subroutines](README.md#sub)
3. [Solution Approach](README.md#solapp)
4. [Full Functionality Test ](README.md#FFT)
5. [Unit Test ](README.md#unit-test )


# Introduction 
Input data set contains information on prescription drug prescribed by healthcare providers. It contains id, prescriber last and first name, drug name and cost as comma separated items. ./output/itcont.txt is a smaller unit of original input sample data with 500000 data entry. 

# Additional Subroutines
I used two additional subroutines:

index_list : For a given sub-set of data this subroutine returns the indices from the original data set. 

count_frequency : For a given number, it returns the number of times that number repeats in a given data set. 

# Solution Approach 
./src/pharmacy‑counting.py initially declares number of data entry (NODE) of the input sample data itcont.txt. The main subroutine used for analysis named pharmacy_counting collects all column such as id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost of the txt data in data_c_dn_fn_ln_unit[] and cost_data_unit[] collects only the drug cost. L26 cleans up the entry if the entry splits more than 5 items since the header contain 5 unit. 

In step 2, data_c_dn_fn_ln_unit_v1[] was obtained from data_c_dn_fn_ln_unit[] since only last name and first name will be used to identify number of times a drug was prescribed to same individual. Sorted cost named as drug_cost[] where list items are float, has been used to identify indices ( L73: index[] ) to pick corresponding drug list ( L83: top_drugs_prescriber[] ).

L88: num_prescriber_rep[] data contains number of times top drugs were prescribed to same individuals that uses subroutine count_frequency and uses data_c_dn_fn_ln_unit_v1[] ( unsorted list of drug and its precriber ) and top_drugs_prescriber[] ( sorted list of drug and its prescriber using indices of top drugs and its prescriber in descending order ) as input to the subroutine. 

L109: top_drug_cost[] converts the costs in rounded $ to write the output top_cost_drug.txt

# Full Functionality Test
code: ./src/pharmacy‑counting.py

./output/itcont.txt has 500000. If I run ./src/pharmacy‑counting-full-functionality.py with 20000, it takes roughly a minute on my pc.
 
# Unit Test 
code: ./src/pharmacy‑counting-unit-test.py 

defines some global variables for running the test since the original input file contains roughly 24 million data points. NODE (number of data entry) variable allows to choose a subset of the input data that would be used for analysis. N allows to choose any percentile of the data say 50%, 10% or 1% of the input that would be used for analysis L54. 

N_unit_test is another global variable that can be varied to pick a subset of the data from any part of the original input. Parameters can be choosen such as;

factor = 10 

NODE = int(round(500000/factor))

N_unit_test = 10000

N_start = int(round(50000/2)) 

  
code: ./src/pharmacy‑counting.py with input ./insight_testsuite/tests/your‑own‑test_1/input/your_own_input_for_itcont.txt returns output 
./insight_testsuite/tests/your‑own‑test_1/output/top_cost_drug.txt. Here the input has only 25 lines including the header.
