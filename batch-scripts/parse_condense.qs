#!/bin/bash -l
#
#
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --job-name=Condense
#SBATCH --partition=standard
#SBATCH --time=7-00:00:00
#SBATCH --output=/work/thsu/rschanta/RTS-PY/logs/ML/CON6_out.out
#SBATCH --error=/work/thsu/rschanta/RTS-PY/logs/ML/CON6_err.out
#SBATCH --mail-user=rschanta@udel.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --export=ALL
#
#UD_QUIET_JOB_SETUP=YES
#UD_USE_SRUN_LAUNCHER=YES
#UD_DISABLE_CPU_AFFINITY=YES
#UD_MPI_RANK_DISTRIB_BY=CORE
#UD_DISABLE_IB_INTERFACES=YES
#UD_SHOW_MPI_DEBUGGING=YES

## Activate conda environment and compress
conda activate tf_env
python /work/thsu/rschanta/RTS-PY/mains/parse_condense.py
