# Daily Log - 3monthproject

**Exercise Number:** Month-01, Week-01, Day-01  
**Exercise Title:** Creating and manipulating Pandas Series  
**Key Learnings:** Learned to create Series from a list; assign custom index; access elements by index; update values; perform arithmetic operations on all elements  
**Challenges:** Remembering the difference between default index and custom index; ensuring index length matches data length  
**Solutions / Insights:** Always use correct index when updating values; arithmetic operations on Series are element-wise

---

**Exercise Number:** Month-01, Week-01, Day-02  
**Exercise Title:** Creating and exploring DataFrames  
**Key Learnings:** Creating a DataFrame from a dictionary; accessing columns and rows with `.iloc`; using `head()` and `tail()` to preview data  
**Challenges:** Understanding row vs. column selection syntax; handling mixed data types  
**Solutions / Insights:** Use `.iloc` for positional indexing; `head()`/`tail()` are useful for quick data inspection

---

**Exercise Number:** Month-01, Week-01, Day-03  
**Exercise Title:** Reading and summarizing CSV data  
**Key Learnings:** Loading a CSV file with `pd.read_csv()`; exploring data structure with `.info()` and `.describe()`  
**Challenges:** Managing file paths correctly; interpreting `.describe()` output for numerical columns  
**Solutions / Insights:** Use raw strings for Windows file paths; `.describe()` provides quick statistical overview

---

**Exercise Number:** Month-01, Week-01, Day-04  
**Exercise Title:** Basic data cleaning, filtering, and sorting  
**Key Learnings:** Checking for missing values with `.isna().sum()`; filling missing values using `.bfill()`; filtering rows with `.query()`; sorting with `.sort_values()`; saving DataFrame to CSV  
**Challenges:** Choosing appropriate fill methods; writing correct query conditions  
**Solutions / Insights:** `.bfill()` propagates next valid observation forward; `.query()` allows readable filtering; `ignore_index=True` resets index after sorting

---

**Exercise Number:** Month-01, Week-01, Day-05  
**Exercise Title:** Comprehensive data cleaning and transformation  
**Key Learnings:** Setting index column while reading CSV; handling missing values per column type; renaming columns; filtering and selecting data with `.query()`, `.loc`, and `.iloc`; multi-column sorting; saving processed data  
**Challenges:** Managing different data types during filling; complex multi-condition sorting  
**Solutions / Insights:** Fill numerical columns with mean (rounded) and categorical with "UNKNOWN"; use list for `ascending` parameter in multi-column sort; `.iloc` uses integer positions, `.loc` uses labels

---

**Exercise Number:** Month-01, Week-02, Day-01  
**Exercise Title:** Data selection techniques in Pandas  
**Key Learnings:** Accessing single and multiple columns; selecting rows with `.loc` and `.iloc`  
**Challenges:** Understanding the difference between `.loc` (label-based) and `.iloc` (integer position-based)  
**Solutions / Insights:** `.loc` includes the endpoint, `.iloc` excludes it; use column name lists for multi-column selection

---

**Exercise Number:** Month-01, Week-02, Day-03  
**Exercise Title:** Sorting and limiting data  
**Key Learnings:** Sorting by single and multiple columns; ascending/descending control; using `.head()` and `.tail()` to limit results  
**Challenges:** Handling NaN values during sorting; managing sort direction for multiple columns  
**Solutions / Insights:** Drop or fill NaN before sorting; pass a list to `ascending` for multi-column sorting

---

**Exercise Number:** Month-01, Week-02, Day-04  
**Exercise Title:** Advanced filtering and result limitation  
**Key Learnings:** Multi-condition filtering with `.query()`; using methods like `.between()`, `.isin()`, `.str.startswith()`; sorting filtered results; selecting specific rows and columns together  
**Challenges:** Writing complex query conditions; understanding that filtering doesn't modify original DataFrame unless assigned  
**Solutions / Insights:** Save filtered results to a new variable; chain `.iloc` for row/column subset selection

---

**Exercise Number:** Month-01, Week-02, Day-05  
**Exercise Title:** Real dataset processing with queries and statistics  
**Key Learnings:** Applying multi-condition filters; sorting data; calculating basic statistics (sum, mean, median, std, min, max); using `.agg()` for multiple aggregations  
**Challenges:** Writing negative conditions in queries; applying different aggregation functions per column  
**Solutions / Insights:** Use `not` operator or `!=` in queries; pass dictionary to `.agg()` for column-specific aggregations

---

**Exercise Number:** Month-01, Week-02, Day-07  
**Exercise Title:** Review: selection, filtering, sorting, and basic statistics  
**Key Learnings:** Selecting important columns; filtering rows with string conditions and numerical comparisons; sorting and resetting index; adding new columns; calculating statistical summaries  
**Challenges:** Handling NaN values before string operations; applying multiple statistical functions  
**Solutions / Insights:** Drop NaN before `.str` operations; use `.agg()` to apply multiple statistics to a column

---

**Exercise Number:** Month-01, Week-03, Day-01  
**Exercise Title:** Reading multi-sheet Excel files  
**Key Learnings:** Reading entire Excel file with `sheet_name=None`; accessing specific sheets; selecting columns with `usecols`; limiting rows with `nrows`  
**Challenges:** Managing dictionary structure when reading all sheets; selecting appropriate sheet indices  
**Solutions / Insights:** Use `.keys()` to see sheet names; `usecols` and `nrows` optimize memory usage

---

**Exercise Number:** Month-01, Week-03, Day-02  
**Exercise Title:** Saving DataFrames to Excel  
**Key Learnings:** Saving single DataFrame to Excel with `.to_excel()`; appending multiple sheets using `pd.ExcelWriter` with mode='a'  
**Challenges:** Preventing sheet overwrite; reading back saved data for verification  
**Solutions / Insights:** Use `ExcelWriter` with `if_sheet_exists="new"` to add sheets; mode='a' allows appending

---

**Exercise Number:** Month-01, Week-03, Day-03  
**Exercise Title:** Combining DataFrames with concat  
**Key Learnings:** Concatenating DataFrames vertically and horizontally; handling duplicates and NaN after concatenation  
**Challenges:** Matching dimensions for horizontal concatenation; cleaning combined data  
**Solutions / Insights:** Use `axis=1` for horizontal concat; apply `.dropna()` and `.drop_duplicates()` post-concatenation

---

**Exercise Number:** Month-01, Week-03, Day-04  
**Exercise Title:** Merging DataFrames with join operations  
**Key Learnings:** Performing outer, inner, left, and right joins with `pd.merge()`; ordering results with nulls last using DuckDB; selecting specific columns after merge  
**Challenges:** Understanding join type differences; handling NULL values in output  
**Solutions / Insights:** DuckDB's `ORDER BY ... NULLS LAST` organizes nulls; specify columns to keep after merge

---

**Exercise Number:** Month-01, Week-03, Day-06  
**Exercise Title:** Real-world merge and data completion  
**Key Learnings:** Merging two Excel files on a unique key; identifying and filling missing values using random sampling from existing data; saving merged result  
**Challenges:** Selecting appropriate key for merge; filling missing values realistically  
**Solutions / Insights:** Use unique identifier columns for merge; sample from existing data to fill missing values realistically

---

**Exercise Number:** Month-01, Week-04, Day-03  
**Exercise Title:** Grouping and aggregation  
**Key Learnings:** Selecting grouping columns based on uniqueness percentage; grouping with `.groupby()`; calculating mean per group  
**Challenges:** Choosing optimal column for grouping; applying aggregation to multiple numeric columns  
**Solutions / Insights:** Calculate percentage of unique values to find good grouping columns; use `as_index=False` to keep grouping column as regular column

---

**Exercise Number:** Month-01, Week-04, Day-04  
**Exercise Title:** Basic plotting with Matplotlib  
**Key Learnings:** Creating line and bar charts; adding labels, title, and legend; displaying plot  
**Challenges:** Setting up x-axis for bar charts; customizing plot appearance  
**Solutions / Insights:** Create x-axis range manually for bar charts; use `plt.show()` to display

---

**Exercise Number:** Month-01, Week-04, Day-05  
**Exercise Title:** Data visualization from processed data  
**Key Learnings:** Plotting bar charts from grouped data; adding line plots on same axes; customizing chart elements; saving figures  
**Challenges:** Overlaying different plot types; managing axis labels  
**Solutions / Insights:** Plot bar first then line on same axes; use `plt.savefig()` to export image

---

**Exercise Number:** Month-01, Week-04, Day-06  
**Exercise Title:** Complete data cleaning, grouping, and visualization pipeline  
**Key Learnings:** Cleaning data by filling missing values with mode; grouping by categorical column; creating multi-series bar chart; saving both data and visualization  
**Challenges:** Preparing data for grouped bar chart; ordering bars logically  
**Solutions / Insights:** Sort data before plotting for ordered bars; use width parameter to differentiate series in bar chart

---

**Exercise Number:** Month-02, Week-01, Day-01  
**Exercise Title:** Vector operations with NumPy  
**Key Learnings:** Creating NumPy arrays; performing scalar arithmetic; calculating vector norm  
**Challenges:** Understanding array vs. list behavior; computing vector magnitude  
**Solutions / Insights:** NumPy arrays enable element-wise operations; `np.linalg.norm()` calculates Euclidean length

---

**Exercise Number:** Month-02, Week-01, Day-02  
**Exercise Title:** Matrix creation and operations  
**Key Learnings:** Creating 2D arrays; selecting rows, columns, elements; computing row/column sums and means  
**Challenges:** Understanding axis parameter in aggregation functions  
**Solutions / Insights:** `axis=0` means column-wise, `axis=1` means row-wise

---

**Exercise Number:** Month-02, Week-01, Day-03  
**Exercise Title:** Matrix multiplication  
**Key Learnings:** Creating random matrices; checking dimension compatibility; performing matrix multiplication  
**Challenges:** Ensuring inner dimensions match for multiplication  
**Solutions / Insights:** Check `shape[1]` of first matrix equals `shape[0]` of second matrix before multiplying

---

**Exercise Number:** Month-02, Week-01, Day-04  
**Exercise Title:** Matrix determinant and inverse  
**Key Learnings:** Calculating determinant with `np.linalg.det()`; computing inverse if determinant non-zero  
**Challenges:** Handling non-invertible matrices; managing floating-point precision  
**Solutions / Insights:** Check determinant != 0 before inverting; use `.round()` to control decimal display

---

**Exercise Number:** Month-02, Week-01, Day-05  
**Exercise Title:** Solving linear systems  
**Key Learnings:** Setting up coefficient matrix and constant vector; solving with `np.linalg.solve()`  
**Challenges:** Ensuring square system; verifying solution  
**Solutions / Insights:** System must be square (n equations, n unknowns) for `solve()`; check by substituting back

---

**Exercise Number:** Month-02, Week-01, Day-06  
**Exercise Title:** Comprehensive matrix operations review  
**Key Learnings:** Matrix addition, subtraction, multiplication; determinant and inverse calculation; solving linear systems  
**Challenges:** Performing multiple operations sequentially; verifying results  
**Solutions / Insights:** Use random seed for reproducibility; check matrix properties step by step

---

**Exercise Number:** Month-02, Week-01, Day-07  
**Exercise Title:** Advanced matrix operations  
**Key Learnings:** Working with 4x4 matrices; computing row/column sums; finding determinant and inverse; solving 4x4 linear system  
**Challenges:** Managing larger matrices; interpreting results  
**Solutions / Insights:** Larger matrices follow same principles; `solve()` works for any square system with non-zero determinant

---

**Exercise Number:** Month-02, Week-02, Day-01  
**Exercise Title:** Array creation methods  
**Key Learnings:** Creating arrays with `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`  
**Challenges:** Understanding differences between creation methods  
**Solutions / Insights:** `arange()` creates sequences with step; `linspace()` creates evenly spaced numbers within interval

---

**Exercise Number:** Month-02, Week-02, Day-02  
**Exercise Title:** Array operations and mathematical functions  
**Key Learnings:** Element-wise arithmetic operations; applying `sqrt()` and `log()` functions; creating mathematical expressions over arrays  
**Challenges:** Handling division by zero; applying functions to entire arrays  
**Solutions / Insights:** NumPy functions work element-wise on arrays; mathematical expressions apply to entire array

---

**Exercise Number:** Month-02, Week-02, Day-03  
**Exercise Title:** Statistical measures of arrays  
**Key Learnings:** Computing mean, median, std, variance, max, min; understanding relationship between std and variance  
**Challenges:** Interpreting variance vs. standard deviation  
**Solutions / Insights:** Variance = std²; std = √variance; std is in same units as data

---

**Exercise Number:** Month-02, Week-02, Day-04  
**Exercise Title:** Basic plotting with NumPy arrays  
**Key Learnings:** Creating line plots from array data; adding labels and title; saving figures  
**Challenges:** Setting up x-y data for plotting  
**Solutions / Insights:** Create x array first, then compute y from mathematical function

---

**Exercise Number:** Month-02, Week-02, Day-05  
**Exercise Title:** Histograms and scatter plots  
**Key Learnings:** Creating histograms from random data; making scatter plots; using subplots; analyzing data relationships  
**Challenges:** Interpreting histogram bins; identifying data patterns in scatter plots  
**Solutions / Insights:** Histograms show distribution; scatter plots reveal relationships between variables

---

**Exercise Number:** Month-02, Week-02, Day-06  
**Exercise Title:** Multiple function plotting  
**Key Learnings:** Plotting different mathematical functions; calculating statistical measures of function outputs  
**Challenges:** Handling domain issues (e.g., sqrt of negative numbers)  
**Solutions / Insights:** Use `np.abs()` before `sqrt()` for negative domains; different functions produce different output distributions

---

**Exercise Number:** Month-02, Week-02, Day-07  
**Exercise Title:** Integrated NumPy and Matplotlib project  
**Key Learnings:** Creating random dataset; computing statistics; creating histograms and scatter plots; making line charts; analyzing results  
**Challenges:** Integrating multiple visualization types; interpreting complex outputs  
**Solutions / Insights:** Use subplots for multiple visualizations; random data shows inherent variability

---

**Exercise Number:** Month-02, Week-03, Day-01  
**Exercise Title:** NumPy and Pandas integration basics  
**Key Learnings:** Converting between NumPy arrays and Pandas DataFrames; computing statistics in both libraries  
**Challenges:** Understanding axis parameter consistency  
**Solutions / Insights:** NumPy and Pandas use similar axis conventions; conversion between formats is seamless

---

**Exercise Number:** Month-02, Week-03, Day-02  
**Exercise Title:** Variance and standard deviation comparison  
**Key Learnings:** Computing variance and std in NumPy and Pandas; comparing results  
**Challenges:** Small numerical differences between libraries  
**Solutions / Insights:** Pandas and NumPy may show slight differences due to implementation; both are statistically valid

---

**Exercise Number:** Month-02, Week-03, Day-03  
**Exercise Title:** Normal vs. uniform distributions  
**Key Learnings:** Generating normal and uniform distributions; comparing their statistical properties; visualizing differences  
**Challenges:** Understanding distribution characteristics  
**Solutions / Insights:** Normal distribution clusters around mean; uniform distribution spreads evenly; std differs significantly

---

**Exercise Number:** Month-02, Week-03, Day-04  
**Exercise Title:** Synthetic dataset creation and analysis  
**Key Learnings:** Creating realistic dataset with Faker; computing comprehensive statistics; using `describe()`  
**Challenges:** Generating realistic synthetic data; reorganizing DataFrame columns  
**Solutions / Insights:** Faker library creates realistic names; column reordering requires list manipulation

---

**Exercise Number:** Month-02, Week-03, Day-05  
**Exercise Title:** Categorical data analysis  
**Key Learnings:** Adding categorical columns; counting categories with `value_counts()` and `groupby()`; creating bar charts  
**Challenges:** Creating balanced categorical distributions  
**Solutions / Insights:** Use `weights` parameter in `random.choices()` for controlled distributions; `value_counts()` vs `groupby().size()` give similar results

---

**Exercise Number:** Month-02, Week-03, Day-06  
**Exercise Title:** Comprehensive descriptive analysis  
**Key Learnings:** Analyzing real dataset; computing statistics for numerical and categorical columns; creating visualizations  
**Challenges:** Identifying categorical vs. numerical columns; selecting appropriate visualizations  
**Solutions / Insights:** Use `nunique()` to identify categorical columns; histograms for numerical, bar charts for categorical data

---

**Exercise Number:** Month-02, Week-03, Day-07  
**Exercise Title:** Complete data analysis project  
**Key Learnings:** Creating synthetic educational dataset; computing full statistics; creating multiple visualizations; writing analytical summary  
**Challenges:** Managing complex subplots; interpreting synthetic data patterns  
**Solutions / Insights:** Use `constrained_layout=True` for better subplot spacing; synthetic random data often resembles normal distribution

---

**Exercise Number:** Month-02, Week-04, Weekly Exercise  
**Exercise Title:** End-to-end data analysis pipeline  
**Key Learnings:** Complete workflow: data loading, cleaning, exploration, grouping, visualization; handling real-world dataset  
**Challenges:** Managing multi-day project structure; integrating all learned techniques  
**Solutions / Insights:** Break project into logical days; each day builds on previous work; visualizations help communicate findings