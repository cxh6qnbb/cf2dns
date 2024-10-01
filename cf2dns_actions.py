import os
import requests

def fetch_license():
    # 从环境变量获取密钥
    license_key = os.getenv('KEY')
    
    if not license_key:
        print("错误：未找到许可证密钥。")
        return
    
    url = f"https://api.hostmonit.com/get_license?license={license_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        print("许可证响应:", response.text)
    except requests.exceptions.RequestException as e:
        print("请求失败:", e)

if __name__ == "__main__":
    fetch_license()
