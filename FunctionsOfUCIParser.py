# -*- coding: utf-8 -*-


def get_file_path():
    FilePath = input("Please enter the path to the file:")
    FilePath = FilePath.rstrip()
    return FilePath


def file_to_list(StringOfPath):
    ListOfLists = []
    with open(StringOfPath) as File:
        for line in File:
            Line = line.split(",")
            for i in range(len(Line)):
                Line[i] = float(Line[i])
            ListOfLists.append(Line)
    print(ListOfLists)
    return ListOfLists


def functions_unit_test():
    TestString = get_file_path()
    assert TestString == TestString.rstrip()
    print(TestString)
    file_to_list("/home/kolya/Документы/PythonNinja/DataSets/Et_H_CO_n")


def main():
    functions_unit_test()


if __name__ == "__main__":
    main()
