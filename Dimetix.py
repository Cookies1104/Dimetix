import csv
import matplotlib.pyplot as plt


class DiagramDimetix:
    """Построение диаграммы из файлов Dimetix в формате csv с разделителем ; и столбцами дата, время, расстояние"""

    def __init__(self, file_name):
        self.filename = file_name

    def conversion(self):
        """Редактирует csv файл полученный с Dimetix оставляя только значения расстояний"""
        with open(self.filename) as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
            storage = []
            x = 0
            for el in rows:
                n = rows[x]
                n = n[0]
                n = n[22:]
                storage.append(float(n))
                x += 1
            return storage

    def calculate(self, storage):
        """Расчёт полученных данных, создание и вывод диаграммы"""
        storage_y = []
        storage_x = []
        zero = round(float(storage[0]) / 10 ** (len(str(storage[0])) - 2), 2) * 10 ** (len(str(storage[0])) - 2)
        zero_y = round((sum(storage) / (len(storage) + 1) - zero) * 0.1, 1)
        sec = 0
        for el in storage:
            storage_y.append(round(((el - zero) * 0.1) - zero_y, 1))
            storage_x.append(round(sec))
            sec += 1 / 6

        new_storage_y = storage_y[::6]
        new_storage_x = storage_x[::6]

        plt.figure(dpi=128, figsize=(10, 6))
        plt.axes(facecolor="black")
        plt.plot(new_storage_x[:1000], new_storage_y[:1000], linewidth=1)
        plt.title(self.filename, fontsize=24)
        plt.xlabel('Время, с', fontsize=14)
        plt.ylabel('Отклононения, мм', fontsize=14)
        plt.scatter(new_storage_x, new_storage_y, cmap=plt.cm.Blues, s=10, edgecolors='none')
        plt.show()


print('Для начала работы с программой поместите файлы для построения диаграмм в одну директорию с приложением'
      ' .exe и измените расширение файла на .csv')

while True:
    try:
        filename = input('Введите название файла с расширением (Например - измерения 21.12.24.csv):')
        my_diagram = DiagramDimetix(filename)
        my_diagram.calculate(my_diagram.conversion())
    except FileNotFoundError:
        print('Такого файла не существует, повторите ввод')
    else:
        break
