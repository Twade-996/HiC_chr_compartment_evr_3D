import sys
# 假设格式：chr1 start1 end1 chr2 start2 end2 count
# 取start1和start2作为位置，strand都用 "+"
# read name用行号i作为唯一标识
def main():
    """
    主函数，用于处理命令行参数并执行文件格式化。
    """
    # 检查命令行参数数量是否正确
    if len(sys.argv) != 3:
        # sys.argv[0] 是脚本自己的名字
        print(f"用法: python {sys.argv[0]} <输入文件名> <输出文件名>")
        sys.exit(1) # 参数不正确，退出程序

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        with open(input_path, 'r') as fin, open(output_path, 'w') as fout:
            for i, line in enumerate(fin):
                fields = line.strip().split()
                if len(fields) >= 5:
                    read_name = f"read{i}"
                    chr1 = fields[0]
                    pos1 = fields[1]
                    strand1 = '+'
                    chr2 = fields[3]
                    pos2 = fields[4]
                    strand2 = '+'
                    fout.write(f"{read_name}\t{chr1}\t{pos1}\t{strand1}\t{chr2}\t{pos2}\t{strand2}\n")
        
        print(f"文件 '{input_path}' 已成功处理并保存为 '{output_path}'")

    except FileNotFoundError:
        print(f"错误：找不到输入文件 '{input_path}'")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")

if __name__ == "__main__":
    main()
