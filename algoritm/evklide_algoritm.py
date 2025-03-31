"""Наименьшее общее кратное(NOK) И наибольший общий делитель(NOD)"""
def NOD(num1,num2):
  if num1 == 0 or num2 == 0:
    return num1+num2
  if num1>num2:
    return NOD(num1%num2,num2)
  return NOD(num1,num2%num1)
def NOK(num1,num2):
  return num1*num2/NOD(num1,num2)
