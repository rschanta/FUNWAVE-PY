#!/bin/bash -l
#
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --partition=thsu
#SBATCH --time=7-00:00:00
#SBATCH --mail-user=rschanta@udel.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --export=ALL
#SBATCH --array=1-20
#SBATCH --job-name=run_files
#SBATCH --dependency=28297421
#SBATCH --output=/work/thsu/rschanta/RTS-PY/runs/Dune3c/logs/Val_1/run_files/out/out%a.out
#SBATCH --error=/work/thsu/rschanta/RTS-PY/runs/Dune3c/logs/Val_1/run_files/err/err%a.out
#

    . /opt/shared/slurm/templates/libexec/openmpi.sh
    ## Construct name of file
        input_dir="/lustre/scratch/rschanta/Dune3c/Val_1/inputs/"
        task_id=$(printf "%05d" $SLURM_ARRAY_TASK_ID)
        input_file="${input_dir}input_${task_id}.txt"
    ## Run FUNWAVE
        ${UD_MPIRUN} /work/thsu/rschanta/RTS/funwave/v3.6H/exec/FW-REG "$input_file"

    ## COMPRESS
    conda activate tf_env
    export WORK_DIR=/work/thsu/rschanta/RTS-PY 
    export DATA_DIR=/work/thsu/rschanta/DATA
    export TEMP_DIR=/lustre/scratch/rschanta
    export FW_MODEL=Dune3c
    export RUN_NAME=Val_1
    export $SLURM_ARRAY_TASK_ID
    python RTS-PY/runs/Dune3/model_pipelines/Validate_1/p02_run_condense.py" 

    ## Remove Raw Folder

    