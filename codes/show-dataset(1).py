import numpy as np
import sys

def display_npz(file_path):
    try:
        with np.load(file_path,allow_pickle=True) as data:
            print(f"文件 '{file_path}' 包含以下数组：")
            for key in data.files:
                array = data[key]
                print("\n" + "=" * 50)
                print(f"数组名称: {key}")
                print(f"形状: {array.shape}")
                print(f"数据类型: {array.dtype}")
                print("\n数据示例:")
                print(array)
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

if __name__ == "__main__":
    display_npz(r"D:\BYSJ_final\datasets\NAB-known-anomaly\wind_power.npz")