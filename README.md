# calculator

### calculator1

+ 计算器 加减乘除 测试用例
+ 使用参数化完成测试用例的自动生成
+ 在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
+ 测试用例中添加断言，验证结果
+ 了解setup(), teardown() , setup_class(), teardown_class()

### calculator2
+ 补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
+ 创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
+ 将 fixture 方法存放在 conftest.py ，设置 scope=module
+ 控制测试用例顺序按照【加-减-乘-除】这个顺序执行
+ 结合 allure 生成本地测试报告