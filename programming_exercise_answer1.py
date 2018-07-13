
# coding: utf-8

# In[35]:

"""
This module will sort all records from input file into a json output file
(by using ages and states)
"""
# Import packages
import json
import pandas as pd

# Define a function to read, analysis and write the output file
def demographic_analysis(input_file_name, output_file_name):
    """
    This function is used to read input file;
    list all records (people name and their ages) by state and ages;
    and write the output as a JSON file.
    """
    # Read csv file into dataframe
    data_frame = pd.read_csv(input_file_name, index_col=0)
    # Prepare test data by adding 'name' column to dataframe
    data_frame['name'] = data_frame['first_name'] + " " + data_frame['last_name']
    # Rearrange columns in dataframe
    data_frame = data_frame[['name', 'email', 'gender', 'state', 'age']]
    # Convert dataframe to json
    test_data = data_frame.to_json(orient='records')
    python_obj = json.loads(test_data)
    # Get a list of states from records
    states_list = set(data_frame['state'])
    # Create empty dictionary properpties
    state_dict = {}
    # For each state in the states_list
    for state in states_list:
        age_25_higher_list = []
        age_25_lower_list = []
        age_dict = {}
        for record in python_obj:
            name_age_data = {
                k : v for k, v in filter(lambda t: t[0] in ['name', 'age'], record.items())}
            if record['state'] == state:
                if record['age'] > 25:
                    age_25_higher_list.append(name_age_data)
                    age_dict['Older Than 25'] = age_25_higher_list
                elif record['age'] <= 25:
                    age_25_lower_list.append(name_age_data)
                    age_dict['25 and Younger'] = age_25_lower_list
        state_dict[state] = age_dict
    # Write output into a JSON file,'output.json
    with open(output_file_name, 'a') as output_file:
        output = json.dumps(state_dict, indent=1)
        output_file.write(output)

# Execute function with parameters, input file name and output file name
demographic_analysis('exercise_test_data.csv', 'excercise_output_file10.json')

