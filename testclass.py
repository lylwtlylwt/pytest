from  Pytest import Pytest

s = Pytest('127.0.0.1','pymysql','Py_123','pymysql')
res = s.get_one("select version()")
print(res)




