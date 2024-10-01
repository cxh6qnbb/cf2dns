#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def main():
    # 获取并输出KEY值
    key = os.environ.get("KEY", "未设置KEY")
    print("KEY内容:", key)

if __name__ == '__main__':
    main()
