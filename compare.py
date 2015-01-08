import time
class Compare:
    def compare_n2(self, n):
        minimum = None

        for i in n:
            is_min = True
            for j in n:
                if j < i:
                    is_min = False
            if is_min:
                minimum = i

        return minimum

    def compare(self, n):
        minimum = n[0]
        for i in n:
            if i <= minimum:
                minimum = i
        return minimum


array = [3,1,2,4,6,8,5,0,-1,21,-4,88,23,49,45,41,68,12,67,13,14,15,16,17,18,19,20,21,43,55,67,78,90,123,23,54,73,96,128,9871,2878,518,2348,248,12,8,35,98,3,87,354,9,54464,354,327,654,-64,-58,5448,5452,579,963,557]

time1 = time.time()
i = Compare.compare_n2(Compare(),array)
time2 = time.time()
print time2-time1
print i

time3 = time.time()
j = Compare.compare(Compare(),array)
time4 = time.time()
print time4-time3
print j

