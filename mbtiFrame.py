import time
import os
import platform
import matplotlib.pyplot as plt
from PIL import Image


def clear():
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


clear()
print("무료 성격 유형 검사 입니다.")

a = 0
b = 0
time.sleep(1)
clear()
print("문항이?")
print("1.을 입력")
print("2.을 입력")
q1 = int(input("번호를 입력해주세요:"))

if q1 == 1:
    a += 1
if q1 == 2:
    b += 1


clear()
print("2번째 문항이?")
print("1.을 입력")
print("2.을 입력")
q2 = int(input("번호를 입력해주세요:"))

if q2 == 1:
    a += 1
if q2 == 2:
    b += 1
clear()
print("3번째 문항이?")
print("1.을 입력")
print("2.을 입력")
q3 = int(input("번호를 입력해주세요:"))

if q3 == 1:
    a += 1
if q3 == 2:
    b += 1

clear()
print("4번째 문항이?")
print("1.을 입력")
print("2.을 입력")
q4 = int(input("번호를 입력해주세요:"))


if q4 == 1:
    a += 1
if q4 == 2:
    b += 1
clear()


print("결과는")
clear()
script_dir = os.path.dirname(os.path.abspath(__file__))


if a > b:
    print("q결과")
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
elif b > a:
    print("w결과")
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
else:
    print("ㄷ결과")
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
