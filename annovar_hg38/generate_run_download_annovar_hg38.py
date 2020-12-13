ANNOVAR_HOME = '/home/PublicData/annovar_src/annovar_2019Oct24'

db_gene_file = '../annovar_db_gene_list.txt'
db_gene = [i.strip() for i in open(db_gene_file) if i.strip()]

db_filter_file = '../annovar_db_filter_list.txt'
db_filter = [i.strip() for i in open(db_filter_file) if i.strip()]

db_list = db_gene + db_filter

log_file = 'download_annovar_hg38.completed.log'
cmd_file = 'run_download_annovar_hg38.sh'
with open(cmd_file, 'w') as f:
    new_line = f'''
    export PATH={ANNOVAR_HOME}:$PATH
    cd {ANNOVAR_HOME}
    touch {log_file}
    \n
    '''
    f.write(new_line)
    for db in db_list:
        check_db_in_log = f'''[[ -z $( grep {db} {log_file} ) ]]'''
        download_db = f'''annotate_variation.pl -buildver hg38 -downdb -webfrom annovar {db} humandb/'''
        add_db_to_log = f'''echo {db} &>> {log_file}'''
        new_line = f'''{check_db_in_log} && {download_db} && {add_db_to_log}\n'''
        f.write(new_line)

    # for some reason this should be downloaded manually
    new_line = f'''wget -O humandb/hg38_kgXref.txt.gz http://disq.us/url?url=http%3A%2F%2Fhgdownload.cse.ucsc.edu%2FgoldenPath%2Fhg38%2Fdatabase%2FkgXref.txt.gz%3AJOOPG7r3TBmXFDXTMT97B9XvO34&cuid=3494157\n'''
    new_line += f'''gzip -d humandb/hg38_kgXref.txt.gz'''
    f.write(new_line)

print(f'# bash {cmd_file}')
