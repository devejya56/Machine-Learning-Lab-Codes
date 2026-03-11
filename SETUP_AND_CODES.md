# Setup Instructions and Complete Code Samples

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/devejya56/Machine-Learning-Lab-Codes.git
cd Machine-Learning-Lab-Codes
```

### 2. Create Lab Folders
```bash
mkdir -p Lab-01-Python-NumPy-Pandas
mkdir -p Lab-03-Descriptive-Statistics
mkdir -p Lab-04-Regression-And-Classification
```

### 3. Install Requirements
```bash
pip install jupyter numpy pandas matplotlib seaborn scikit-learn scipy
```

### 4. Run the Notebook Generator
```bash
python create_notebooks.py
```

## LAB 01: Python, NumPy & Pandas - Complete Code Samples

### Exp1: Create NumPy Array from Python List
```python
import numpy as np

python_list = [10, 20, 30, 40, 50]
arr = np.array(python_list)

print("Array:", arr)
print("Shape:", arr.shape)
print("Data Type:", arr.dtype)
```

### Exp2: Create Matrices
```python
import numpy as np

# Create a 3x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)
print("Dimension:", matrix.ndim)

# Matrix operations
print("Sum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
```

### Exp3: Random Arrays
```python
import numpy as np

# Random floats between 0 and 1
random_arr = np.random.rand(3, 3)
print("Random array:\n", random_arr)

# Random integers
random_int = np.random.randint(1, 100, 10)
print("Random integers:", random_int)

# Random normal distribution
random_normal = np.random.randn(5)
print("Random normal:", random_normal)
```

### Exp4: Pandas DataFrame
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'Score': [85, 90, 78, 92]}

df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
```

### Exp5: Load CSV File
```python
import pandas as pd

# Example of loading CSV
# df = pd.read_csv('data.csv')
# print(df.head())

# For testing, create sample data
data = {'ID': [1, 2, 3], 'Value': [100, 200, 300]}
df = pd.DataFrame(data)
print(df)
```

### Exp6: EDA - head(), tail(), info()
```python
import pandas as pd

data = {'Name': ['A', 'B', 'C', 'D', 'E'],
        'Score': [85, 90, 78, 92, 88]}
df = pd.DataFrame(data)

print("Head:")
print(df.head(2))
print("\nTail:")
print(df.tail(2))
print("\nInfo:")
df.info()
```

### Exp7: EDA - describe() and dtypes
```python
import pandas as pd

data = {'Score': [85, 90, 78, 92, 88, 95, 80]}
df = pd.DataFrame(data)

print("Descriptive Statistics:")
print(df.describe())
print("\nData Types:")
print(df.dtypes)
```

### Exp8: Data Type Conversions
```python
import pandas as pd

df = pd.DataFrame({'Score': ['85', '90', '78', '92']})
print("Original type:", df['Score'].dtype)

df['Score'] = df['Score'].astype(int)
print("Converted type:", df['Score'].dtype)
print(df)
```

## LAB 03: Descriptive Statistics - Code Structure

Load data and perform:
- Mean, median, mode
- Variance, standard deviation
- Percentiles and quartiles
- Correlation and covariance
- Visualization (histograms, boxplots)

## LAB 04: Regression & Classification - Code Structure

Implement:
- Linear Regression (simple and multiple)
- Logistic Regression
- Cross-validation
- Confusion matrix and classification metrics
- ROC and PR curves

## Creating Notebooks Manually

If you prefer to create notebooks manually:
1. Open Jupyter: `jupyter notebook`
2. Create new notebook in each lab folder
3. Copy the code samples from the sections above
4. Run the cells to verify

## Next Steps

1. Complete all experiments in each lab
2. Test all code cells
3. Commit and push to GitHub
4. Share the repository
