import subprocess
import os
import re
import sys
# Make sure workdir is on the path
sys.path.append("/work/thsu/rschanta/RTS-PY")
import funwave_ds.fw_ba as fba

# Standard Slurm Flags
slurm_defaults = {
    "nodes": 1,
    "tasks-per-node": 32,
    "partition": "thsu",
    "time": "7-00:00:00",
    "mail-user": "rschanta@udel.edu",
    "mail-type": "BEGIN,END,FAIL",
    "export": "ALL"
}

work_dir = "/work/thsu/rschanta/RTS-PY"
run_name = "dep_flat_reg"
env_name = "tf_env"
super_path = "/lustre/scratch/rschanta"
matrix = "matrix_1"

os.environ['WORK_DIR'] = "/work/thsu/rschanta/RTS-PY"
os.environ['RUN_NAME'] = "dep_flat_reg"
os.environ['SUPER_PATH'] = "/lustre/scratch/rschanta"
os.environ['ENV_NAME'] = "tf_env"
os.environ['MATRIX'] = "matrix"

FW_ex = "/work/thsu/rschanta/RTS/funwave/v3.6H/exec/FW-REG"

# Initialize the pipeline
pipeline = fba.SlurmPipeline(slurm_vars=slurm_defaults, 
                         work_dir=work_dir, run_name=run_name, matrix=matrix,env_name=env_name)

# Import parts of the pipeline
from pipeline import generate_files, run_files

# Define the steps with their respective arguments and optional SLURM edits
#generate_files: {"file": "p01_generate_files.py"},
steps = {
    run_files: {"FW_ex": FW_ex, "file": "p02_run_condense.py", "slurm_edit": {"array": "4500-8910"}},
}

# Run the pipeline
pipeline.run_pipeline(steps)
