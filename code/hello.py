#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《大数据与人工智能》课程 - 环境验证脚本

运行方式：
    python code/hello.py
"""

import sys


def main():
    print("=" * 46)
    print("  大数据与人工智能 - 环境验证")
    print("=" * 46)
    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"解释器路径: {sys.executable}")
    print()
    print("✅ 环境搭建成功，可以开始课程学习啦！")
    print("=" * 46)


if __name__ == "__main__":
    main()
