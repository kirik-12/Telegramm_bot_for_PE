# import requests
# from bs4 import BeautifulSoup as BS
# import fake_useragent


# url =  'https://drive.google.com/drive/folders/1g7N4A3jtxlkM_0GAQNGZcjp5OVZPA_vN?usp=share_link'
# user_agent = fake_useragent.UserAgent().random
# headers ={
#     'User-Agent': user_agent
# }
# response = requests.get(url)   
  
# html = BS(response.content,'html.parser')

# link = html.select('div[jscontroller="zgISHf"]')
# print(link[2])
# print(link[25])

# stringer = '/view?usp=share_link'
# # link = html.find('class="l-u-Ab-zb l-u-Ab-ul"')




# dict ={ 
# 1: 29,
# 2: 45,
# 3: 56,
# 4: 19,
# 5: 59,
# 6: 11,
# 7: 21,
# 8: 41,
# 9: 44,
# 10 : 16,
# 11 : 33,
# 12 : 4,
# 13 : 6,
# 14 : 48,
# 15 : 14,
# 16 : 8,
# 17 : 31,
# 18 : 25,
# 19 : 2,
# 20 : 53,
# 21 : 28,
# 22 : 46,
# 23 : 58,
# 24 : 54,
# 25 : 15,
# 26 : 55,
# 27 : 23,
# 28 : 43,
# 29 : 24,
# 30 : 1,
# 31 : 27,
# 32 : 9,
# 33 : 26,
# 34 : 50,
# 35 : 7,
# 36 : 47,
# 37 : 12,
# 38 : 40,
# 39 : 18,
# 40 : 5,
# 41 : 36,
# 42 : 38,
# }

dict = {
    43 : 13,
    44 : 34,
    45 : 49,
    46 : 52,
    47 : 60,
    48 : 35,
    49 : 17,
    50 : 42,
    51 : 10,
    52 : 20,
    53 : 3,
    54 : 30,
    55 : 39,
    56 : 51,
    57 : 22,
    58 : 57,
    59 : 37,
    60 : 32,
}

with open("hello.py", 'w') as file:
    for i in range(43,61):
        file.write(f'photo_{i}, ')
    file.write('\n')
    
