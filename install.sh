#!/bin/bash
# 关于为什么写英文提醒 —— 怕使用者的终端无法显示中文
# 关于为什么写中文注释 —— 因为我写的英文比较蹩脚，还是写中文方便
echo "Checking pip3 is exists..."

type supervisord
if [ $? -eq 0 ]; then
    echo "Installing finished."
    exit 0
fi

# 检查内容
type pip3
if [ $? -ne 0 ]; then
    echo "Looks like you don't have pip3, please install pip. If your pip is same with pip3, please change line2 'pip3' to 'pip'.\n If you are using virtual environment, please enable your virtual environment first."
    exit -1
fi

# 判断是否安装supervisor成功 
echo "Installing supervisor..."
pip3 install supervisor
if [ $? -ne 0 ]; then
    echo "Install supervisor failed. Install break."
    exit -1
fi
