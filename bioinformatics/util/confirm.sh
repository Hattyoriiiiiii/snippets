#!/bin/bash

FQ1=$1
FQ2=$2

result_dir='result_fastqc'
if [ ! -d ${result_dir} ]; then
    mkdir ${result_dir}
fi

for FQ in ${FQ1} ${FQ2}
do
    fastqc 00outdir result_fastqc ${FQ} \
    >> ${result_dir}/fastqc_logs.txt 2>&1
done


result_FQ1="${FQ1%.*}"_fastqc.html
result_FQ2="${FQ2%.*}"_fastqc.html

reads_num_FQ1=`grep 'Total Sequences' ${result_dir}/${result_FQ1}`
reads_num_FQ2=