# -*- coding: utf-8 -*-


def get_file_path():
    FilePath = input("Please enter the path to the file:")
    FilePath = FilePath.rstrip()
    return FilePath


def file_to_list(StringOfPath):
#    with open(StringOfPath) as File:
#        pass
#TODO: Copypaste the below code at the place of pass.
    ListOfLists = []
    with open("/home/kolya/Документы/PythonNinja/DataSets/Et_H_CO_n") as File:
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
    file_to_list(get_file_path())


def main():
    functions_unit_test()


if __name__ == "__main__":
    main()
