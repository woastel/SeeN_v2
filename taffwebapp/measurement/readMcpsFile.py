
import os
import csv


class readMcpsStatisticFile(object):




    def __init__(self, mcpsfile, user="noname"):

        self.__file = mcpsfile
        self.__user = user
        self.__tempFile1 = str("temp_mcpsfile1_{}.csv".format(self.__user))
        self.__tempFile2 = str("temp_mcpsfile2_{}.csv".format(self.__user))

        self.__mcpsInfoLine = str("")

        self.__sensorName_dict = {}
        self.__sensorMax_dict = {}
        self.__sensorValue_dict = {}


        # erstmal das file ckecken
        try:
            if (self.__fileckeck(self.__file) == True):
                print("DEBUG: Fileckeck is True")
            else:
                print("DEBUG: Fileckeck is False")
        except:
            print("ERROR: Fileckeck False")


        try:
            if (self.__read_file(self.__file) == True):
                print("DEBUG: file read pass")
            else:
                print("DEBUG: Error read file")
        except:
            print("ERROR: Fileckeck False")

        self.__print_sensorDate()

    def __fileckeck(self, mcpsfile):
        """
            Method: __fileckeck (privat)
            Parameter: filee is the mcps file
            Return: Bool --> True or False
            Description:
                This method ckeck if the file is a mcps statistik file.
        """
        print("DEBUG: fileckecker muss noch implementiert werden ")

        return(True)

    def __read_file(self, mcpsfile):

        # das file wird von django als binary format gelesen deswegene muss
        #   das file erstemal im binary mode abgespeichert werden
        with open(self.__tempFile1, "wb") as fileTemp:
            for i in mcpsfile:
                fileTemp.write(i)


        lines = []
        with open(self.__tempFile1, "r", encoding='utf-8', errors='ignore') as fileMessung:
            # speichern der Zeilen in die liste
            for i in fileMessung:
                lines.append(i)


        # vor dem loeschen der zeilen nochmal die info zeile abspeichern
        self.__mcpsInfoLine = str(lines[0])

        # loeschen der zeilen 3 = [2] und 1 = [0]
        del(lines[2])
        del(lines[0])


        with open(self.__tempFile2, "w", encoding="utf-8", errors="ignore") as fileTemporary:
            for i in lines:
                fileTemporary.write(str(i))

        fileTemporary.close()



        with open(self.__tempFile2, "r") as myfile:
            xcountt = 0
            reader = csv.DictReader(myfile, delimiter='\t')

            for row in reader:
                xcountt = xcountt + 1

                # Sensor Name Dict generieren
                sensorName_str = str(row["Messstelle"]) + str(row["Kommentar"])
                sensorName_str_format = sensorName_str.replace("\t", "   ")
                sensorName_dict_t = {"name{}".format(xcountt):sensorName_str_format}
                self.__sensorName_dict.update(sensorName_dict_t)


                # sensor Maximal Wert einlesen (Grenzwert)
                # erstmal muss der sting umgedreht werden
                sensorMax_str = sensorName_str[::-1]
                # jetzt koennen auch die max werte ausgelesen werden die max
                # werte sehen jetzt ganz am anfang vom string
                # hier werden die ersten 3 zeichen des strings eingelesen
                sensorMax_str_format = sensorMax_str[:3]
                # jetzt muss wieder umgedreht werden
                sensorMax_str_format = sensorMax_str_format[::-1]

                # versuchen in float zu konvertieren
                #   falls es nicht geht einfach eine 0 nehmen
                try:
                    a = {"max{}".format(xcountt):float(sensorMax_str_format)}
                except:
                    a = {"max{}".format(xcountt):float(0)}

                # jetzt hinzufuegen
                self.__sensorMax_dict.update(a)

                # sensor Value Wert einlesen (Gemessener Wert)
                sensorValue_str = str(row["Maximimum"])
                sensorValue_str_format = sensorValue_str.replace(",", ".")

                try:
                    # string None nicht typ None
                    if sensorValue_str_format is 'None':
                        sensorMax_dict_t = {"value{}".format(xcountt):float(0)}
                        self.__sensorValue_dict.update(sensorMax_dict_t)
                    else:
                        sensorMax_dict_t = {"value{}".format(xcountt):float(sensorValue_str_format)}
                        self.__sensorValue_dict.update(sensorMax_dict_t)
                    # sensor Diff liste berechnen und abspeicher
                    #   wenn der wert "-" negativ ist dann
                    #   ist der grenzwert überschritten
                except:
                    sensorMax_dict_t = {"value{}".format(xcountt):float(0)}
                    self.__sensorValue_dict.update(sensorMax_dict_t)


            # jetzt die liste noch auf einen gewuenschten wert aufrunden
            wunschwert = 60

            if xcountt != wunschwert:
                for aa in range(xcountt, wunschwert + 1):
                    self.__sensorMax_dict.update({"max{}".format(aa):float(0)})
                    self.__sensorName_dict.update({"name{}".format(aa):"name"})
                    self.__sensorValue_dict.update({"value{}".format(aa):float(0)})


        return(True)

    def __print_sensorDate(self):
        table_form = "| {:4} | {:60} | {:10} | {:10} |"
        print("-"*97)
        print(table_form.format("id", "name", "max", "value"))
        print("-"*97)


        for i in range(len(self.__sensorName_dict)):
            print(table_form.format(
                    i+1,
                    self.__sensorName_dict["name{}".format(i+1)],
                    self.__sensorMax_dict["max{}".format(i+1)],
                    self.__sensorValue_dict["value{}".format(i+1)]
                    ))

    def __get_mcpsInfoLine(self):
        return(self.__mcpsInfoLine)

    def __get_sensorName(self):
        return(self.__sensorName_dict)

    def __get_sensorMax(self):
        return(self.__sensorMax_dict)

    def __get_sensorValue(self):
        return(self.__sensorValue_dict)

    mcpsInfoLine = property(fget=__get_mcpsInfoLine, fset=None, fdel=None, doc="mcpsInfoLine property")
    sensorName   = property(fget=__get_sensorName,   fset=None, fdel=None, doc="sensorName property")
    sensorMax    = property(fget=__get_sensorMax,    fset=None, fdel=None, doc="sensorMax property")
    sensorValue  = property(fget=__get_sensorValue,  fset=None, fdel=None, doc="sensorValue property")
