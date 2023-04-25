# Text Tokenizer

This Python script reads in a template text file with placeholders, a list of names, and a set of text files containing token values. It then generates LaTeX files by replacing the placeholders with the token values from the input files, and compiles the LaTeX files into PDFs.

## Requirements

- Python 3.6+
- LaTeX distribution (e.g., TeX Live or MikTeX)

## Usage

1. Prepare the following input files:
   - `body.txt`: A template text file containing placeholders in the format `[[token1]]`, `[[token2]]`, etc.
   - `name.txt`: A text file with a list of names, one per line.
   - `list1.txt`, `list2.txt`, ... : Text files containing token values to replace the placeholders in the template file. Each file should have the same number of lines as the `name.txt` file.

2. Run the script from the command line as follows:

python script.py "body.txt" "name.txt" "list1.txt" "list2.txt" "list3.txt" ... "list10.txt"


Replace `list1.txt`, `list2.txt`, `list3.txt`, ... with the appropriate file names for your token values.

3. The script will generate LaTeX files named `body_name1.tex`, `body_name2.tex`, etc., where `name1`, `name2`, etc., are the names from the `name.txt` file. Each LaTeX file will have the placeholders replaced with the corresponding token values from the input files.

4. The script will also compile the LaTeX files into PDFs using `pdflatex`.

## Notes

- The number of distinct placeholders in `body.txt` should match the number of `list*.txt` files.
- The number of lines in `name.txt` should match the number of lines in each of the `list*.txt` files.

## Troubleshooting

If you encounter any issues while using this script, please ensure that:

- Your input files are formatted correctly.
- You have a LaTeX distribution installed and `pdflatex` is accessible from the command line.
- Your Python version is 3.6 or later.

If you still have issues, feel free to reach out for further assistance.
