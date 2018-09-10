import time
import timeit


def insertion_sort_by_max_speed(helicopters: list):
    print("Insertion sort:")
    comparing_times = 0
    change_times=0
    for i in range(0, len(helicopters)):
        comparing_times = comparing_times + 1
        comparing_helicopter = helicopters[i]
        n = i
        while n >= 0 and comparing_helicopter.max_speed > helicopters[n - 1].max_speed:
            change_times = change_times + 1
            helicopters[n] = helicopters[n - 1]
            n = n - 1
        change_times = change_times + 1
        helicopters[n] = comparing_helicopter
    print("Comparing times:" + str(comparing_times))
    print("Changing times" + str(change_times))


# def merge_sort_by_passengers_number(helicopters: list):
#    if


class Helicopter:
    def __init__(self, name, number_of_passengers, max_speed):
        self.name = name
        self.number_of_passengers = number_of_passengers
        self.max_speed = max_speed


def print_object(helicopter: Helicopter):
    print("Name: " + helicopter.name + " Number of passengers: " + str(helicopter.number_of_passengers) + " max speed: " + str(helicopter.max_speed))

def fun():
    hel1 = Helicopter("name", 3, 50)
    hel2 = Helicopter("name", 5, 51)
    hel3 = Helicopter("name", 4, 49)
    hel = [hel1, hel2, hel3]
    insertion_sort_by_max_speed(hel)
    for i in range(0, len(hel)):
        print(hel[i].max_speed)


def from_file_to_helicopters_list(path_to_file: str):
    file = open(path_to_file, "r")
    helicopters_list = []
    for line in file:
        string = line
        str_list = string.split(",")
        helicopter = Helicopter(str_list[0], str_list[1], (str_list[2])[:-2])
        helicopters_list.append(helicopter)
    return helicopters_list


def merge_sort(helicopters_list):
    print("Merge sort:")
    comparing_times = 0
    change_times = 0
    print("Splitting ", helicopters_list)
    if len(helicopters_list) > 1:
        mid = len(helicopters_list) // 2
        lefthalf = helicopters_list[:mid]
        righthalf = helicopters_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            comparing_times = comparing_times +1
            if lefthalf[i].number_of_passengers > righthalf[j].number_of_passengers:
                change_times = change_times + 1
                helicopters_list[k] = lefthalf[i]
                i = i + 1
            else:
                change_times = change_times + 1
                helicopters_list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            change_times = change_times + 1
            helicopters_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            change_times = change_times + 1
            helicopters_list[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", helicopters_list)
    for i in range(0, len(helicopters_list)):
        print(helicopters_list[i].number_of_passengers)
    print("Comparing times:" + str(comparing_times))
    print("Changing times" + str(change_times))
    return helicopters_list


hel1 = Helicopter("name", 3, 50)
hel2 = Helicopter("name", 5, 51)
hel3 = Helicopter("name", 4, 49)
alist = [hel1, hel2, hel3]
merge_time_start = time.process_time()
merge_time_stop = time.process_time()
for i in merge_sort(from_file_to_helicopters_list("file.cvs")):
    print_object(i)
print("CPU process time:  [sec]" + str((merge_time_stop - merge_time_start)))
print(alist)
