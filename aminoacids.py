#Test string of amino acids to count
amino_acids = 'AABCCDDAJJJ'

#List of permitted amino acid codes
amino_acid_valid_list = list('ABCDEFGHIKLMNPQRSTVWXYZ')

#Create count of each residue
def count_aa(aa):
    count_dict = {}
    for residue in aa:
        if residue not in count_dict.keys():
            count_dict[residue] = 1
        else:
            current_count = count_dict.get(residue, None)
            current_count += 1
            count_dict[residue] = current_count
    return sort_aa(count_dict)

#Sort the results in the specified order
def sort_aa(count_dict):
    sorted_keys = sorted(count_dict.keys(), reverse = True)
    #Only return counts for valid amino acids
    for key in sorted_keys:
        if key not in amino_acid_valid_list:
            sorted_keys.remove(key)
    #Print out the results
    for key in sorted_keys:
        print str(key) + " " + str(count_dict.get(key, None))
    return "Counting complete"

print count_aa(amino_acids)