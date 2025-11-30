import os

# Files to clean
files_to_remove = [
    "decodevideo",
    "videocomp",
    "videoout-64x48x8.dat",
    "stream-64x48x8.dat",
    "tiles-64x48x8.dat",
    # "video-64x48x8.gif", # This is the output the user wants to keep, will be moved
    "gen_badderbaby", # Executable
    "gen_badderbaby.c",
    "huffman_0.dat",
    "vpx_runs.dat",
    "symbol_list.txt",
    # From midclean target
    "test-64x48x8.gif",
    "streamcomp", # Executable
]

def clean_files():
    for f_name in files_to_remove:
        if os.path.exists(f_name):
            try:
                if os.path.isfile(f_name):
                    os.remove(f_name)
                    print(f"Removed file: {f_name}")
                elif os.path.isdir(f_name):
                    pass 
            except Exception as e:
                print(f"Error removing {f_name}: {e}")
        else:
            print(f"File not found: {f_name} (skipped)")

if __name__ == "__main__":
    clean_files()