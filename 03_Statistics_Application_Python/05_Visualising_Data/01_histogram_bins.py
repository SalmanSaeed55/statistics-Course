"""Simple Calculator to convert from histogram counts to histogram proportions"""


def histogram_proportions(bin_heights):
    sum_count_heights = sum(bin_heights)
    proportion_heights = []
    for height in bin_heights:
        height_of_bin = height / sum_count_heights
        proportion_heights.append(height_of_bin)

    return proportion_heights


number_of_bins = int(input("Enter the number of bins: "))
height_of_bins = []

for i in range(number_of_bins):
    height_of_bins.append(int(input(f"Enter the height of bin {i + 1} (left to right): ")))

proportions = histogram_proportions(height_of_bins)

print("\nThe heights of the bins are:")
for i in range(len(proportions)):
    print(f"Proportion of bin {i + 1}:\t {proportions[i]:.4f}")
