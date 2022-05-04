# 通过c++ 库来安装python包的步骤：
1.用PYBIND11_MODULE(llapi_pytypes, m) 将cpp 文件bind成python格式；
2.将llapi_pytypes 用pybind11 编译为动态库文件；
3.编写setup.py 将动态库文件*.so安装为 python的包；

# *.so 导出的python 包的使用
1. 在python中使用：直接 import llapi_pytypes 后使用;
2. 在c++ 中使用：用*.so生成的包替换掉 python原来的包
- llapi_pytypes = importlib.import_module("llapi_pytypes")
- sys.modules["br_generator.code_generator.br_llapi_data_struct_def"] = llapi_pytypes
3. 在c++ 中直接用 c++ 原数据类型传入python 接口中即可
