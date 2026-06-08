# Section 5: Visualising Data

---

## Bar Plots

### Types of Data than can be Represented:
- **_Categorical_**
  - Nominal
  - Ordinal
- **_Numerical_**
  - Discrete

---

## Box Plots

### What is shown on a Box Plot?
- The **_median_** (the line in the middle of the box)
- The **_interquartile range (IQR)_** (the box itself)
- The **_whiskers_** (the lines extending from the box)
- The **_outliers_** (the points outside the whiskers)

---

## Histograms

### Difference between Bar Plots and Histograms:
- **_Bar Plots_**: Used for **categorical** data, bars are separated by spaces
- **_Histograms_**: Used for **continuous, binned** data, bars are adjacent to each other
  - The order of binned categories is important in histograms as it defines the shape of the histogram

### Histogram of Counts
> Usually better for qualitative analysis

| Advantages                                           | Disadvantages                                         |
|------------------------------------------------------|-------------------------------------------------------|
| Can be more meaningful to interpret than raw numbers | Can be difficult to across different datasets/studies |
| Does not need to sum to 1 or 100%                    |                                                       |

### Histogram of Proportions
> Usually better for quantitative analysis

| Advantages                              | Disadvantages                               |
|-----------------------------------------|---------------------------------------------|
| Easy to compare across datasets/studies | Can take extra effort to relate to raw data |
|                                         | Sums up to 1 or 100%                        |

### Converting from Counts to Proportions

`Height of bin = (Height of Counts Bin / Sum of all Counts Bins) x 100`

---

## Pie Charts

> The total of all pie slices must equal 100% (or 1 if using proportions)

### Types of Data than can be Represented:
- Nominal 
- Ordinal
- Discrete

---

## Line Plots vs. Bar Plots

> A line plot assumes that the data points are connected in some way, while a bar plot does not.

### Situations where Line Plots are more appropriate:
1. When there are **_many bars_**
2. When you are **_comparing multiple sets of data_** on the same graph

---

## Linear Scaling vs. Logarithmic Scaling

| Linear Scaling                                                   | Logarithmic Scaling                                                              |
|------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Each interval is found by adding a constant amount onto the last | Each interval is found by multiplying the previous interval by a constant amount |

### Linear Scaling

> Best used unless there a s a compelling reason to use logarithmic scaling

| Advantages                                      | Disadvantages                                        |
|-------------------------------------------------|------------------------------------------------------|
| Often Easier to Interpret                       | Can obscure trends and comparisons between variables |
| Easily scaled to big, small or negative numbers |                                                      |

### Logarithmic Scaling

> Best used only when necessary

| Advantages                                                            | Disadvantages                              |
|-----------------------------------------------------------------------|--------------------------------------------|
| Often appropriate for sciences, finance, growth or really big numbers | Might need explaining to general audiences |
|                                                                       | Might not work for negative numbers        |

