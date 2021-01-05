# -*- coding:utf-8 -*-
# @Time     :2021/1/4 3:01 下午
# @Author   :yun bosheng
# @File     :conftest.py
import pytest
import yaml
import os

from code.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + "/calc_data.yml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    print(datas)
    # 获取文件中key为datas的数据
    add_datas = datas["datas"]["add"]
    add_ids = datas["myids"]

    sub_datas = datas["datas"]["sub"]
    mul_datas = datas["datas"]["mul"]
    div_datas = datas["datas"]["div"]


@pytest.fixture(params=add_datas, ids=add_ids, scope="module")
def get_datas_add(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=sub_datas, ids=add_ids, scope="module")
def get_datas_sub(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=mul_datas, ids=add_ids, scope="module")
def get_datas_mul(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas, ids=add_ids, scope="module")
def get_datas_div(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc