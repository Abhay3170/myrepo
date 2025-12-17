# n=int(input())
# d={l[0]:tuple(map(int,l[1:])) for l in (input().split() for _ in range(n))}
# result={name:sum(value)/len(value) for name,value in d.items()}
# c=round(sum(result.values())/len(result),2)
# [print(f"{name}: {avg}") for name,avg in result.items() if avg>=c]

# def count(s):
#     result={}
#     for i in s.strip().split():
#         first=i[0]
#         if first not in result:
#             result[first]=[]
#         result[first].append(i)
#     return result
# s="cat car dog deer apple"
# print(count(s))

# def salary(s):
#     result={i:(j+(j*0.1) if j<50000 else j+(j*0.05)) for i,j in s.items()}
#     return result
# s={"emp1":40000,"emp2":60000,"emp3":50000}
# print(salary(s))
