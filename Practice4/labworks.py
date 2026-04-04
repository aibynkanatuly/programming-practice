#401
# def square_generetor(n):
#     for i in range(1 , n+1):
#         yield i*i

# n = int(input())
# for x in square_generetor(n):
#     print(x)

# 402
# n = int(input())
# for i in range(0, n+1, 2):
#     if i != 0:
#         print(",", end="")
#     print(i, end="")


# #403
# def asd(n):
#     for i in range(0 , n +1 ):
#         if i % 12 == 0 : 
#             yield i 

# n = int(input())

# for number in asd(n):
#     print(number, end=" ")


# #404
# def square_generetor(n , m):
#     for i in range(n , m+1):
#         yield i*i

# n , m = list(map(int , input().split()))
# for x in square_generetor( n , m):
#     print(x)

# #405
# def cout(n):
#     for i in range(n , -1 , -1 ):
#         yield i

# n = int(input())
# for x in cout(n):
#     print(x)

# 406
# def fibonnacci(n):
#     a = 0 
#     b = 1 
#     for i in range(n):
#         yield a
#         a , b = b , a + b 
# n = int(input())
# result = list(fibonnacci(n))

# print(",".join(map(str, result)))


# #408 
# def isprime(n):
#     if n < 2:
#         return False
#     for i in range(2 , int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def prime_generator(n):
#     for number in range(2, n + 1):
#         if isprime(number):
#             yield number


# n = int(input())
# print(*prime_generator(n))




#409
# def qwerty(n):
#     for i in range(n+1):
#         yield 2 ** i 

# n = int(input())
# print(*qwerty(n))


#410
# def aeuio(lst,n):
#     for _ in range(n ):
#         for j in lst:
#             yield j

# lst = input().split()
# n = int(input())

# print(*aeuio(lst , n ))


#411
# import json

# def merge(source, patch):
#    result = {}

#    for key, value in source.items():
#       if key in patch:
#          patch_value = patch[key]
#          if patch_value is None:
#             continue

#          if isinstance(value, dict) and isinstance(patch_value, dict):
#             result[key] = merge(value, patch_value)
#          else:
#             result[key] = patch_value
#       else:
#          result[key] = value

#    for key, value in patch.items():
#       if key not in source:
#          if value is not None:
#             result[key] = value

#    return result

# source = json.loads(input())
# patch = json.loads(input())

# print(json.dumps(merge(source, patch), sort_keys=True, separators=(',', ':')))

# {"user":{"name":"Ann","age":20},"active":true}
# {"user":{"age":21},"active":false}


#412
# import json

# def compare(obj1, obj2, path=""):
#    differences = []

#    keys = set(obj1.keys()) | set(obj2.keys())

#    for key in keys:
#       new_path = f"{path}.{key}" if path else key

#       in1 = key in obj1
#       in2 = key in obj2

#       if not in1:
#          differences.append(f"{new_path} : <missing> -> {json.dumps(obj2[key], separators=(',', ':'))}")
#       elif not in2:
#          differences.append(f"{new_path} : {json.dumps(obj1[key], separators=(',', ':'))} -> <missing>")
#       else:
#          val1 = obj1[key]
#          val2 = obj2[key]

#          if isinstance(val1, dict) and isinstance(val2, dict):
#             differences.extend(compare(val1, val2, new_path))
#          else:
#             if val1 != val2:
#                differences.append(
#                         f"{new_path} : "
#                         f"{json.dumps(val1, separators=(',', ':'))} -> "
#                         f"{json.dumps(val2, separators=(',', ':'))}"
#                     )

#    return differences

# obj1 = json.loads(input())
# obj2 = json.loads(input())

# diffs = compare(obj1, obj2)

# if not diffs:
#     print("No differences")
# else:
#     for line in sorted(diffs):
#         print(line)



#414
# from datetime import datetime

# line1 = datetime.strptime(input().strip().replace("UTC", ""), "%Y-%m-%d %z") 
# sec1 = line1.timestamp()
# line2 = datetime.strptime(input().strip().replace("UTC", ""), "%Y-%m-%d %z") 
# sec2 = line2.timestamp()
# print(int(abs(sec2 - sec1) / 86400))

# # date_part = line.split()[0] 
# # date_obj = datetime.strptime(date_part, "%Y-%m-%d").date()

# '''
# %a 	Weekday, short version - Wed 	
# %A 	Weekday, full version -	Wednesday 	
# %w 	Weekday as a number 0-6, 0 is Sunday -	3 	
# %d 	Day of month 01-31 	31 	
# %b 	Month name, short version - Dec 	
# %B 	Month name, full version -	December 	
# %m 	Month as a number 01-12 - 12 	
# %y 	Year, short version, without century -	18 	
# %Y 	Year, full version -	2018 	
# %H 	Hour 00-23 - 17 	
# %I 	Hour 00-12 - 05 	
# %p 	AM/PM - PM 	
# %M 	Minute 00-59 - 41 	
# %S 	Second 00-59 - 08 	
# %f 	Microsecond 000000-999999 - 548513 	
# %z 	UTC offset - +0100 	
# %Z 	Timezone - CST 	
# %j 	Day number of year 001-366 - 365 	
# %U 	Week number of year, Sunday as the first day of week, 00-53 - 52 	
# %W 	Week number of year, Monday as the first day of week, 00-53 - 52 	
# %c 	Local version of date and time -	Mon Dec 31 17:41:00 2018 	
# %C 	Century - 20 	
# %x 	Local version of date - 12/31/18 	
# %X 	Local version of time -	17:41:00 	
# %% 	A % character - % 	
# %G 	ISO 8601 year - 2018 	
# %u 	ISO 8601 weekday (1-7) - 1 	
# %V 	ISO 8601 weeknumber (01-53) - 01 
# '''



# import json
# import re

# def resolve_query(data, query):
#     current = data
    
   
#     tokens = re.findall(r'[a-zA-Z_]\w*|\[\d+\]', query)
    
#     for token in tokens:
#         if token.startswith('['): 
#             if not isinstance(current, list):
#                 return "NOT_FOUND"
#             index = int(token[1:-1])
#             if index < 0 or index >= len(current):
#                 return "NOT_FOUND"
#             current = current[index]
#         else: 
#             if not isinstance(current, dict):
#                 return "NOT_FOUND"
#             if token not in current:
#                 return "NOT_FOUND"
#             current = current[token]
    
#     return json.dumps(current, separators=(',', ':'))



# data = json.loads(input())
# q = int(input())

# for _ in range(q):
#     query = input().strip()
#     result = resolve_query(data, query)
#     print(result)