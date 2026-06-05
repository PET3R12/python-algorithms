<a id="readme-top"></a>
<div align="center">

  <h3 align="center">python algorithms</h3>

  <p align="center">
    A collection of algorithms and theoretical documentation for the <i>Metody Inżynierii Wiedzy</i> course at <i>University of Warmia and Mazury</i>.
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#repository-structure">Repository Structure</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

## About The Project

This repository contains various algorithmic implementations and their theoretical breakdowns created for the **Metody Inżynierii Wiedzy** (*Knowledge Engineering Methods*) course at the **University of Warmia and Mazury**. 

The project was developed during the **2025/2026** academic year and focuses on practical engineering solutions, mathematical calculations, and visual data representations.

### Repository Structure

The workspace is organized into two main directories to separate theory from code:

* `pdf-s/` - Contains detailed theoretical documents and step-by-step mathematical breakdowns of how each algorithm operates.
* `algorithms/` - Contains the actual Python source code of the algorithms, along with any optional supplementary files.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

The project strictly utilizes modern tools and fundamental data science libraries specified in the `uv.lock` file:

* [![Python](https://img.shields.io/badge/Python_3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
* [![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)](https://matplotlib.org/)
* [![uv](https://img.shields.io/badge/uv-DE5D83?style=for-the-badge)](https://github.com/astral-sh/uv)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

Follow these simple steps to set up the repository locally and run the algorithms.

### Prerequisites

This project uses **uv** for fast and reproducible package management. Make sure you have it installed on your system.

### Installation

1. Clone the repo
   ```sh
   git clone [https://github.com/PET3R12/repo_name.git](https://github.com/PET3R12/repo_name.git)
   ```
2. Navigate to the project directory
   ```sh
   cd repo_name
   ```
3. Sync the environment and install all dependencies automatically using the lockfile
   ```sh
   uv sync
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

After installing the dependencies, you can run the algorithms directly from the `algorithms` directory. 

```sh
# Example of running an algorithm script using uv
uv run algorithms/example_algorithm_script.py
```

*Note: For a detailed understanding of the logic behind each script, refer to the corresponding documentation inside the `pdf-s` folder.*

<p align="right">(<a href="#readme-top">back to top</a>)</p>
