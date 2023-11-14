# %%
'''
Given a sequence of 100 numbers find the largest subsequence which is increasing. For example, if the given sequence is 5,2,4,11,8,9,3,8,12,14,7,6,9 the increasing subsequences are
[5], [2, 4, 11], [8, 9], [3, 8, 12, 14], [7], [6, 9]
The largest being the subsequence [3,8,12,14], of length 4.
'''

seq = [1, 32, 49, 54, 21, 16, 26, 79, 73, 90, 31, 27, 74, 56, 59, 6, 68, 8, 77, 67, 13, 22, 5, 88, 53, 40, 85, 46, 14, 45, 86, 95, 64, 42, 61, 62, 15, 39, 37, 10, 80, 28, 93, 25, 78, 63, 50, 3, 94, 47, 34, 19, 72, 4, 69, 17, 87, 60, 58, 82, 35, 36, 55, 33, 2, 11, 52, 83, 51, 12, 57, 44, 9, 92, 75, 84, 30, 20, 89, 29, 91, 38, 41, 23, 70, 66, 7, 24, 18, 71, 81, 76, 43, 48, 65, 96]
sub_sequences = []
sub_seq = []
max_len_sub_seqs = []
for index in range(len(seq)-1):
    if seq[index] <= seq[index+1]:
        sub_seq.append(seq[index])
    else:
        sub_seq.append(seq[index])
        sub_sequences.append(sub_seq)
        sub_seq = []

len_sub_seq = [len(sub_seqs) for sub_seqs in sub_sequences]
for index, length in enumerate(len_sub_seq):
    if length == max(len_sub_seq):
        max_len_sub_seqs.append(sub_sequences[index])
        
print(f"The largest being the subsequence {max_len_sub_seqs} of length {max(len_sub_seq)}" )