
import math
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    user_input = input()
    input_list_strings = user_input.split(",")
    input_list_float = []
    for i in input_list_strings:
        decimal = float(i)
        input_list_float.append(decimal)
    return input_list_float


def calc_average(temp_list):
    average_list = sum(temp_list)/len(temp_list)
    return average_list

def find_min_max(temp_list):
    min_max_list = [max(temp_list), min(temp_list)]
    return min_max_list


def sort_temperature(temp_list):
    print("sort_temperature")

def calc_median_temperature(temp_list):
    temp_list_ascending = []
    smallest = math.inf
    for temperature in temp_list:
        if temperature < smallest:
            smallest = temperature
            temp_list_ascending.append(smallest)
    if (len(temp_list_ascending) % 2 == 0):
        median_index1 = (len(temp_list_ascending) // 2) - 1
        median_index2 = (len(temp_list_ascending) // 2)
        median_bottom = temp_list_ascending[median_index1]
        median_top = temp_list_ascending[median_index2]
        median = (median_top + median_bottom) / 2
        return median
    else:
        median_index = int((0 + (len(temp_list_ascending) - 1 ) ) / 2)
        return temp_list_ascending[median_index]
        

        


            



