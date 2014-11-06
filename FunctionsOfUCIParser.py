# -*- coding: utf-8 -*-


import numpy


MAX_VALUE = 1000


def get_file_path():
    FilePath = input("Please enter the path to the file:")
    FilePath = FilePath.rstrip()
    return FilePath


#def file_to_list(StringOfPath):
#    ListOfLists = []
#    with open(StringOfPath) as File:
#        for line in File:
#            Line = line.split(",")
#            for i in range(len(Line)):
#                Line[i] = Line[i]
#            ListOfLists.append(Line)
#    return ListOfLists


def types_of_columns(PathToFile):
    ColumnsList = []
    with open(PathToFile) as File:
        line = File.readline()
        Line = line.split(",")
        for i in range(len(Line)):
            try:
                float(Line[i])
                ColumnsList.append(0)
            except ValueError:
                ColumnsList.append(1)
    return ColumnsList


#def convert(Element, DataType=float):
#    if DataType == float:
#        return float(Element)
#    elif DataType == int:
#        return int(Element)
#    elif DataType == str:
#        pass
#    else:
#        raise TypeError("Such type is not provided.")


#def parse(line, Values):
#    Line = line.split(",")
#    for i in range(len(Line)):
#        try:
#            Line[i] = float(Line[i])
#        except ValueError:
#            Line[i] = 0
#    return Line


def file_to_2D_array(PathToFile):

    def convert(Line):
        for i in range(len(Line)):
            try:
                Line[i] = float(Line[i])
            except ValueError:
                if Line[i] == "N/A":
                    Line[i] = -MAX_VALUE
                elif Line[i] not in Dummies[i]:
                    Dummies[i].append(Line[i])
                    Line[i] = MAX_VALUE + len(Dummies[i])
                else:
                    for j in range(len(Dummies[i])):
                        if Dummies[i][j] == Line[i]:
                            Line[i] = MAX_VALUE + j + 1
                            break
        return Line

    Features = []
    Dummies = []
    with open(PathToFile) as File:
        line = File.readline()
        line.strip()
        Line = line.split(",")
        for i in range(len(Line)):
            Dummies.append([])
        Features.append(convert(Line))
        for line in File:
            line.strip()
            Line = line.split(",")
            Features.append(convert(Line))
    return numpy.array(Features)


def functions_unit_test():
    TestString = get_file_path()
    assert TestString == TestString.rstrip()
    print(TestString)
    x = file_to_2D_array("/home/kolya/Документы/PythonNinja/DataSets/Cars")
    print(x)
#    print(x[100][4])
    x = file_to_2D_array("/home/kolya/Документы/PythonNinja/DataSets/Et_H_CO_n")
    print(x)
    print(x[100][4])


def main():
    functions_unit_test()


if __name__ == "__main__":
    main()
