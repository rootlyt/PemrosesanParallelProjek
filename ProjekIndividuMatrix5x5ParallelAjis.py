import threading
import time

#array matriks dideklarasikan dan digambarkan sebagai berikut

                                    # 0  1  2  3  4
matrix_a = [[1, 2, 3, 2, 1],       #0|0, 0, 0, 0, 0| 
            [4, 5, 6, 5, 4],       #1|0, 0, 0, 0, 0|
            [7, 8, 9, 8, 9],       #2|0, 0, 0, 0, 0|
            [6, 5, 4, 5, 6],       #3|0, 0, 0, 0, 0| 
            [3, 2, 1, 2, 3]]       #4|0, 0, 0, 0, 0|

matrix_b = [[9, 8, 7, 8, 9], 
            [6, 5, 4, 5, 6], 
            [3, 2, 1, 5, 4], 
            [4, 5, 6, 5, 4], 
            [7, 8, 9, 2, 1]]

matrix_c = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]

#dekomposisi dan operasi untuk mendapatkan hasil dari matriks,
#menggunakan 1 thread per baris.

class Thread1(threading.Thread):        #0|0, 0, 0, 0, 0| 
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_c[0][0] = matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0] + matrix_a[0][2] * matrix_b[2][0] + matrix_a[0][3] * matrix_b[3][0] + matrix_a[0][4] * matrix_b[4][0]
        matrix_c[0][1] = matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1] + matrix_a[0][2] * matrix_b[2][1] + matrix_a[0][3] * matrix_b[3][1] + matrix_a[0][4] * matrix_b[4][1]
        matrix_c[0][2] = matrix_a[0][0] * matrix_b[0][2] + matrix_a[0][1] * matrix_b[1][2] + matrix_a[0][2] * matrix_b[2][2] + matrix_a[0][3] * matrix_b[3][2] + matrix_a[0][4] * matrix_b[4][2]
        matrix_c[0][3] = matrix_a[0][0] * matrix_b[0][3] + matrix_a[0][1] * matrix_b[1][3] + matrix_a[0][2] * matrix_b[2][3] + matrix_a[0][3] * matrix_b[3][3] + matrix_a[0][4] * matrix_b[4][3]
        matrix_c[0][4] = matrix_a[0][0] * matrix_b[0][4] + matrix_a[0][1] * matrix_b[1][4] + matrix_a[0][2] * matrix_b[2][4] + matrix_a[0][3] * matrix_b[3][4] + matrix_a[0][4] * matrix_b[4][4]

        print ("End " + self.name + "\n")


class Thread2(threading.Thread):        #1|0, 0, 0, 0, 0|
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_c[1][0] = matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0] + matrix_a[1][2] * matrix_b[2][0] + matrix_a[1][3] * matrix_b[3][0] + matrix_a[1][4] * matrix_b[4][0]
        matrix_c[1][1] = matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1] + matrix_a[1][2] * matrix_b[2][1] + matrix_a[1][3] * matrix_b[3][1] + matrix_a[1][4] * matrix_b[4][1]
        matrix_c[1][2] = matrix_a[1][0] * matrix_b[0][2] + matrix_a[1][1] * matrix_b[1][2] + matrix_a[1][2] * matrix_b[2][2] + matrix_a[1][3] * matrix_b[3][2] + matrix_a[1][4] * matrix_b[4][2]
        matrix_c[1][3] = matrix_a[1][0] * matrix_b[0][3] + matrix_a[1][1] * matrix_b[1][3] + matrix_a[1][2] * matrix_b[2][3] + matrix_a[1][3] * matrix_b[3][3] + matrix_a[1][4] * matrix_b[4][3]
        matrix_c[1][4] = matrix_a[1][0] * matrix_b[0][4] + matrix_a[1][1] * matrix_b[1][4] + matrix_a[1][2] * matrix_b[2][4] + matrix_a[1][3] * matrix_b[3][4] + matrix_a[1][4] * matrix_b[4][4]

        print ("End " + self.name + "\n")


class Thread3(threading.Thread):        #2|0, 0, 0, 0, 0|
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_c[2][0] = matrix_a[2][0] * matrix_b[0][0] + matrix_a[2][1] * matrix_b[1][0] + matrix_a[2][2] * matrix_b[2][0] + matrix_a[2][3] * matrix_b[3][0] + matrix_a[2][4] * matrix_b[4][0]
        matrix_c[2][1] = matrix_a[2][0] * matrix_b[0][1] + matrix_a[2][1] * matrix_b[1][1] + matrix_a[2][2] * matrix_b[2][1] + matrix_a[2][3] * matrix_b[3][1] + matrix_a[2][4] * matrix_b[4][1]
        matrix_c[2][2] = matrix_a[2][0] * matrix_b[0][2] + matrix_a[2][1] * matrix_b[1][2] + matrix_a[2][2] * matrix_b[2][2] + matrix_a[2][3] * matrix_b[3][2] + matrix_a[2][4] * matrix_b[4][2]
        matrix_c[2][3] = matrix_a[2][0] * matrix_b[0][3] + matrix_a[2][1] * matrix_b[1][3] + matrix_a[2][2] * matrix_b[2][3] + matrix_a[2][3] * matrix_b[3][3] + matrix_a[2][4] * matrix_b[4][3]
        matrix_c[2][4] = matrix_a[2][0] * matrix_b[0][4] + matrix_a[2][1] * matrix_b[1][4] + matrix_a[2][2] * matrix_b[2][4] + matrix_a[2][3] * matrix_b[3][4] + matrix_a[2][4] * matrix_b[4][4]

        print ("End " + self.name + "\n")

class Thread4(threading.Thread):        #3|0, 0, 0, 0, 0|
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_c[3][0] = matrix_a[3][0] * matrix_b[0][0] + matrix_a[3][1] * matrix_b[1][0] + matrix_a[3][2] * matrix_b[2][0] + matrix_a[3][3] * matrix_b[3][0] + matrix_a[3][4] * matrix_b[4][0]
        matrix_c[3][1] = matrix_a[3][0] * matrix_b[0][1] + matrix_a[3][1] * matrix_b[1][1] + matrix_a[3][2] * matrix_b[2][1] + matrix_a[3][3] * matrix_b[3][1] + matrix_a[3][4] * matrix_b[4][1]
        matrix_c[3][2] = matrix_a[3][0] * matrix_b[0][2] + matrix_a[3][1] * matrix_b[1][2] + matrix_a[3][2] * matrix_b[2][2] + matrix_a[3][3] * matrix_b[3][2] + matrix_a[3][4] * matrix_b[4][2]
        matrix_c[3][3] = matrix_a[3][0] * matrix_b[0][3] + matrix_a[3][1] * matrix_b[1][3] + matrix_a[3][2] * matrix_b[2][3] + matrix_a[3][3] * matrix_b[3][3] + matrix_a[3][4] * matrix_b[4][3]
        matrix_c[3][4] = matrix_a[3][0] * matrix_b[0][4] + matrix_a[3][1] * matrix_b[1][4] + matrix_a[3][2] * matrix_b[2][4] + matrix_a[3][3] * matrix_b[3][4] + matrix_a[3][4] * matrix_b[4][4]

        print ("End " + self.name + "\n")

class Thread5(threading.Thread):        #4|0, 0, 0, 0, 0|
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_c[4][0] = matrix_a[4][0] * matrix_b[0][0] + matrix_a[4][1] * matrix_b[1][0] + matrix_a[4][2] * matrix_b[2][0] + matrix_a[4][3] * matrix_b[3][0] + matrix_a[4][4] * matrix_b[4][0]
        matrix_c[4][1] = matrix_a[4][0] * matrix_b[0][1] + matrix_a[4][1] * matrix_b[1][1] + matrix_a[4][2] * matrix_b[2][1] + matrix_a[4][3] * matrix_b[3][1] + matrix_a[4][4] * matrix_b[4][1]
        matrix_c[4][2] = matrix_a[4][0] * matrix_b[0][2] + matrix_a[4][1] * matrix_b[1][2] + matrix_a[4][2] * matrix_b[2][2] + matrix_a[4][3] * matrix_b[3][2] + matrix_a[4][4] * matrix_b[4][2]
        matrix_c[4][3] = matrix_a[4][0] * matrix_b[0][3] + matrix_a[4][1] * matrix_b[1][3] + matrix_a[4][2] * matrix_b[2][3] + matrix_a[4][3] * matrix_b[3][3] + matrix_a[4][4] * matrix_b[4][3]
        matrix_c[4][4] = matrix_a[4][0] * matrix_b[0][4] + matrix_a[4][1] * matrix_b[1][4] + matrix_a[4][2] * matrix_b[2][4] + matrix_a[4][3] * matrix_b[3][4] + matrix_a[4][4] * matrix_b[4][4]

        print ("End " + self.name + "\n")

start = int(round(time.time_ns())) #start perhitungan waktu eksekusi program hingga selesai

thread1 = Thread1(1, "Thread 1")
thread2 = Thread2(2, "Thread 2")
thread3 = Thread3(3, "Thread 3")
thread4 = Thread4(4, "Thread 4")
thread5 = Thread5(5, "Thread 5")


#untuk hasil serial parallel silahkan comment atau uncomment salah satu dari dibawah ini

#//serial exec
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread4.start()
thread4.join()
thread5.start()
thread5.join()

# #//parallel exec
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()

print("Waktu Eksekusi: ", (int(round(time.time_ns())) - start)," nanosecond") #print hasil waktu eksekusi saat selesai


#for array in matrix_c:
#   print (matrix_c)

#print (matrix_c,"\n")

print(*matrix_c, sep='\n') #separator print hasil array