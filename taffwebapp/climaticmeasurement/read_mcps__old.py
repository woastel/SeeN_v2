"""
Beispiel:
    zum erstellen einer Messung in der datenbank anhand einer MCPUs Statistik

in diesem kleinen script wird eine MCPS Statistik file eingelesen
und ausgewetet.
die angaben werden formatiert
"""

import csv
import os
from time import localtime
import settings


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class read_mcpsStatisticFile:
    def __init__(self, _filename):
        """
        object need a filename or path

            _filename = name of the mcps file

        """
        # Definieren der Sensor Value Listen

        self.__filename = str(_filename)
        self.__mcpsinfo = str("")  # the first line of the file

        self._newSensorName_list = []
        self._newSensorValue_list = []
        self._newSensorMax_list = []
        self._newSensorDiff_list = []

        self.__read_mcpsFile(self.__filename)

    def __read_mcpsFile(self, _filename):
        """
        (privat) __read_mcpsFile

        make the mcps File readabale
        (this fuking file has no standard)
        """

        # File der Messung einlesen
        #   fileMessungName = 'temp.xla'
        #   fileTemporaryName = '_temp.xla'
        fileMessungName = _filename
        lt = localtime()

        datetime_str = "{:04}{:02}{:02}_{:02}{:02}{:02}".format(
            lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec)

        """
        FUNKTION:
            hier kann entschieden werden ob man bei jedem mal aufrufen siech
            ein csv file erstellen will oder nicht

            das ist sozudagen das converting von xla mit tab nach cls
        """

        if settings.settingsTaff.MCPS_READ_LOG == "no":
            foldera = settings.settingsTaff.USER_DATA_FOLDER_TEMP
            fileTemporaryName = '{}mcps_read_tempfile.csv'.format(foldera)

        elif settings.settingsTaff.MCPS_READ_LOG == "yes":

            folder = settings.settingsTaff.MCPS_READ_FOLDER

            fileTemporaryName = str(
                '{}mcps_sensorvalues_{}.csv'.format(folder, datetime_str))

        print("CSV-File created: {}".format(fileTemporaryName))

        lines = []
        with open(fileMessungName, "r", encoding='utf-8', errors='ignore'
                  ) as fileMessung:
            # speichern der Zeilen in die liste
            for i in fileMessung:
                lines.append(i)

        # file schliesen
        fileMessung.close()

        # vor dem loeschen der zeilen nochmal die info zeile abspeichern
        self.__mcpsinfo = str(lines[0])
        print(self.__mcpsinfo)

        # loeschen der zeilen 3 = [2] und 1 = [0]
        del(lines[2])
        del(lines[0])

        # Ausgeben der formatierten liste

        # # x = 0
        # # for i in lines:
        # #     x = x + 1
        # #     print(str(x) + " -- " + i)

        # erstellen eines _temp.xla Files
        #fileTemporary = open(fileTemporaryName, "w")
        with open(fileTemporaryName, "w", encoding="utf-8", errors="ignore") as fileTemporary:
            # abspeichern der formatierten liste in das _temp.xla File
            for i in lines:
                fileTemporary.write(i)

        # schliesen des temp files
        fileTemporary.close()

        """
        Jetzt kann das temp-File wieder geoeffnet werden und die daten
        ausgelesen werden. Damit sie in der datenbank gespeichert werden
        koennen.
        """

        with open(fileTemporaryName, "r") as f:
            xcountt = 0
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                xcountt = xcountt + 1
                # Sensor Namen einlesen
                sensorName_str = str(row["Messstelle"]) + str(row["Kommentar"])
                sensorName_str_format = sensorName_str.replace("\t", "   ")
                self._newSensorName_list.append(sensorName_str_format)

                # sensor Maximal Wert einlesen (Grenzwert)
                # erstmal muss der sting umgedreht werden
                sensorMax_str = sensorName_str[::-1]
                # jetzt koennen auch die max werte ausgelesen werden die max
                # werte sehen jetzt ganz am anfang vom string
                # hier werden die ersten 3 zeichen des strings eingelesen
                sensorMax_str_format = sensorMax_str[:3]
                # jetzt muss wieder umgedreht werden
                sensorMax_str_format = sensorMax_str_format[::-1]
                try:
                    self._newSensorMax_list.append(float(sensorMax_str_format))
                except:
                    self._newSensorMax_list.append(float("0"))

                # sensor Value Wert einlesen (Gemessener Wert)
                sensorValue_str = str(row["Maximimum"])
                sensorValue_str_format = sensorValue_str.replace(",", ".")

                print("{} | {}   {} | {}  {} ".format(xcountt,
                                                      type(
                                                          sensorValue_str_format
                                                      ),
                                                      sensorValue_str_format,
                                                      type(sensorValue_str),
                                                      sensorValue_str))

                try:
                    #
                    # string None nicht typ None
                    if sensorValue_str_format is 'None':
                        self._newSensorValue_list.append(float(0))
                    else:
                        self._newSensorValue_list.append(
                            float(sensorValue_str_format))

                    # sensor Diff liste berechnen und abspeicher
                    #   wenn der wert "-" negativ ist dann
                    #   ist der grenzwert überschritten

                except:
                    self._newSensorValue_list.append(float(0))

        while(len(self._newSensorName_list) != 60):
            self._newSensorName_list.append("none")

        while(len(self._newSensorMax_list) != 60):
            self._newSensorMax_list.append(0)

        while(len(self._newSensorValue_list) != 60):
            self._newSensorValue_list.append(0)


        # jetz noch die temp diff list erstellen
        for i in range(len(self._newSensorValue_list)):
            self._newSensorDiff_list.append(self._newSensorMax_list[i] -
                                            self._newSensorValue_list[i])




        print("\n\n DEBUG\n\n")

        for i in self._newSensorName_list:
            print(i)

        for i in self._newSensorMax_list:
            print(i)
        for i in self._newSensorValue_list:
            print(i)
        for i in self._newSensorDiff_list:
            print(i)

        print("\n\n DEBUG\n\n")





    def print_sensorData(self):
        """
        (public)print_snesorData
            function to view the sensor data from the mcps statistic file
        """

        # Listen formatiert ausgeben
        table_form = " |  {:54} | {:10} | {:10} | {:10.3} |"
        table_form_red = str(bcolors.BOLD + bcolors.FAIL +
                             " |  {:54} | {:10} | {:10} | {:10.3} |" +
                             bcolors.ENDC)
        table_form_gelb = str(bcolors.BOLD + bcolors.WARNING +
                              " |  {:54} | {:10} | {:10} | {:10.3} |" +
                              bcolors.ENDC)

        table_line = " +--" + "-" * 93 + "-+"

        # DEBUG Ausgaben
        print("DEBUG: " + str(len(self._newSensorName_list)))
        print("DEBUG: " + str(len(self._newSensorValue_list)))
        print("DEBUG: " + str(len(self._newSensorMax_list)))
        print("Filename: " + self.__filename)

        print(table_line)
        print(table_form.format("NAME", "value", "max", "diff"))
        print(table_line)

        for i in range(len(self._newSensorName_list)):

            # Formatierte ausgabe anhand des wertes der differenz
            if self._newSensorDiff_list[i] >= 10:
                print(table_form.format(str(self._newSensorName_list[i]),
                                        self._newSensorValue_list[i],
                                        self._newSensorMax_list[i],
                                        self._newSensorDiff_list[i]))

            elif (self._newSensorDiff_list[i] > 0 and
                  self._newSensorDiff_list[i] < 10):
                print(table_form_gelb.format(str(self._newSensorName_list[i]),
                                             self._newSensorValue_list[i],
                                             self._newSensorMax_list[i],
                                             self._newSensorDiff_list[i]))
            else:
                print(table_form_red.format(str(self._newSensorName_list[i]),
                                            self._newSensorValue_list[i],
                                            self._newSensorMax_list[i],
                                            str(self._newSensorDiff_list[i])))

        print(table_line)




if __name__ == "__main__":
    """
    only the test funktion

    """

    print("")
    print("INFO: this file is a module not the main- file ")
    print("")

    x = 'te.xla'
    a = read_mcpsStatisticFile(x)
    a.print_sensorData()

    print(len(a._newSensorDiff_list))
