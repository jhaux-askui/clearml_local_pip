from clearml import Task
import pprint

pp = pprint.PrettyPrinter(indent=4)

import my_package as mp

pp.pprint(mp.__dict__)
print(mp)

from my_package.my_code import MyClass
from my_package.sub_package.my_sub_code import MySubClass

T = Task.init('test_pipelines/latenight_clearml_testing', 'pls_work_tiny')
T.execute_remotely('single-gpu-2080ti')



mc = MyClass()

if mc.awesome:
    print('yay')
else:
    print('nay')

msc = MySubClass()

if msc.awesome:
    print('yay')
else:
    print('nay')
