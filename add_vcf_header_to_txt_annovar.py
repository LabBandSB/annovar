import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--vcf_annovar', help='', required=True)
    parser.add_argument('-t', '--txt_annovar', help='', required=True)
    args = parser.parse_args()
    add_vcf_header_to_txt(args.vcf_annovar, args.txt_annovar)


def add_vcf_header_to_txt(vcf_anno, txt_anno):
    vcf_header = get_header_list(vcf_anno)
    txt_header = get_header_list(txt_anno)
    print_first_ten_columns_number(txt_anno)
    ''
    new_header = txt_header[:-len(vcf_header)] + vcf_header
    len_new_header = len(new_header)
    print(f'# new_len_header :{len_new_header}')
    print(f'# new_header :\n{" ".join(new_header)}')
    ''
    out_txt_anno = generate_output_filename(txt_anno, 'header')
    print(f'# generating new {out_txt_anno} file')
    with open(out_txt_anno, 'w') as f:
        f.write('\t'.join(new_header) + '\n')
        for line in open(txt_anno):
            if 'Otherinfo' in line:
                continue
            f.write(line)
    ''
    print(f'# first 10 columns of new {out_txt_anno} file')
    print_first_ten_columns_number(out_txt_anno)


def get_header_list(in_file):
    for line in open(in_file):
        if 'CHROM' in line or 'Otherinfo' in line:
            header_list = line.strip().split('\t')
            return header_list


def print_first_ten_columns_number(in_file):
    counter = 0
    for line in open(in_file):
        if line.startswith('##'):
            continue
        arr = line.strip('\n').split('\t')
        len_arr = len(arr)
        print(f'# len_arr: {len_arr}')
        if counter < 10:
            counter += 1
        else:
            break


def generate_output_filename(in_file, suffix='out'):
    file_path, file_extension = os.path.splitext(in_file)
    return f'{file_path}.{suffix}{file_extension}'


if __name__ == '__main__':
    main()
