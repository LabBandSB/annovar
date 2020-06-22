import os

# variables block
ANNOVAR_HOME = "/home/PublicData/annovar_src/annovar_2019Oct24/"
HUMANDB_HOME = os.path.join(ANNOVAR_HOME, "humandb")

# scan block
db_list = [i[5:-4] for i in os.listdir(HUMANDB_HOME) if i.startswith("hg19_") and i.endswith(".txt")]

# reordering block
db_gene = """refGene
knownGene
ensGene"""
db_gene = [i.strip() for i in db_gene.split('\n')]

db_filter = """snp138
avsnp138
avsnp150
ALL.sites.2015_08
AFR.sites.2015_08
AMR.sites.2015_08
SAS.sites.2015_08
EUR.sites.2015_08
EAS.sites.2015_08
esp6500siv2_ea
esp6500siv2_all
esp6500siv2_aa
popfreq_all_20150413
abraom
hrcr1
kaviar_20150923
cg69
dbnsfp35a
dbscsnv11
kgXref
exac03nonpsych
exac03nontcga
gnomad_exome
gnomad_genome
gme
mcap
revel
nci60
icgc21
cosmic68
cosmic70
clinvar_20180603
mitimpact24
regsnpintron
gerp++elem
gerp++gt2
cadd13
fathmm
gwava
eigen"""
db_filter = [i.strip() for i in db_filter.split('\n')]

db_order = list()
# genes block
for db in db_gene:
    if db in db_list:
        db_order.append(db)
        db_list[db_list.index(db)] = ""
# filters block
for db in db_filter:
    if db in db_list:
        db_order.append(db)
        db_list[db_list.index(db)] = ""
# remainder block, recall last 3 elements are fathmm, gwava, eigen
for db in db_list:
    if db:
        db_order.append(db)

# print block
db_str = '"' + '\n'.join(db_order) + '"'
print (db_str)
