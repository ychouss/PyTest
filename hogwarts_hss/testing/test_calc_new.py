import allure
import pytest


#计算器测试类
@allure.feature('测试计算器')
class Testcalc:

    # 加法测试方法
    @allure.story('测试加法')
    @pytest.mark.first
    def test_add(self, get_calc, get_add_datas):
        with allure.step('计算两数相加'):
            reslut = get_calc.add(get_add_datas[0], get_add_datas[1])
        #如果结果为float类型，只保留两位小数
        if isinstance(reslut, float):
            reslut = round(reslut, 2)
        #断言
        assert reslut == get_add_datas[2]


    #除法的测试方法
    @allure.story('测试除法')
    @pytest.mark.fourth
    def test_div(self,get_calc,get_div_datas):
        with allure.step('计算两数相除'):
            reslut = get_calc.div(get_div_datas[0],get_div_datas[1])
        assert reslut == get_div_datas[2]


    #减法的测试方法
    @allure.story('测试减法')
    @pytest.mark.second
    def test_sub(self,get_calc,get_sub_datas):
        with allure.step('计算两数相减'):
            reslut = get_calc.sub(get_sub_datas[0],get_sub_datas[1])
        assert reslut == get_sub_datas[2]


    #乘法的测试方法
    @allure.story('测试乘法')
    @pytest.mark.third
    def test_mul(self,get_calc,get_mul_datas):
        with allure.step('计算两数相乘'):
            reslut = get_calc.mul(get_mul_datas[0],get_mul_datas[1])
        assert reslut == get_mul_datas[2]