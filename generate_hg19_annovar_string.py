import argparse
import os


table_annovar = "perl /home/PublicData/annovar_src/annovar_20190101/table_annovar.pl"
convert2annovar = "perl /home/PublicData/annovar_src/annovar_20190101/convert2annovar.pl"
annovar_db_folder = "/home/PublicData/annovar_src/annovar_20190101/humandb"


def main():
    vcf = parse_arguments_to_settings()
    cmd = bash_annovar(vcf)
    print (cmd)


def parse_arguments_to_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", default=None, required=True)
    args = parser.parse_args()
    return args.vcf


def bash_annovar(input_vcf):
    output_vcf = generate_output_filename(input_vcf, ".FINAL.annovar" )

    db_gene = [
        "refGene",
        "knownGene",
        "ensGene",
    ]

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

    protocol = ",".join(db_gene + db_filter)
    operation = ",".join(["g"] * len(db_gene) + ["f"] * len(db_filter))

    cmd = f"""
        {table_annovar}
        {input_vcf}
        {annovar_db_folder}
        --protocol {protocol}
        --operation {operation}
        --outfile {output_vcf}
        --buildver hg19
        --remove
        --otherinfo
        --onetranscript
        --nastring "."
        --vcfinput
    """
    cmd = cmd.replace("\n", " \\\n").strip(" \\\n")
    return cmd

def generate_output_filename(in_file, suffix="out"):
    import os
    file_path, file_extension = os.path.splitext(in_file)
    return file_path + "." + suffix + file_extension


###############################################################################
if __name__ == "__main__":
    main()
