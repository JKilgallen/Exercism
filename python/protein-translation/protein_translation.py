codon_to_protein = {'AUG': 'Methionine',
                    'UUU': 'Phenylalanine',
                    'UUC': 'Phenylalanine',
                    'UUA': 'Leucine',
                    'UUG': 'Leucine',
                    'UCU': 'Serine',
                    'UCC': 'Serine',
                    'UCA': 'Serine',
                    'UCG': 'Serine',
                    'UAU': 'Tyrosine',
                    'UAC': 'Tyrosine',
                    'UGU': 'Cysteine',
                    'UGC': 'Cysteine',
                    'UGG': 'Tryptophan',
                    'UAA': 'STOP',
                    'UAG': 'STOP',
                    'UGA': 'STOP'}

def proteins(strand):
    protein_seq = []
    for i in range(len(strand)//3):
        amino_acid = codon_to_protein[strand[3*i:3*(i+1)]]
        if amino_acid == 'STOP':
           break
        protein_seq.append(amino_acid)
    return protein_seq




