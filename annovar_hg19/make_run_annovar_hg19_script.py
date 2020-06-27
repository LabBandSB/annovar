import argparse
import os
import datetime

ANNOVAR_HOME = "/home/PublicData/annovar_src/annovar_2019Oct24/"

table_annovar = f"perl {ANNOVAR_HOME}/table_annovar.pl"
annovar_db_folder = f"{ANNOVAR_HOME}/humandb"

# edit if necessary
db_gene = [
    "refGene",
    "knownGene",
    "ensGene",
]

# edit if necessary
db_filter = [
    "snp138",
    "avsnp138",
    "avsnp150",
    "ALL.sites.2015_08",
    "AFR.sites.2015_08",
    "AMR.sites.2015_08",
    "SAS.sites.2015_08",
    "EUR.sites.2015_08",
    "EAS.sites.2015_08",
    "esp6500siv2_ea",
    "esp6500siv2_all",
    "esp6500siv2_aa",
    "popfreq_all_20150413",
    "abraom",
    "hrcr1",
    "kaviar_20150923",
    "cg69",
    "dbnsfp35a",
    "dbscsnv11",
    "kgXref",
    "exac03nonpsych",
    "exac03nontcga",
    "gnomad_exome",
    "gnomad_genome",
    "gme",
    "mcap",
    "revel",
    "nci60",
    "icgc21",
    "cosmic68",
    "cosmic70",
    "clinvar_20180603",
    "mitimpact24",
    "regsnpintron",
    "gerp++elem",
    "gerp++gt2",
    "cadd13",
    "fathmm",
    "gwava",
    "eigen",
]

# to load db from ANNOVAR_HOME/humabdb instead of using default list
if True:
    from .get_annovar_db_from_humandb_dir import make_db_gene, make_db_filter

    db_gene = make_db_gene()
    db_filter = make_db_filter()

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
    now = datetime.datetime.now().strftime("%y%m%d_%H%M")
    # option 1 to save at working dir
    cmd_file = at_working_dir = input_file_prefix + '.RUN_ANNOVAR_hg19_' + now + '_.sh'
    with open(cmd_file, "w") as f:
        f.write(cmd)
    # option 2 to save at current dir
    cmd_file = at_current_dir = 'run_annovar_hg19_' + now + '_.sh'
    with open(cmd_file, "w") as f:
        f.write(cmd)
    #
    print(f"# bash {at_working_dir}")
    print(f"# nohup bash {at_working_dir} &")
    print(f"# bash {at_current_dir}")
    print(f"# nohup bash {at_current_dir} &")


if __name__ == '__main__':
    main()
