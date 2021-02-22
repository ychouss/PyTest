import pytest
import yaml

from testedcode.calc import Calculator
#为打开yaml文件的函数设置别名,获取yaml文件列表数据
with open('./calc.yaml') as f:
    data = yaml.safe_load(f)
    add_datas = data['add']['datas']
    add_datanames = data['add']['datanames']

    div_datas = data['div']['datas']
    div_datanames = data['div']['datanames']

#定义一个函数级别的测试装置
def setup():
    print('计算开始')

def teardown():
    print('计算结束')
#定义一个加法测试函数,为函数添加参数化装饰器
@pytest.mark.parametrize("a,b,c",add_datas,ids=add_datanames)
def test_add(a,b,c):
    calc = Calculator()
    result = calc.add(a,b)
    if isinstance(result,float):
        result = round(result,2)
    #相加之后断言
    assert result == c

#定义一个测试类
class Testcal:
    #定义一个类级别的测试装置
    def setup_class(self):
        print('计算开始')
        #实例化测试类
        self.calc1 = Calculator()

    def teardown_class(self):
        print('计算结束')

    #定义一个除法的测试方法，通过装饰器参数化
    @pytest.mark.parametrize("a,b,c",div_datas,ids=div_datanames)
    def test_div(self,a,b,c):
        reslut1 = self.calc1.div(a,b)
        assert reslut1 == c