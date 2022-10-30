#task 1

# def test_jackpot(list):
#     for i in range(len(list)):
#         if(list[0]!=list[i]):
#             print("False")
#         else:print("True")
# list1=["SS","SS","SS","SS"]
# test_jackpot(list1)

# task 2

# def arrayValuesTypes(list):
#     b=[]
#     for i in range(len(list)):
#         b.append(type(list[i]))
#     print(b)
#
#
# list=[1,"asf",[],True,1.4]
# arrayValuesTypes(list)

# task 3

# class Country:
#     def __init__(self,name,population,area):
#         self.name=name
#         self.population=population
#         self.area=area
#     def is_big(self):
#         if(self.population>2500000 and self.area>3000000):
#             print("True")
#         else:print("False")
#
#     def compare_pd(self,nam):
#         if(self.population/self.area>nam.population/nam.area):
#             print(f'{self.name} has a larger population density than {nam.name}')
#         else:print(f'{nam.name} has a larger population density than {self.name}')
#
#
# australia=Country("Australia",23545500,7692024)
# andorra=Country("Andorra",76098,468)
# australia.is_big()
# andorra.is_big()
# andorra.compare_pd(australia)

# task 4

def sortByLength(list):
   print(sorted(list,key=len))
list=["Microsoft","Apple","Google"]
sortByLength(list)
