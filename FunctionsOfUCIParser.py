# -*- coding: utf-8 -*-


import numpy


NA_VALUE = 1000


def get_file_path():
    FilePath = input("Please enter the path to the file:")
    FilePath = FilePath.rstrip()
    return FilePath


def file_to_2D_array(PathToData, PathToDescription=None, NA_Value=NA_VALUE):

    def description_to_list(PathToDescription):
        List = []
        with open(PathToDescription) as File:
            for line in File:
                line = line.rstrip()
                Line = line.split(",")
                List.append(Line)
        return List

    def convert(Line, Mode):
        for i in range(len(Line)):
            try:
                Line[i] = float(Line[i])
            except ValueError:
                if Line[i] == "N/A":
                    Line[i] = -NA_Value
                elif Line[i] not in Dummies[i]:
                    Dummies[i].append(Line[i])
                    Line[i] = len(Dummies[i]) + Mode * NA_Value
                else:
                    Line[i] = Dummies[i].index(Line[i]) + Mode * NA_Value + 1
        return Line

    Features = []
    with open(PathToData) as Data:
        if not PathToDescription:
            Dummies = []
            Mode = 1
            line = Data.readline()
            line = line.rstrip()
            Line = line.split(",")
            for i in range(len(Line)):
                Dummies.append([])
            Features.append(convert(Line, Mode))
        else:
            Dummies = description_to_list(PathToDescription)
            Mode = 0
        for line in Data:
            line = line.rstrip()
            Line = line.split(",")
            Features.append(convert(Line, Mode))
    return numpy.array(Features)


def functions_unit_test():
    TestString = get_file_path()
    assert TestString == TestString.rstrip()
    print(TestString)
    print("\n")
    DataPath = "/home/kolya/Документы/PythonNinja/DataSets/Cars"
    DataDescription = "/home/kolya/Документы/PythonNinja/DataSets/CarsDescr"
    x = file_to_2D_array(DataPath, DataDescription)
    print(x)
    print(x[100][4])
    x = file_to_2D_array(DataPath, None, 10)
    print(x)
    print(x[100][4])
    DataPath = "/home/kolya/Документы/PythonNinja/DataSets/Et_H_CO_n"
    x = file_to_2D_array(DataPath)
    print(x)
    print(x[100][4])


def main():
    functions_unit_test()


if __name__ == "__main__":
    main()


#TODO urlopen
