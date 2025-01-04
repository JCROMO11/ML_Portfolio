import glob
import fileinput
import os


def load_input(input_directory):
    dir_path = input_directory + "/*.txt"
    filenames = glob.glob(dir_path)

    sequence = []
    with fileinput.input(files=filenames) as file:
        for line in file:
            tupla = (fileinput.filename(), line)
            sequence.append(tupla)
    return sequence


def mapper(sequence):
    new_sequence = []
    for _, text in sequence:
        words = text.split()
        for word in words:
            word = word.replace(",", "")
            word = word.replace(".", "")
            word = word.lower()
            new_sequence.append((word, 1))
    return new_sequence


def shuffle_and_sort(sequence):
    new_sequence = sorted(sequence, key=lambda x: x[0])
    return new_sequence


def reducer(sequence):
    diccionario = {}
    for key, value in sequence:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)

    new_sequence = []
    for key, value in diccionario.items():
        tupla = (key, sum(value))
        new_sequence.append(tupla)

    return new_sequence


def create_output_directory(output_directory):

    if os.path.exists(output_directory):
        raise FileExistsError(f"The directory '{output_directory}' already exists.")
    os.makedirs(output_directory)


def save_output(output_directory, sequence):
    with open(f"{output_directory}/part-00000", "w") as file:
        for key, value in sequence:
            file.write(f"{key}\t{value}\n")


def job(input_directory, output_directory):
    sequence = load_input(input_directory)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    create_output_directory(output_directory)
    save_output(output_directory, sequence)


if __name__ == "__main__":
    job("input", "output")
