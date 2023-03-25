import math

def calc_sequence(p0, pn, n):
    seq = [p0]
    while len(seq) < n:
        seq.append(pn(seq[len(seq) - 1]))
    return seq

def aitkens_sequence(seq):
    aitkens = []
    for i in range(len(seq) - 2):
        aitkens.append(seq[i] - ((seq[i+1]-seq[i])**2)/(seq[i+2] - 2*seq[i+1] + seq[i]))
    return aitkens

if __name__ == "__main__":
    p0 = 0.75
    pn = lambda x : ((math.e**x) / 3)**0.5
    seq = calc_sequence(p0, pn, 7)
    aitkens = aitkens_sequence(seq)
    print()
    print('Original Sequence: ')
    print(seq)
    print()
    print('Aitkens Sequence: ')
    print(aitkens)
