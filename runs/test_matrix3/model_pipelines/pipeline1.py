import os
work_dir = os.getenv('WORK_DIR')
run_name = os.getenv('RUN_NAME')
env_name = os.getenv('ENV_NAME')
super_path = os.getenv('SUPER_PATH')

## GENERATE FILES
def generate_files(file=None):
    text_content = f"""
    ## Activate conda environment and compress
    conda activate {env_name}
    python {work_dir}/runs/{run_name}/model_pipelines/{file} {super_path} {run_name} 
    """
    return text_content

## RUN AND CONDENSE
def run_files(file=None,FW_ex=None):

    text_content = f"""
    . /opt/shared/slurm/templates/libexec/openmpi.sh
    ## Construct name of file
        input_dir="{super_path}/{run_name}/inputs/"
        task_id=$(printf "%05d" $SLURM_ARRAY_TASK_ID)
        input_file="${{input_dir}}input_${{task_id}}.txt"
    ## Run FUNWAVE
        ${{UD_MPIRUN}} {FW_ex} "$input_file"

    ## COMPRESS
    conda activate {env_name}
    python {work_dir}/runs/{run_name}/model_pipelines/{file} {super_path} {run_name}  $SLURM_ARRAY_TASK_ID
    """
    return text_content

def postprocessa(file=None):
    text_content = f"""
    conda activate {env_name}
    python {work_dir}/runs/{run_name}/model_pipelines/{file} {super_path} {run_name}  $SLURM_ARRAY_TASK_ID
    """
    return text_content

def postprocessb(file=None):

    text_content = f"""
    conda activate {env_name}
    python {work_dir}/runs/{run_name}/model_pipelines/{file} {super_path} {run_name} 
    """
    return text_content

def ml_model(file=None):
    text_content = f"""
    conda activate {env_name}
    python {work_dir}/runs/{run_name}/model_pipelines/{file} {super_path} {run_name} "test_model"
    """ 
    return text_content