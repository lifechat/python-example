# from __future__ import print_function  在当前python2环境下超前使用python3 特性

import argparse  # 此模块是 Python 标准库中推荐的命令行解析模块。
import subprocess
import sys
import os
import tempfile
import uuid


def main():
    parser = argparse.ArgumentParser() # 获取命令行参数
    parser.add_argument('--descriptor_set_out',default=None);
    parser.add_argument('--dependency_out',default=None);
    parser.add_argument('protoc');
    args,remaining = parser.parse_known_args()

    if args.dependency_out and args.descriptor_set_out:
        tmp_path = os.path.join(tempfile.gettempdir(),str(uuid.uuid4()));
        # 自定义命令行指令
        custom = [
            '--descriptor_set_out',
            args.descriptor_set_out,
            '--dependency_out',
            tmp_path
        ]

        try:
            cmd = [args.protoc] + custom + remaining
            subprocess.check_call(cmd) # 子进程进行管理
            with open(tmp_path,'rb')
        finally:
            # 根据指令处理相关文件
            with open()
    print('命令行窗口');



if __name__ == "__main__" :
    sys.exit(main())
