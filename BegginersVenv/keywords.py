# and  as  assert  break  class  continue  def  del  elif  else  except  False  finally  for  from  global  if
# import  in  is  lambda  None  nonlocal  not  or  pass  raise  return  True  try  while  with  yield

a = ['False', 'class', 'finally', 'is', 'return', 'None', 'continue', 'for', 'lambda', 'try', 'True', 'def',
     'from', 'nonlocal', 'while', 'and', 'del', 'global', 'not', 'with', 'as', 'elif', 'if', 'or', 'yield',
     'pass', 'else', 'import', 'assert', 'break', 'except', 'in', 'raise']

print(a)
print(sorted(a))
b = sorted(a, key=str.lower)
print(b)
