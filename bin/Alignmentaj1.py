from Bio.SeqIO import parse
from Bio.Seq import Seq
print("Please install the BioPyton package first.")
language = input('Plese choose language which you will work:\n'
                 'English or Russian: ')
if language == 'English':
    h = input('If you want to know about Aligmentaj enter: "help",\n'
            'If you want to start analyses enter: "start",\n'
            'If you want to stop analyses enter: "stop",\n'
            'If you want to know about author enter: "author",\n'
            'Your choose: ')
    if h == 'help':
        print(' Our Alignmentaj program works very well and even very fast.\n '
            'Our program Alignmentaj works with local alignment.\n '
            'And Alignmentaj receives two files in a fasta format as an input,\n '
            'and as an output, you firstly receive data about the\n '
            'proteins that you gave to the program, that is, the name of\n '
            'the protein, the ID number of the protein, and the amino acid\n '
            'sequences of the protein. And also get the output of those\n '
            'pentapeptides that the program found and also get the number\n '
            'of lines that start where these pentapeptides are in proteins.\n'
            'Our program is available in English and Russian languages.')
    if h == 'start':
        a = input('Specify the path to the fasta file 1: ')
        b = input('Specify the path to the fasta file 2: ')
        j = int(input('Write the number of proposed amino acid sequences: '))
        if j < 4 or j == 4:
            print('The sequence starts from pentapeptides only!')
        if j > 5 or j == 5:
            file = open(a)
            records = parse(file, 'fasta')
            if records == parse(file, 'fasta'):
                print('file not as fasta format!')
            for record in records:
                record.seq

            file1 = open(b)
            humans = parse(file1, 'fasta')
            for human in humans:
                human.seq

            a = record.seq
            b = human.seq
            c = len(human.seq)
            d = len(record.seq)
            for i in range(c):
                if len(b[i:i + j]) < 4:
                    break
                if b[i:i+j] in a:
                    name_protein1 = record.name
                    print('NAME and ID number protein from first file: ',
                        name_protein1)
                    seq_protein1 = record.seq
                    print('SEQUENCES from first protein: ', seq_protein1)
                    print('PEPTID from first protein: ', b[i:i+j])
                    kar = b[i:i+j]
                    print('The number of the beginning of the peptide in the first protein: ',
                        a.find(kar) + 1)

            for dal in range(d):
                if len(a[dal:dal+j]) < 4:
                    break
                if a[dal:dal+j] in b:
                    name_protein2 = human.name
                    print('NAME and ID number protein from second file: ', name_protein2)
                    seq_protein2 = human.seq
                    print('SEQUENCES from second protein: ', seq_protein2)
                    print('PEPTID from second protein: ', a[dal:dal+j])
                    kar2 = a[dal:dal+j]
                    print('The number of the beginning of the peptide in the second protein: ',
                        b.find(kar2) + 1)

            print('Results ready!')
            print('Thank you for using Aligmentaj!')

    if h == 'stop':
        print('Thank you for using Aligmentaj!')

    if h == 'author':
        print('Author data:\n'
            'Name: Muslimbek,\n'
            'Midle name: Ghulomovich,\n'
            'Surname: Normatov,\n'
            'Contact: muslimbek_normatov@mail.ru')

if language == 'Russian':
    h = input('Если вы хотите узнать об Alignmentaj, введите: "помощь",\n'
              'Если вы хотите начать анализ, введите: "начать",\n'
              'Если вы хотите остановить анализ, введите: "стоп",\n'
              'Если вы хотите узнать об авторе, введите: "автор",\n'
              'Ваш выбор: ')
    if h == 'помощь':
        print(' Наша программа Alignmentaj работает очень хорошо и даже очень быстро.\n '
              'Наша программа Alignmentaj работает с локальным выравниванием.\n '
              'Alignmentaj получает на вход два файла в формате фаста,\n '
              'и на выходе вы сначала получаете данные о\n '
              'белков, которые вы дали программе, то есть название\n '
              'белок, идентификационный номер белка и аминокислотные\n '
              'последовательности белка. А также получить вывод этих\n '
              'пентапептидов, которые программа нашла, а также получайте номер\n '
              'линий, которые начинаются там, где эти пентапептиды находятся в белках.\n'
              'Наша программа доступна на английском и русском языке.')
    if h == 'начать':
        a = input('Укажите путь к файлу fasta 1: ')
        b = input('Укажите путь к файлу fasta 2: ')
        j = int(input('Напишите количество предложенных аминокислотных последовательностей: '))
        if j < 4 or j == 4:
            print('Последовательность начинается только с пентапептидов!')
        if j > 5 or j == 5:
            file = open(a)
            records = parse(file, 'fasta')
            if records == parse(file, 'fasta'):
                print('file not as fasta format!')
            for record in records:
                record.seq

            file1 = open(b)
            humans = parse(file1, 'fasta')
            for human in humans:
                human.seq

            a = record.seq
            b = human.seq
            c = len(human.seq)
            d = len(record.seq)
            for i in range(c):
                if len(b[i:i + j]) < 4:
                    break
                if b[i:i + j] in a:
                    name_protein1 = record.name
                    print('НАЗВАНИЕ и идентификационный номер белка из первого файла: ',
                          name_protein1)
                    seq_protein1 = record.seq
                    print('ПОСЛЕДОВАТЕЛЬНОСТИ из первого белка: ', seq_protein1)
                    print('ПЕПТИД из первого белка: ', b[i:i + j])
                    kar = b[i:i + j]
                    print('Номер начала пептида в белке: ',
                          a.find(kar) + 1)

            for dal in range(d):
                if len(a[dal:dal + j]) < 4:
                    break
                if a[dal:dal + j] in b:
                    name_protein2 = human.name
                    print('НАЗВАНИЕ и идентификационный номер белка из второго файла: ', name_protein2)
                    seq_protein2 = human.seq
                    print('ПОСЛЕДОВАТЕЛЬНОСТИ из второго белка: ', seq_protein2)
                    print('ПЕПТИД из второго белка: ', a[dal:dal + j])
                    kar2 = a[dal:dal + j]
                    print('Номер начала пептида во втором белке: ',
                          b.find(kar2) + 1)

            print('Результаты готов!')
            print('Спасибо, что используете Alignmentaj!')

    if h == 'стоп':
        print('Спасибо, что используете Alignmentaj!')

    if h == 'автор':
        print('Данные автора:\n'
            'Имя: Муслимбек,\n'
            'Отчество: Гуломович,\n'
            'Фамиля: Норматов,\n'
            'Контакт: muslimbek_normatov@mail.ru')





