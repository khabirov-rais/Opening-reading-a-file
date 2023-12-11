import os

def merge_files(file_list, output_file):
    file_contents = []

    for file_name in file_list:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            file_contents.append((file_name, len(lines), lines))

    file_contents.sort(key=lambda x: x[1])

    with open(output_file, 'w') as output:
        for file_name, num_lines, lines in file_contents:
            output.write(f'{file_name}\n{num_lines}\n')
            output.writelines(lines)
            output.write('\n')

def main():
    file_list = ['1.txt', '2.txt']
    output_file = 'result.txt'

    merge_files(file_list, output_file)
    print(f'Файлы объединены. Результат сохранен в {output_file}')

if __name__ == '__main__':
    main()
