# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

import os

# PROBLEM 01

def read_file(filepath):
    """Reads text file and returns each line as a list element.

    Parameters:
        filepath (str): path to file

    Returns
        list: list of all lines in the file
    """
    return_data = []
    with open(filepath, 'r', encoding='utf-8') as input_file:

        for item in input_file.readlines():
            return_data.append(item.strip())

        return return_data

filepath = 'project_data.txt' # Gradescope

# Create filepath using the os module (COMMENT OUT BEFORE SUBMITTING TO GRADESCOPE)
# abs_path = os.path.dirname(os.path.abspath(__file__))
# filepath = os.path.join(abs_path, 'project_data.txt')

projects = read_file(filepath)
print(f"\n1.0 {projects}")

# PROBLEM 02
def get_filtered_projects(projects,categories):
    """
    This function returns a filtered list of projects based on one or more passed in categories.

    Parameters:
        projects (list): a list of strings that represent project information.
        categories (list): list of categories used as filters

    Returns:
        list: A filtered list of tuples. Each tuple contains both project name and project goal
    """

    return_data = []
    for project in projects:
        project_type, project_name, project_goal = project.split(',')
        for category in categories:
            if category.lower() in project_type.lower():
                return_data.append((project_name, project_goal))

    return return_data

categories = ['data', 'UI/UX']
data_ux_projects = get_filtered_projects(projects, categories)

print(f"\n2.0 {data_ux_projects}")

# PROBLEM 03
def write_file(filepath, output_list):

    with open(filepath, 'w') as output_file:
        for item in output_list:
            output_file.writelines(f"{item}\n")

write_file('data_ux_projects.txt', data_ux_projects)