
# Evaluation of Spine Loading Across Common Positions Using OpenSim

## Team Members
- Christian Mandujano  
- Michael McGrath

## Overview
This project evaluates how different static postures affect loading on the spine, specifically the lumbar region. Using OpenSim and a validated full-body musculoskeletal model, we simulate common postures encountered in daily life, physical therapy, and stretching exercises. The primary goal is to understand which positions place the least stress on the lower back—especially in light of a prior L3/L5 vertebral injury.

## Simulated Postures
- Standing (Neutral)
- Sitting
- Lifting
- Stretching
- Laying Down

Each posture begins in a standard anatomical neutral pose and transitions to the target pose for analysis.

## Tools & Technologies
- **[OpenSim](https://opensim.stanford.edu/)**: Biomechanical modeling and simulation
- **Python**: For scripting, automation, and generating `.sto` output files
- **OpenSim Creator**: For visualizing simulation outputs
- **Anaconda Environment**: For isolated and reproducible execution of Python scripts

## Directory Structure
```

spine-loading-analysis/
├── README.md
├── .gitignore
├── requirements.txt
├── models/
│   └── MaleFullBodyModel\_v2.0\_OS4.osim
├── scripts/
│   ├── simulate\_postures.py
│   └── utils.py
├── data/
│   └── outputs/          # .sto simulation result files
├── notebooks/
│   └── analysis.ipynb    # Optional visualization notebook
└── docs/
└── posture-diagrams.png (optional)

````

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/spine-loading-analysis.git
cd spine-loading-analysis
````

### 2. Create Environment and Install Dependencies

```bash
conda create -n opensim-env python=3.8
conda activate opensim-env
pip install opensim  # Or use OpenSim Python bindings if needed
```

### 3. Run First Simulation

```bash
python scripts/simulate_postures.py
```

## Research References

1. Beaucage-Gauvreau, E., et al. (2019). Validation of an OpenSim full-body model with detailed lumbar spine for estimating lower lumbar spine loads during symmetric and asymmetric lifting tasks. *Computer Methods in Biomechanics and Biomedical Engineering*, 22(5), 451–464. [DOI](https://doi.org/10.1080/10255842.2018.1564819)

2. Cho, I. Y., et al. (2015). The Effect of Standing and Different Sitting Positions on Lumbar Lordosis: Radiographic Study of 30 Healthy Volunteers. *Asian Spine Journal*, 9(5), 762. [DOI](https://doi.org/10.4184/asj.2015.9.5.762)

## Additional Resources

* OpenSim documentation and tutorials
* SimTK spine-specific musculoskeletal models
* Course concepts in kinematics, dynamics, and optimization

## License

**_This project is for academic and educational purposes._**
