# -*- coding: utf-8 -*-
# TODO:
# author=QIUKU
# 

from enum import Enum, unique


class Test(object):
	# 单下划线开头的私有属性可以被外部直接访问
	_name = 'test'
	# 双下划线开头的私有属性不可以被直接访问，但是可以通过特殊形式访问
	__type = 'any'

	def __init__(self, socre, sex):
		self.score = socre
		self.sex = sex


@unique
class Gender(Enum):
	Male = 0
	Female = 1


class Student(object):
	def __init__(self, name, gender):
		self.name = name
		if isinstance(gender, int) and (gender == 1 or gender == 0):
			self.gender = Gender(gender)
		elif isinstance(gender, Gender):
			self.gender = gender
		else:
			raise ValueError("Wrong Gender")


def B():
	print("I'm B")


def A():
	B()
	print("I'm A")


if __name__ == '__main__':
	# 关于函数嵌套调用
	A()
	print("I'm main")
	t1 = Test(10, 0)
	# t1._name = 'Kike'
	t1.id = 2
	# 私有属性其实也可以被外部访问，但是请不要去访问它们
	print(t1._name)
	print(t1._Test__type)
	# 关于枚举类
	s1 = Student('Bart', 0)
	s2 = Student('Kely', Gender.Male)
	# s3 = Student('Cartaman', 2)
	# s4 = Student('Wendy', 'Male')
	if s1.gender == Gender.Male:
		print('测试通过!')
	else:
		print('测试失败!')