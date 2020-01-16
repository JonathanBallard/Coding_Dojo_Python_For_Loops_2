
import math



#Biggie Size
def BiggieSize(list):
    for i in range(0,len(list),1):
        if list[i] > 0:
            list[i] = "big"
    return list

myList = [1,-3,-4,3,0]
x = BiggieSize(myList)
print(x)

#Count Positives
def CountPositives(list):
    num = 0
    for i in range(len(list)):
        if list[i] > 0:
            num += 1
    list[len(list) - 1] = num
    return list

myList2 = [1,-3,-4,3,0]
x = CountPositives(myList2)
print(x)



#Sum Total
def SumTotal(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

myList3 = [1,4,6,8]
x = SumTotal(myList3)
print(x)


#Average
def Average(list):
    avg = 0
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    avg = sum / len(list)
    return avg

myList4 = [1,4,6,8]
x = Average(myList4)
print(x)


#Length
def Length(list):
    return len(list)

x = Length(myList4)
print(x)




#Minimum
def Minimum(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min


x = Minimum(myList4)
print(x)


#Maximum
def Maximum(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max


x = Maximum(myList4)
print(x)


#Ultimate Analysis
def UltimateAnalysis(list):
    myDict = {}
    sumTotal = SumTotal(list)
    min = Minimum(list)
    max = Maximum(list)
    avg = Average(list)
    leng = len(list)
    myDict = {'sumTotal': sumTotal,
        'minimum': min,
        'maximum': max,
        'average': avg,
        'length': leng
    }
    return myDict


x = UltimateAnalysis(myList4)
print(x)

#Reverse List
def ReverseList(list):
    ii = len(list) - 1
    temp = 0
    for i in range(math.floor(len(list) / 2)):
        temp = list[ii]
        list[ii] = list[i]
        list[i] = temp

        ii -= 1
    return list



x = ReverseList(myList4)
print(x)



