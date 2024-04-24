### Description ###
Graph networks can represent a large variety of phenomena and their visualization can show different levels of abstraction.
In this example, the network nodes represent neurons within a human brain, such that they have a physical location assigned to them.
Such point-like locations in 3D space can be represented by geomtric objects, such as spherical glyphs, while connections between nodes can be represented by connecting lines.
Properties such as size or color of glyphs and lines can then be used to encode additional attributes.

This specific example is a single snapshot of one member of a brain simulation ensembles provided in the 2023 IEEE SciVis Contest [1](#reference_dataset).
The data is based on clinical measurements of actual human brains and activity is simulated based on the model of strucural plasticity [2](#plasticity).
Each individual neuron has target calcium levels assigned to them as well as a corresponding area in the brain.
The target level is mapped to the glyph's color, while the different areas are visible through the coloring of the connecting lines representing synapses.

### References ###
1. [<span id="reference_dataset">T. Gerrits, F. Czappa, D. Baneshund F. Wolf, "IEEE SciVis Contest 2023 - Dataset of Neuronal Network Simulations of the Human Brain". Zenodo, Okt. 19, 2022. doi: 10.5281/zenodo.10519411.](https://zenodo.org/records/10519411)
2. [<span id="plasticity">Markus Butz, Arjen van Ooyen, 2013, "A simple rule for dendritic spine and axonal bouton formation can account for cortical reorganization after focal retinal lesions", doi: https://doi.org/10.1371/journal.pcbi.1003259</span>](https://doi.org/10.1371/journal.pcbi.1003259)