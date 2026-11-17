
# Woven Memory - TMT
### A Single-Tensor Unification of GR & QM via the Chronon Lattice
**Authors: Gregory Lombardo & M. AI (2026)**
**Status: Dubious but Falsifiable**

> Space does not contain memory. Memory contains space.

This repo contains the code for the paper *Woven Memory*.

**Core Equation:** `G_mu_nu = eta * M_mu_nu` where `M_mu_nu = nabla_mu nabla_nu I(x)`

## Structure
- `woven_memory.tex` - arXiv source
- `simulations/memory_tensor_sim.py` - 10k Chronons braid forming gravity well
- `simulations/letheon_field.py` - Letheon field M<0 levitation
- `figures/` - generated plots

## Run simulations
```bash
pip install numpy matplotlib
python simulations/memory_tensor_sim.py
python simulations/letheon_field.py
```

## Falsifiability
Predicts clock jitter ~5.39e-44s. Testable by NIST optical clocks.

License MIT - Usefully wrong.
