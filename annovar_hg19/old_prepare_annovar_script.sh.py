# erfactoring required

import argparse
import os


def main():
    sample_dict = parse_arguments_to_settings()
    cmd = get_cmd_annovar(sample_dict)


def parse_arguments_to_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", default=None, required=True)
    args = parser.parse_args()
    vcf = args.vcf
    sample = os.path.basename(vcf).split('.')[0]
    sample_path_prefix, _ = os.path.splitext(vcf)
    d = {
        "table_annovar": "perl /home/PublicData/annovar_src/annovar_20190101/table_annovar.pl",
        "convert2annovar": "perl /home/PublicData/annovar_src/annovar_20190101/convert2annovar.pl",
        "annovar_db_folder": "/home/PublicData/annovar_src/annovar_20190101/humandb",

        "vcf": vcf,
        "sample": sample,
        "sample_path_prefix": sample_path_prefix,
        "annovar_output": sample_path_prefix + ".FINAL.annovar",
        "annovar_txt": sample_path_prefix + ".FINAL.annovar.hg19_multianno.txt",
        "annovar_vcf": sample_path_prefix + ".FINAL.annovar.hg19_multianno.vcf",
        "annovar_header_txt": sample_path_prefix + ".FINAL.annovar.hg19_multianno.header.txt",
    }
    return d


def reduce_spaces_and_newlines(func):
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        s = s.replace("\n", " ")
        s = " ".join([i for i in s.split(" ") if i])
        return s

    return wrapper


@reduce_spaces_and_newlines
def get_cmd(d):
    d["token"] = "{sample_dir}/token.{sample}.{token_suffix}".format(**d)
    d["flags"] = " && ".join([" [ -f {:s} ] ".format(i) for i in d["files_list"]]) + \
                 " && [ ! -f {token} ] ".format(**d)
    cmd = """
        {flags} &&
        dt1=`date +%y%m%d_%H%M%S` && 
        echo $dt1 {token} &&
        {main_cmd} &&
        du {out_file} > {out_file}.$dt1.du &&
        md5sum {out_file} > {out_file}.$dt1.md5 &&
        dt2=`date +%y%m%d_%H%M%S` &&
        echo $dt1 $dt2 > {token} ||
        echo "TOKEN SKIPPED {token}"
        """.format(**d)
    return cmd


def get_cmd_annovar(d):
    d["files_list"] = [d["vcf"]]
    d["token_suffix"] = "annovar_vct_and_txt"
    d["out_file"] = d["annovar_txt"]
    d["main_cmd"] = bash_annovar(d)
    return get_cmd(d)


def bash_annovar(d):
    input_file = d["vcf"]
    output_file = d["annovar_output"]
    table_annovar = "perl /home/PublicData/annovar_src/annovar_20190101/table_annovar.pl"
    convert2annovar = "perl /home/PublicData/annovar_src/annovar_20190101/convert2annovar.pl"
    annovar_db_folder = "/home/PublicData/annovar_src/annovar_20190101/humandb"

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
        {input_file}
        {annovar_db_folder}
        --protocol {protocol}
        --operation {operation}
        --outfile {output_file}
        --buildver hg19
        --remove
        --otherinfo
        --onetranscript
        --nastring "."
        --vcfinput
    """
    return cmd


###############################################################################
def get_cmd_annovar_add_header(d):
    d["files_list"] = [d["annovar_txt"], d["annovar_vcf"], ]
    d["token_suffix"] = "annovar_add_header"
    d["out_file"] = d["annovar_header_txt"]
    d["main_cmd"] = bash_annovar_add_header(d)
    return get_cmd(d)


def bash_annovar_add_header(d):
    return """ python /home/PublicData/annovar_src/python/add_header.py -v {annovar_vcf} -t {annovar_txt} """.format(
        **d)


###############################################################################
def write_cmd_list_to_file(sample_settings, cmd_list):
    script_file = os.path.join(
        sample_settings["sample_dir"],
        sample_settings["sample"] + ".annovar.ss.sh",
    )
    with open(script_file, "w") as f:
        f.write("#!/bin/bash\n\n")
        for cmd in cmd_list:
            new_line = cmd + "\n\n"
            f.write(new_line)


###############################################################################
if __name__ == "__main__":
    main()
