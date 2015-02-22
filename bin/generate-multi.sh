#!/usr/bin/env bash

size=$1
threshold=$2
number=$3
stem=$4
for i in $(seq -w $number)
do
    python bin/generate-data.py $size $threshold > $stem-$i.csv
done
