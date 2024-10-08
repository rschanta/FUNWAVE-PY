#!/bin/bash -l
#
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --job-name=posta
#SBATCH --partition=standard
#SBATCH --time=7-00:00:00
#SBATCH --output=/work/thsu/rschanta/RTS-PY/runs/test_matrix2/logs/posta/out/out%a.out
#SBATCH --error=/work/thsu/rschanta/RTS-PY/runs/test_matrix2/logs/posta/err/err%a.out
#SBATCH --mail-user=rschanta@udel.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --export=ALL
#SBATCH --array=1-80
#SBATCH --dependency=afterany:28250083
#

conda activate tf_env
python /work/thsu/rschanta/RTS-PY/runs/test_matrix2/model_pipeline/p03a_condense.py /lustre/scratch/rschanta test_matrix2  $SLURM_ARRAY_TASK_ID
