# -*- coding:utf-8 -*-
# @Time     :2020/12/23 10:29 上午
# @Author   :yun bosheng
# @File     :test_calculator.py
import pytest
import yaml
from code.calculator import Calculator

def setup_module():
    print("\n用例开始执行")

def teardown_module():
    print("\n用例结束执行")


def read_file(path):
    with open(path) as f:
        datas = yaml.safe_load(f)
    return datas

class TestCalculator:
    def setup_class(self):
        self.calc = Calculator()
        print("\n类用例执行开始")

    def teardown_class(self):
        print("\n类用例执行结束")

    def setup(self):
        print("\n开始计算")

    def teardown(self):
        print("\n计算结束")

    @pytest.mark.parametrize("a, b, expect", read_file("../data/calc_parame.yml")['add'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", read_file("../data/calc_parame.yml")['sub'])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", read_file("../data/calc_parame.yml")['mul'])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", read_file("../data/calc_parame.yml")['div'])
    def test_div(self, a, b, expect):
        try:
            result = self.calc.div(a, b)
            assert result == expect
        except Exception as info:
            assert info.__eq__(ZeroDivisionError)

    @pytest.mark.parametrize("a, b", read_file("../data/calc_parame_fault.yml")['add'])
    def test_add_fault(self, a, b):
        try:
            result = self.calc.add(a, b)
            print(type(result))
            assert type(result) == int
        except Exception as info:
            assert info.__eq__(TypeError)

    @pytest.mark.parametrize("a, b", read_file("../data/calc_parame_fault.yml")['sub'])
    def test_sub_fault(self, a, b):
        try:
            self.calc.sub(a, b)
        except Exception as info:
            assert info.__eq__(TypeError)

    @pytest.mark.parametrize("a, b", read_file("../data/calc_parame_fault.yml")['mul'])
    def test_mul_fault(self, a, b):
        try:
            result = self.calc.mul(a, b)
        except Exception as info:
            assert info.__eq__(TypeError)

    @pytest.mark.parametrize("a, b", read_file("../data/calc_parame_fault.yml")['div'])
    def test_div_fault(self, a, b):
        try:
            result = self.calc.div(a, b)
        except Exception as info:
            assert info.__eq__(TypeError)