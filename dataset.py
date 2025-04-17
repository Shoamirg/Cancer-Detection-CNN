import pydicom
from PIL import Image
import os

def convert_dicom_to_png(dicom_path, output_path):
    dicom_data = pydicom.dcmread(dicom_path)
    image_array = dicom_data.pixel_array
    image = Image.fromarray(image_array)
    image.save(output_path)

input_directory = 'dataset/dicom_images'
output_directory = 'dataset/converted_images'

os.makedirs(output_directory, exist_ok=True)

for dicom_file in os.listdir(input_directory):
    dicom_path = os.path.join(input_directory, dicom_file)
    if dicom_file.endswith('.dcm'):
        output_path = os.path.join(output_directory, dicom_file.replace('.dcm', '.png'))
        convert_dicom_to_png(dicom_path, output_path)