import onnx
from onnx import version_converter, helper

model_path = 'resnet18.onnx'
original_model = onnx.load(model_path)

#print('The model before conversion:\n{}'.format(original_model))
converted_model = version_converter.convert_version(original_model, 8)
#print('The model after conversion:\n{}'.format(converted_model))
