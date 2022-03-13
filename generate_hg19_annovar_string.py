import argparse
import os

table_annovar = "perl /home/PublicData/annovar_src/annovar_20190101/table_annovar.pl"
convert2annovar = "perl /home/PublicData/annovar_src/annovar_20190101/convert2annovar.pl"
annovar_db_folder = "/home/PublicData/annovar_src/annovar_20190101/humandb"

token_start = """
# lock sample to prevent runnig 2 times
[ ! -f {alignment_dir}/token.{sample}.__annovar_start__ ] && \
touch {alignment_dir}/token.{sample}.__annovar_start__ \
|| exit 1

# remove final lock to indicate that the pipeline is not ended 
rm -f {alignment_dir}/token.{sample}.__annovar_finish__ 
dt1dt1=`date +%y%m%d_%H%M%S` 
"""

token_finish = """
dt2dt2=`date +%y%m%d_%H%M%S` && \
echo $dt1dt1 $dt2dt2 > {alignment_dir}/token.{sample}.__annovar_finish__ 
"""


def main():
    d = parse_arguments_to_settings()
    vcf = d["vcf"]
    if vcf:
        cmd = bash_annovar(vcf)
        print(cmd)
    else:
        script_dir = d['script_dir']
        generate_scripts_for_annovar(d)
        print(f"# cd {script_dir}")


def generate_scripts_for_annovar(d):
    vcf_dir = d['vcf_dir']
    vcf_suffix = d['vcf_suffix']
    script_dir = d['script_dir']
    for vcf in vcf_list_generator(vcf_dir, vcf_suffix):
        alignment_dir, sample_file = os.path.split(vcf)
        sample = sample_file.split(".")[0]
        sh_file = f"{script_dir}/{sample}.annovar_hg19.sh"
        with open(sh_file, "w") as f:
            new_line = token_start.format(alignment_dir=alignment_dir, sample=sample) + "\n"
            f.write(new_line)
            new_line = bash_annovar(vcf) + "\n"
            f.write(new_line)
            new_line = "echo DONE at `date +%y%m%d_%H%M%S` "
            f.write(new_line)
            new_line = token_finish.format(alignment_dir=alignment_dir, sample=sample) + "\n"
            f.write(new_line)


def get_files_generator(dirs_list, extension=""):
    for path in dirs_list:
        for data_file in os.listdir(path):
            if data_file:
                data_path = os.path.join(path, data_file)
                if os.path.isfile(data_path) and data_path.endswith(extension):
                    yield data_path
                elif os.path.isdir(data_path):
                    yield from get_files_generator([data_path], extension)


def vcf_list_generator(dir, suffix):
    yield from get_files_generator([dir], extension=suffix)


def parse_arguments_to_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", default=None, required=False)
    parser.add_argument("--vcf_dir", default=None, required=False)
    parser.add_argument("--vcf_suffix", default=".FINAL.vcf", required=False)
    parser.add_argument("--script_dir", default="./scripts", required=False)
    args = parser.parse_args()
    d = {
        "vcf": args.vcf,
        "vcf_dir": args.vcf_dir,
        "vcf_suffix": args.vcf_suffix,
        "script_dir": args.script_dir,
    }
    return d


def bash_annovar(input_vcf):
    file_path, file_extension = os.path.splitext(input_vcf)
    output_vcf = file_path + ".FINAL.annovar"

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
    cmd = "\n\n" + cmd.replace("\n", " \\\n").strip(" \\\n")
    return cmd


###############################################################################
if __name__ == "__main__":
    main()
