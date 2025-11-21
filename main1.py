# # a =  iter(range(5))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # try:
# #     print(next(a))
# # except:
# #         print("Error")
# #
# class Counter:
#     def __init__(self):
#         self.a=0
#
#     def __iter__(self):
#         self.a=0
#         return self
#
#     def __next__(self):
#         self.a+=2*2
#         return self.a
#
# c = iter(Counter())
#
# for i in range(20):
#     print(next(c))
# def gen(number):
#     b = number
#     i=0
#     while True:
#         i+=1
#         b+=1
#         yield b+1
# g=gen(5)
#
# print(next(g))
# print(next(g))
# print(next(g))
#
# def dec(f1):
#     def f2():
#         result = f1()
#         return f"Result: {result}"
#
#     return f2
#
# @dec
# def test():
#     return "Test"
#
# print(test())
class Car:
    def __init__(self, make, model, year):
        self.year=year
        self.make=make
        self.model=model
    def get_info(self):
        print(f"{self.year}, {self.make}, {self.model}")

Kasane_teto = Car("tesla", "Ultra nano 9x pro max superlight", 2077)
Kasane_teto.get_info()