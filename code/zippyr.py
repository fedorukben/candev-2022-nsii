import shutil

def open_zip(extract_from: str, extract_to: str='.', debug: bool=False):
    try:
        shutil.unpack_archive(extract_from, extract_to)
        if debug:
            print(f'Extracted {extract_from} to {extract_to}.')
            print('Please don\'t forget to call close_zip()')
    except:
        print('Error while extracting zip file.')

def close_zip(directory: str, debug: bool=True):
    try:
        shutil.rmtree(directory)
        if debug:
            print(f'Deleted (recursively) {directory}.')
    except:
        print('Error while deleting directory structure!')
        print('PLEASE DELETE THE WHOLE EXTRACTED DIRECTORY BEFORE PUSHING TO GIT!!!')
close_zip('../data/ext/businesses')
