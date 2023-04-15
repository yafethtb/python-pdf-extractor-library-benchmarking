import os
from SpellBench import SpellBenchmark
import json
from sys import argv

"""
----------------
HOW TO USE
----------------
This file can be used by directly typing onto CLI in these pattern:
python benchmark_process.py {directory of text files} {library name used for extracting pdf}

---------
Example:
---------
I'm using PDFMiner for extracting PDFs and I put the result in folder D named "pdfminer_result".
So to benchmark the results I will type:

    python benchmark_process.py "D:\pdfminer_result" pdfminer

The result is a JSON file.
"""


path = argv[1]

# Listing file names
filelist = []
for filename in os.listdir(path):
    filelist.append(filename)

# Bencmarking
benchdata = []
for file in filelist:
    print(f"> Open file {file}.")
    filepath = os.path.join(path, file)

    with open(filepath, 'r') as f:
        text = f.read().replace('\n', ' ')
    
    print(f">> Benchmarking {file}.")
    bench = SpellBenchmark(text)
    benchdata.append(
        {
            "library": argv[2],
            "file": file,
            'total words': bench.wordcount,
            "misspelled": bench.misscount,
            "accuracy (%)": bench.accuracy
        }
    )
    
    print(">>> DONE. Next iteration....")

# Export as JSON file
with open(f"{argv[2]}_benchmarking.json", "w") as benchmark:
    json.dump(benchdata, benchmark, indent = 4)

