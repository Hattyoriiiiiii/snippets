#!/usr/bin/bash

SEQLIBS=("test" "test_f" "test_r")

for seqlib in ${SEQLIBS[@]}
do
            stringtie -p 8 ../3_mapping/${seqlib}.sorted.bam -G ~/ref/Refseq_mm10.gtf -o ../4_gtf/${seqlib}_no_option.gtf
done