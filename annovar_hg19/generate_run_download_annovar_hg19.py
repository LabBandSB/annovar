ANNOVAR_HOME = "/home/PublicData/annovar_src/annovar_2019Oct24/"

# order from https://doc-openbio.readthedocs.io/projects/annovar/en/latest/user-guide/download/
db_gene = [
    "refGene",
    "knownGene",
    "ensGene",
]
db_filter = [
    "avsift",
    "ljb26_all",
    "dbnsfp35c",
    "dbscsnv11",
    "intervar_20180118",
    "cg69",
    "cosmic68",
    "cosmic70",
    "cosmic80",
    "esp6500siv2_ea",
    "esp6500siv2_aa",
    "esp6500siv2_all",
    "exac03nonpsych",
    "exac03nontcga",
    "gene4denovo201907",
    "gnomad_exome",
    "gnomad_genome",
    "gnomad211_exome",
    "gnomad211_genome"
    "gnomad30_genome",
    "kaviar_20150923",
    "hrcr1",
    "abraom",
    "1000g2015aug",
    "gme",
    "mcap",
    "mcap13",
    "revel",
    "snp138",
    "avsnp138",
    "avsnp150",
    "nci60",
    "icgc21",
    "clinvar_20180603",
    "clinvar_20200316",
    "popfreq_all_20150413",
    "mitimpact24",
    "regsnpintron",
    "gerp++elem",
    "gerp++gt2",
    "cadd13",
    "fathmm",
    "gwava",
    "eigen",
]
db_list = db_gene + db_filter

log_file = "download_annovar_hg19.completed.log"
cmd_file = "run_download_annovar_hg19.sh"
with open(cmd_file, "w") as f:
    new_line = f"""
    export PATH={ANNOVAR_HOME}:$PATH
    cd {ANNOVAR_HOME}
    touch {log_file}
    \n
    """
    f.write(new_line)
    for db in db_list:
        check_db_in_log = f"""[[ -z $( grep {db} {log_file} ) ]]"""
        download_db = f"""annotate_variation.pl -buildver hg19 -downdb -webfrom annovar {db} humandb/"""
        add_db_to_log = f"""echo {db} &>> {log_file}"""
        new_line = f"""{check_db_in_log} && {download_db} && {add_db_to_log}\n"""
        f.write(new_line)

print(f"# bash {cmd_file}")
