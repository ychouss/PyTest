import pytest
import yaml
from testedcode.calc import Calculator


@pytest.fixture(scope= 'class')
def get_calc():
    print('获取计算机实例')
    calc = Calculator()
    return calc

#为打开yaml文件的函数设置别名,获取yaml文件列表数据
with open('./calc.yaml') as f:
    data = yaml.safe_load(f)
    add_datas = data['add']['datas']
    add_datanames = data['add']['datanames']

    div_datas = data['div']['datas']
    div_datanames = data['div']['datanames']

    sub_datas = data['sub']['datas']
    sub_datanames = data['sub']['datanames']

    mul_datas = data['mul']['datas']
    mul_datanames = data['mul']['datanames']

#获取加法参数化数据
@pytest.fixture(params=add_datas,ids=add_datanames)
def get_add_datas(request):
    print('开始加法计算')
    data = request.param
    print(f'加法测试数据为{data}')
    yield data
    print('结束加法计算')

#获取除法参数化数据
@pytest.fixture(params=div_datas,ids=div_datanames)
def get_div_datas(request):
    print('开始除法计算')
    data = request.param
    print(f'除法测试数据为{data}')
    yield data
    print('结束除法计算')

#获取乘法参数化数据
@pytest.fixture(params=mul_datas,ids=mul_datanames)
def get_mul_datas(request):
    print('开始乘法计算')
    data = request.param
    print(f'乘法测试数据为{data}')
    yield data
    print('结束乘法计算')

#获取减法参数化数据
@pytest.fixture(params=sub_datas,ids=sub_datanames)
def get_sub_datas(request):
    print('开始减法计算')
    data = request.param
    print(f'减法测试数据为{data}')
    yield data
    print('结束减法计算')
