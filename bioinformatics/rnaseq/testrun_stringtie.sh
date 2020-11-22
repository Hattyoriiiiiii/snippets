#!/usr/bin/bash

SEQLIBS=("test" "test_f" "test_r")
STRAND=(rf fr)

for seqlib in ${SEQLIBS[@]}
do
    for strand in ${STRAND[@]}
        do
            stringtie -p 8 --${strand} ../3_mapping/${seqlib}.sorted.bam -G ~/ref/Refseq_mm10.gtf -o ../4_gtf/${seqlib}_${strand}.gtf
        done
done