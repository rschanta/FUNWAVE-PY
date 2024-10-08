import argparse
from pathlib import Path
import os
import sys


#%%
def main(super_path, run_name,tri_num):
    
    # Path Commands
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
    
    # Import needed functions
    import python_code as pc
    
    # Assemble path to out_XXXXX RESULT_FOLDER
    out_XXXXX = Path(f'{super_path}/{run_name}/outputs-raw/out_{tri_num:05}/')
    
    # Variables to search for and their paths
    var_list = ['eta_','dep','time_dt']
    var_paths = pc.co.ke.get_list_var_output_paths(out_XXXXX, var_list)
    tri_str = pc.co.ke.get_numbers(filepath=out_XXXXX)['tri']

    # Load in inputs from In_d
    In_d = pc.co.ke.load_In_d(f'{super_path}/{run_name}/inputs-proc/In_d.pkl')

    # Compress all the outputs to tensors in a dictionary
    tensor_dict = pc.co.ke.load_and_stack_to_tensors(var_paths,In_d,tri_str)
    
    # Serialize everything
    serialized_features = pc.co.ke.serialize_inputs(In_d, tri_str, {})
    serialized_features = pc.co.ke.serialize_outputs(tensor_dict, serialized_features)
    serialized_features = pc.co.ke.serialize_bathy_array(In_d, tri_str, serialized_features)
    
    # Save Out
    save_name = f'{super_path}/{run_name}/outputs-proc/out_{tri_num:05}.tfrecord'
    pc.co.ke.save_tfrecord(serialized_features,save_name)
    
    print(f'Successfully saved out_{tri_num:05}.tfrecord')
    return

#%%
if __name__ == "__main__":
    # Define the parser
    parser = argparse.ArgumentParser(description="Process variables for compression")
    
    # Add arguments and descriptions
    parser.add_argument("super_path", type=str, help="Path to super directory")
    parser.add_argument("run_name", type=str, help="Name of the run")
    parser.add_argument("tri_num", type=int, help="Trial number")

    # Call the parser
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args.super_path, args.run_name,args.tri_num)
    