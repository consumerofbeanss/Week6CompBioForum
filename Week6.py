from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo

input_file = 'sample_sequences.fasta'
alignment = AlignIO.read(input_file, 'fasta')

calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)
print('Distance Matrix:', distance_matrix)

constructor = DistanceTreeConstructor(calculator, method='nj')
phylo_tree = constructor.build_tree(alignment)
phylo_tree.rooted = True

Phylo.draw(phylo_tree)
Phylo.write(phylo_tree, 'phylogenetic_tree.xml', 'phyloxml')
