"""Decompose, decompose blocksub, normalize Complete Genomics Controls."""
import sys, os, csv

sys.path.append('/home/evansj/me/projects/me/tool_dirs/')
from tools import *

caddFile = '/nas/is1/reference/human/annotations/CADD/whole_genome_SNVs_1.2.tsv.gz'
outFile = 'data/cadd_v12.vcf.gz'

rule mkVcf:
    input:  caddFile
    output: outFile
    shell:  'python cadd2vcf.py {input} | bgzip -c > {output}'

rule tabix:
    input:  '{sample}.vcf.gz'
    output: '{sample}.vcf.gz.tbi'
    shell:  'tabix -p vcf {input}'

rule all:
    input: outFile + '.tbi'
