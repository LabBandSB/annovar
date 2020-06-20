import argparse
import os

table_annovar = "perl /home/PublicData/annovar_src/annovar_20190101/table_annovar.pl"
annovar_db_folder = "/home/PublicData/annovar_src/annovar_20190101/humandb"

db_gene = [
    "refGene",
    "knownGene",
    "ensGene",
]

db_filter = [
    "avsnp150",
    "ALL.sites.2015_08",
    "AFR.sites.2015_08",
    "SAS.sites.2015_08",
    "EUR.sites.2015_08",
    "EAS.sites.2015_08",
    "esp6500siv2_ea",
    "esp6500siv2_aa",
    "esp6500siv2_all",
    "dbnsfp35c",
    "dbscsnv11",
    "intervar_20180118",
    "cosmic70",
    "exac03",
    "exac03nontcga",
    "exac03nonpsych",
    "gene4denovo201907",
    "gnomad211_exome",
    "gnomad211_genome",
    "kaviar_20150923",
    "hrcr1",
    "abraom",
    "gme",
    "mcap",
    "revel",
    "nci60",
    "clinvar_20200316",
    "regsnpintron",
]

protocol = ",".join(db_gene + db_filter)
operation = ",".join(["g"] * len(db_gene) + ["f"] * len(db_filter))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", default=None, required=True)
    args = parser.parse_args()

    input_file = args.vcf
    input_file_prefix, _ = os.path.splitext(input_file)
    output_file = input_file_prefix + ".FINAL.annovar"

    cmd = f"""
        {table_annovar} \
        {input_file} \
        {annovar_db_folder} \
        --protocol {protocol} \
        --operation {operation}  \
        --outfile {output_file} \
        --buildver hg38 \
        --remove \
        --otherinfo \
        --onetranscript \
        --nastring '.' \
        --vcfinput
    """
    cmd_file = input_file_prefix + '.RUN_ANNOVAR_hg38.sh'
    with open (cmd_file, "w") as f:
        f.write(cmd)


if __name__ == '__main__':
    main()
