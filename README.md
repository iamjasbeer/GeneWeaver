# GeneWeaver : GPU-Accelerated CRISPR Alignment Engine
**GeneWeaver** is a Python-based bioinformatics project designed to identify DNA sequence matches and potential CRISPR off-target candidates. It uses a modular architecture with a CPU-based alignment engine and is planned to support GPU acceleration and distributed processing.

The project focuses on sequence parsing, DNA validation, mismatch calculation, and efficient genomic sequence scanning.

## 🚀 Features

- **FASTA Parsing:** Read and process genomic DNA sequences using Biopython.
- **DNA Validation:** Validate DNA sequences containing A, T, G, C, and optionally N.
- **DNA Utilities:** Normalize sequences and calculate GC content.
- **Mismatch Scoring:** Count differences between guide and reference DNA sequences.
- **CPU Alignment Engine:** Scan reference sequences using a sliding-window algorithm.
- **Off-Target Candidate Detection:** Identify matching regions within a configurable mismatch limit.
- **Automated Testing:** Validate project functionality using Pytest.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Biopython | FASTA sequence parsing |
| NumPy | Numerical computing |
| Pytest | Unit testing |
| Numba CUDA | Planned GPU acceleration |
| Dask | Planned distributed processing |

## 📁 Project Structure

```text
GeneWeaver/
│
├── app/
│   ├── dna.py
│   ├── parser.py
│   ├── scoring.py
│   └── cpu_engine.py
│
├── data/
│   └── sample.fasta
│
├── tests/
│   ├── test_dna.py
│   └── test_parser.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/iamjasbeer/GeneWeaver.git
cd GeneWeaver
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv geneweaver_env
.\geneweaver_env\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 🧪 Usage

### Parse a FASTA file

```python
from app.parser import parse_fasta

records = parse_fasta("data/sample.fasta")

for record in records:
    print(record["id"])
    print(record["sequence"])
```

### Calculate DNA mismatches

```python
from app.scoring import count_mismatches

guide = "ATGCGT"
target = "ATGCTT"

mismatches = count_mismatches(guide, target)

print("Mismatches:", mismatches)
```

### Find matching DNA candidates

```python
from app.cpu_engine import find_candidates

reference = "ATGCGTACGTTAGC"
guide = "ATGCGT"

candidates = find_candidates(
    reference,
    guide,
    max_mismatches=2
)

for candidate in candidates:
    print(candidate)
```

## 🧬 How It Works

GeneWeaver uses a sliding-window approach to scan a reference DNA sequence.

1. Load DNA sequences from a FASTA file.
2. Normalize and validate the sequences.
3. Compare the guide sequence against reference windows.
4. Calculate mismatches for each window.
5. Return candidate regions within the specified mismatch threshold.

## 🧪 Run Tests

Execute the test suite using:

```bash
python -m pytest -v
```

Run a specific test file:

```bash
python -m pytest tests/test_dna.py -v
```

## 🗺️ Development Roadmap

- [x] DNA sequence utilities
- [x] FASTA parsing
- [x] Mismatch calculation
- [x] CPU-based sequence matching
- [ ] CRISPR PAM recognition and filtering
- [ ] Off-target candidate scoring
- [ ] GPU acceleration using Numba CUDA
- [ ] Distributed sequence processing using Dask
- [ ] Text-based user interface
- [ ] Performance benchmarking

## 🎯 Project Objective

The long-term objective of GeneWeaver is to build a modular and performance-focused CRISPR alignment engine capable of processing large genomic sequences using CPU, GPU, and distributed computing techniques.

## ⚠️ Disclaimer

GeneWeaver is an educational bioinformatics project and is not intended for clinical, diagnostic, or therapeutic use. Candidate matches and scores should not be interpreted as experimentally validated biological predictions.

## 👨‍💻 Author

**Jasbeer Singh**

GitHub: [iamjasbeer](https://github.com/iamjasbeer)

