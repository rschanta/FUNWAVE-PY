import argparse
import os 
import sys
import tensorflow as tf


def main(super_path, run_name,tri_num):
    # Add to system path
    sys.path.append("/work/thsu/rschanta/RTS-PY")
    sys.path.append(f"/work/thsu/rschanta/RTS-PY/runs/{run_name}")
    # Get modules
    import funwave_ds.fw_py as fpy
    import funwave_ds.fw_tf as ftf
    import ml_models as ml
    
    ## Get paths
    p = fpy.get_FW_paths(super_path, run_name)
    ptr = fpy.get_FW_tri_paths(tri_num, p)
    paths = ptr['out_record']

    ## Parse in features to dictionary
    parsed_dict = ftf.parse_spec_var(paths,
                tensors_3D = ['eta'],
                tensors_2D = ['bathy','time_dt'],
                floats = ['DX','Xc_WK','AMP_WK','Tperiod'],
                strings = ['ALT_TITLE'])

    ## Apply post-processed features
    out_dict =  ml.ska_conv_1.preprocessing_pipeline3(parsed_dict[f'tri_{tri_num:05}'],0)

    ## Serialize the post-processed features
    feature_dict_ML = ftf.serialize_dictionary(out_dict,{})
    
    ## Save out 
    ftf.save_tfrecord(feature_dict_ML,f'/work/thsu/rschanta/RTS-PY/runs/test_matrix3/processed_outputs/ML_inputs/MLin_{tri_num:05}.tfrecord')

    
    return

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