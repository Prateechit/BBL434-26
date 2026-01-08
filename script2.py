#!/usr/bin/env python3
import sys

def read_fasta_single(fasta_file):
    seq = []
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith(">"):
                continue
            seq.append(line.strip().upper())
    return "".join(seq)

def unique_kmer_count(sequence, k=3):
    if len(sequence) < k:
        return 0
    kmers = set(sequence[i:i+k] for i in range(len(sequence) - k + 1))
    return len(kmers)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python unique_kmer.py <seq.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequence = read_fasta_single(fasta_file)

    k = 3
    count = unique_kmer_count(sequence, k)
    print(f"Unique {k}-mer count: {count}")
