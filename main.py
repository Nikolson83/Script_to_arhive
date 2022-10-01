import os
import time
import zipfile


def total_folder_name(folders_list, name_list, archive_sum):

    data_time = time.localtime()
    data_time = str('{}_{}_{}'.format(data_time.tm_mday, data_time.tm_mon, data_time.tm_year))

    for i in range(archive_sum):
        try:
            os.chdir('C:\Python_and_Django\Test_del_files\Archive')
            zip_file = zipfile.ZipFile(name_list[i] + '_' + data_time + '.zip', 'w')
        except IndexError:
            zip_file = zipfile.ZipFile('None_name' + '_' + data_time + '.zip', 'w')

        for path, dirs, files in os.walk(folders_list[i]):
            for file in files:
                zip_file.write(os.path.join(path, file))  # join соединяет путь
        zip_file.close()


def open_files():
    archive_sum = 0

    open_folders = os.path.join('data_file', 'folders_archive.txt')  # Путь и имя файла
    with open(open_folders, 'r') as folders:  # Блокирования, разблокирования и автозакрытия файлов.
        folders_list = [line.rstrip() for line in folders
                        if line != '\n' and not line.startswith('#')]  # Считать строки и исключить перенос строки и символа rstrip() \
                                                                       # также удаляет любой пробел в конце строки и /n
    open_name = os.path.join('data_file', 'name_archive.txt')  # Путь и имя файла
    with open(open_name, 'r') as folders:  # Блокирования, разблокирования и автозакрытия файлов.
        name_list = [line.rstrip() for line in folders
                     if line != '\n' and not line.startswith('#')]  # Считать строки и исключить перенос строки и символа rstrip() \
                                                                    # также удаляет любой пробел в конце строки и /n
    for _ in folders_list:
        archive_sum += 1

    #  total_folder_name(folders_list, name_list, archive_sum)

    return archive_sum  # Возвращает значение и прекращает функцию


def main_archive():

    start_time = time.asctime()

    count_sum = open_files()

    finish_time = time.asctime()

    print()
    print('Start time:', str(start_time))
    print('Creation to archive:', str(count_sum), 'archive')
    print('Finished time:', str(finish_time))


if __name__ == '__main__':
    main_archive()
