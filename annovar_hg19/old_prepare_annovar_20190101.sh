# bash run_annovar_full.sh VCF_FILE


input_file=${1}
output_file=${input_file}_ANNOVAR_FULL


table_annovar="perl /home/PublicData/annovar_src/annovar_20190101/table_annovar.pl"
convert2annovar="perl /home/PublicData/annovar_src/annovar_20190101/convert2annovar.pl"
annovar_db_folder="/home/PublicData/annovar_src/annovar_20190101/humandb"


db_gene="refGene
knownGene
ensGene"


db_filter="snp138
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
eigen"


protocol=""
operation=""
for p in $db_gene;do
    protocol="${protocol},${p}"
    operation="${operation},g"
done
for p in $db_filter;do
    protocol="${protocol},${p}"
    operation="${operation},f"
done
protocol="${protocol/,/}"
operation="${operation/,/}"


echo "
${table_annovar} \
        ${input_file} \
        ${annovar_db_folder} \
        --protocol ${protocol} \
        --operation ${operation}  \
        --outfile ${output_file} \
        --buildver hg19 \
        --remove \
        --otherinfo \
        --onetranscript \
        --nastring '.' \
        --vcfinput
" > run_annovar_20190101.${input_file}.sh
