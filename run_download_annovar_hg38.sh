
export PATH=/home/PublicData/annovar_src/annovar_20190101:$PATH
cd /home/PublicData/annovar_src/annovar_20190101
touch download_annovar_hg38.completed.log


[[ -z $( grep refGene download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar refGene humandb/ && echo refGene &>> download_annovar_hg38.completed.log
[[ -z $( grep knownGene download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar knownGene humandb/ && echo knownGene &>> download_annovar_hg38.completed.log
[[ -z $( grep ensGene download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar ensGene humandb/ && echo ensGene &>> download_annovar_hg38.completed.log
[[ -z $( grep dbnsfp35c download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar dbnsfp35c humandb/ && echo dbnsfp35c &>> download_annovar_hg38.completed.log
[[ -z $( grep dbscsnv11 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar dbscsnv11 humandb/ && echo dbscsnv11 &>> download_annovar_hg38.completed.log
[[ -z $( grep intervar_20180118 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar intervar_20180118 humandb/ && echo intervar_20180118 &>> download_annovar_hg38.completed.log
[[ -z $( grep cosmic70 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar cosmic70 humandb/ && echo cosmic70 &>> download_annovar_hg38.completed.log
[[ -z $( grep esp6500siv2_ea download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar esp6500siv2_ea humandb/ && echo esp6500siv2_ea &>> download_annovar_hg38.completed.log
[[ -z $( grep esp6500siv2_aa download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar esp6500siv2_aa humandb/ && echo esp6500siv2_aa &>> download_annovar_hg38.completed.log
[[ -z $( grep esp6500siv2_all download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar esp6500siv2_all humandb/ && echo esp6500siv2_all &>> download_annovar_hg38.completed.log
[[ -z $( grep exac03 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar exac03 humandb/ && echo exac03 &>> download_annovar_hg38.completed.log
[[ -z $( grep exac03nontcga download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar exac03nontcga humandb/ && echo exac03nontcga &>> download_annovar_hg38.completed.log
[[ -z $( grep exac03nonpsych download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar exac03nonpsych humandb/ && echo exac03nonpsych &>> download_annovar_hg38.completed.log
[[ -z $( grep gene4denovo201907 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar gene4denovo201907 humandb/ && echo gene4denovo201907 &>> download_annovar_hg38.completed.log
[[ -z $( grep gnomad211_exome download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar gnomad211_exome humandb/ && echo gnomad211_exome &>> download_annovar_hg38.completed.log
[[ -z $( grep gnomad211_genome download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar gnomad211_genome humandb/ && echo gnomad211_genome &>> download_annovar_hg38.completed.log
[[ -z $( grep kaviar_20150923 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar kaviar_20150923 humandb/ && echo kaviar_20150923 &>> download_annovar_hg38.completed.log
[[ -z $( grep hrcr1 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar hrcr1 humandb/ && echo hrcr1 &>> download_annovar_hg38.completed.log
[[ -z $( grep abraom download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar abraom humandb/ && echo abraom &>> download_annovar_hg38.completed.log
[[ -z $( grep 1000g2015aug download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar 1000g2015aug humandb/ && echo 1000g2015aug &>> download_annovar_hg38.completed.log
[[ -z $( grep gme download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar gme humandb/ && echo gme &>> download_annovar_hg38.completed.log
[[ -z $( grep mcap download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar mcap humandb/ && echo mcap &>> download_annovar_hg38.completed.log
[[ -z $( grep revel download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar revel humandb/ && echo revel &>> download_annovar_hg38.completed.log
[[ -z $( grep avsnp150 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar avsnp150 humandb/ && echo avsnp150 &>> download_annovar_hg38.completed.log
[[ -z $( grep nci60 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar nci60 humandb/ && echo nci60 &>> download_annovar_hg38.completed.log
[[ -z $( grep clinvar_20200316 download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar clinvar_20200316 humandb/ && echo clinvar_20200316 &>> download_annovar_hg38.completed.log
[[ -z $( grep regsnpintron download_annovar_hg38.completed.log ) ]] && annotate_variation.pl -buildver hg38 -downdb -webfrom annovar regsnpintron humandb/ && echo regsnpintron &>> download_annovar_hg38.completed.log
