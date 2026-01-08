#!/usr/bin/env python3
import sys

def fasta_length(fasta_file):
    seq = []
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith(">"):
                continue
            seq.append(line.strip())
    return len("".join(seq))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fasta_len.py <seq.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    length = fasta_length(fasta_file)
    print(f"Sequence length: {length}")
