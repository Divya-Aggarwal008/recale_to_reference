rule all:
    input:
        "output/{query}.bed.gz_rescaled_to_{ref}.hist.bed"

rule Unique_length:
    input:
        "data/{query}.bed.gz"
    output:
        "data/frag_len_{query}.txt"
    shell:
        "zless {input} | awk -F'\t' '{{print $4}}' > {output}"

rule frequency:
    input:
        "data/frag_len_{query}.txt"
    output:
        "data/frequency_{query}.txt"
    shell:
        "python scripts/frequency.py {input} {output}"

rule rescaling:
    input:
        freq = "data/frequency_{query}.txt",
        ref = "data/{ref}.hist"
    output:
        "output/rescaling_{query}_to_{ref}.txt"
    shell:
        "python scripts/rescaling.py {input.freq} {input.ref} {output}"

rule rescaled_bed:
    input:
        scaling = "output/rescaling_{query}_to_{ref}.txt",
        bed = "data/{query}.bed.gz"
    output:
        "output/{query}.bed.gz_rescaled_to_{ref}.hist.bed"
    shell:
        "python script/rescaled_bed.py {input.scaling} {input.bed} {output}"

