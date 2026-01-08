#!/usr/bin/env python3
import sys

def count_fasta_records(fasta_file):
    count = 0
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith(">"):
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_records.py <seq.mfa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    record_count = count_fasta_records(fasta_file)

    print(f"Number of FASTA records: {record_count}")
