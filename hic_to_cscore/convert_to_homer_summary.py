import sys

infile = sys.argv[1]  # chr1_100kb_raw.txt
outfile = sys.argv[2]  # chr1_100kb.summary

chrom = 'chr1'
bin_size = 100000

with open(infile) as fin, open(outfile, 'w') as fout:
    for line in fin:
        fields = line.strip().split()
        if len(fields) != 3:
            continue
        start1, start2, count = fields
        try:
            start1 = int(start1)
            start2 = int(start2)
            count = float(count)
        except:
            continue
        end1 = start1 + bin_size
        end2 = start2 + bin_size
        # 只保留count>0的记录
        if count > 0:
            fout.write(f"{chrom}\t{start1}\t{end1}\t{chrom}\t{start2}\t{end2}\t{int(count)}\n")
