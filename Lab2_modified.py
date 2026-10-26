
import math,statistics

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(f"The median temperature is {calc_median_temperature(num_list)}")
    print(f"The average temperature is {calc_average(num_list)}")
    print(f"The lowest temperature is {find_min_max(num_list)[1]}")
    print(f"The highest temperature is {find_min_max(num_list)[0]} ")


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    user_input = input("Please input a string of temperatures: ")
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
    return statistics.median(temp_list)
    
        
if __name__ == "__main__":
    main()
        


            



