#!/usr/bin/env python3
"""
Notebook Generator for Machine Learning Lab Codes
Run this script to create all Jupyter notebooks for the three labs.
"""

import json
import os
from pathlib import Path

def create_notebook(title, cells):
    """
    Create a Jupyter notebook structure
    cells: list of dicts with 'cell_type', 'source', and optionally other fields
    """
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    return notebook

def save_notebook(filepath, notebook):
    """Save notebook to file"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(notebook, f, indent=1)
    print(f"Created: {filepath}")

# LAB 01 - EXPERIMENTS
lab01_experiments = {
    "Exp1": {
        "title": "Create NumPy Array from Python List",
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Exp1: Create NumPy Array from Python List\n", "\n", "**Objective:** Create a NumPy array using a Python list, display the array, and print shape and data type."]},
            {"cell_type": "code", "metadata": {}, "source": ["import numpy as np\n", "\n", "# Create a Python list\n", "python_list = [10, 20, 30, 40, 50]\n", "\n", "# Convert list to NumPy array\n", "arr = np.array(python_list)\n", "\n", "# Display the array\n", "print(\"NumPy array:\", arr)\n", "\n", "# Print shape and dtype\n", "print(\"Shape:\", arr.shape)\n", "print(\"Data type:\", arr.dtype)"]}
        ]
    },
    "Exp2": {
        "title": "Create Matrices Using NumPy",
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Exp2: Create Matrices Using NumPy"]},
            {"cell_type": "code", "metadata": {}, "source": ["import numpy as np\n", "\n", "# 2D array (matrix)\n", "matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n", "print(\"Matrix:\\n\", matrix)\n", "print(\"Shape:\", matrix.shape)\n", "print(\"Dimension:\", matrix.ndim)"]}
        ]
    },
    "Exp3": {
        "title": "Create Random Arrays",
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Exp3: Create Random Arrays"]},
            {"cell_type": "code", "metadata": {}, "source": ["import numpy as np\n", "\n", "# Random array\n", "random_arr = np.random.rand(3, 3)\n", "print(\"Random array:\\n\", random_arr)\n", "\n", "# Random integers\n", "random_int = np.random.randint(1, 100, 10)\n", "print(\"Random integers:\", random_int)"]}
        ]
    },
    "Exp4": {
        "title": "Pandas DataFrame Creation",
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Exp4: Pandas DataFrame Creation"]},
            {"cell_type": "code", "metadata": {}, "source": ["import pandas as pd\n", "import numpy as np\n", "\n", "# Create DataFrame\n", "data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [85, 90, 78]}\n", "df = pd.DataFrame(data)\n", "print(df)"]}
        ]
    },
    "Exp5": {
        "title": "Load CSV File",
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Exp5: Load CSV File\n", "\n", "# NOTE: Replace 'data.csv' with your CSV file path"]},
            {"cell_type": "code", "metadata": {}, "source": ["import pandas as pd\n", "\n", "# Load CSV (replace with your file)\n", "# df = pd.read_csv('data.csv')\n", "# print(df.head())"]}
        ]
    },
    "Exp6": {
        "title": "EDA: head(), tail(), info()",
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Exp6: Exploratory Data Analysis"]},
            {"cell_type": "code", "metadata": {}, "source": ["import pandas as pd\n", "\n", "data = {'Name': ['A', 'B', 'C'], 'Score': [85, 90, 78]}\n", "df = pd.DataFrame(data)\n", "\n", "print(\"Head::\")\n", "print(df.head())\n", "print(\"\\nInfo::\")\n", "df.info()"]}
        ]
    },
    "Exp7": {
        "title": "EDA: describe(), dtypes",
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Exp7: Describe and Data Types"]},
            {"cell_type": "code", "metadata": {}, "source": ["import pandas as pd\n", "\n", "data = {'Score': [85, 90, 78, 92]}\n", "df = pd.DataFrame(data)\n", "\n", "print(df.describe())\n", "print(\"\\nData types::\")\n", "print(df.dtypes)"]}
        ]
    },
    "Exp8": {
        "title": "Data Type Conversions",
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Exp8: Data Type Conversions"]},
            {"cell_type": "code", "metadata": {}, "source": ["import pandas as pd\n", "\n", "df = pd.DataFrame({'Score': ['85', '90', '78']})\n", "print(\"Original type:\", df['Score'].dtype)\n", "\n", "df['Score'] = df['Score'].astype(int)\n", "print(\"Converted type:\", df['Score'].dtype)\n", "print(df)"]}
        ]
    }
}

# Create Lab 01 notebooks
for exp_name, content in lab01_experiments.items():
    cells = [
        {"cell_type": "markdown", "metadata": {}, "source": content["cells"][0]["source"]},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": content["cells"][1]["source"]}
    ]
    notebook = create_notebook(content["title"], cells)
    save_notebook(f"Lab-01-Python-NumPy-Pandas/{exp_name}.ipynb", notebook)

print("\nAll Lab 01 notebooks created successfully!")
print("Note: Create Lab 03 and Lab 04 notebooks similarly.")
