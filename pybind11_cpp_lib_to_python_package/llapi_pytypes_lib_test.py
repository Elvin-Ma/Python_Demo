import importlib
import llapi_pytypes

# llapi_pytypes = importlib.import_module("llapi_pytypes")

print(llapi_pytypes)

shape_matrix = llapi_pytypes.br_2d_matrix_shape()
shape_matrix.height = 10
shape_matrix.subusharp = 3

matrix_desc = llapi_pytypes.br_2d_matrix_desc()
matrix_desc.usharp_id = 4
matrix_desc.shape = shape_matrix

usharp_id = matrix_desc.usharp_id

print("usharp id is : ", usharp_id)

reduce = llapi_pytypes.br_template_type_e.REDUCE
print("reduce is : ", int(reduce))

"""
# c++ 中调用 包装后的llapi_pytypes, 并且替换掉原来的数据类型
if (!llapi_imported_) {
        py::exec(R"(
            import sys
            import importlib
            import br_generator.code_generator
            llapi_pytypes = importlib.import_module("llapi_pytypes")
            sys.modules["br_generator.code_generator.br_llapi_data_struct_def"] = llapi_pytypes
            sys.modules["br_generator.code_generator"].br_llapi_data_struct_def = llapi_pytypes
        )");
        llapi_ = py::module_::import("br_generator.code_generator.br_code_gen_low_level_interface");
        llapi_imported_ = true;
}
"""



