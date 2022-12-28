from lesson import file_dir_copy, show_dirs, show_files
import shutil, sys, os


def test_file_dir_copy():
    # test copy directory
    try:
        filedirname1 = 'test_dir_name1'
        filedirname2 = 'test_dir_name2'
        if not os.path.exists(filedirname1):
            os.mkdir(filedirname1)
        if os.path.exists(filedirname2):
            shutil.rmtree(filedirname2)  # dir shutil.rmtree() deletes a directory and all its contents.
        if os.path.exists(filedirname1) and not os.path.exists(filedirname2):
            file_dir_copy(filedirname1, filedirname2)
            assert filedirname2 in os.listdir(os.getcwd()), f'Error with copying "{filedirname1}" in "{filedirname2}"'
    except:
        if os.path.exists(filedirname2):
            shutil.rmtree(filedirname2)
    # test copy file
    try:
        filedirname1 = 'test_file_name1'
        filedirname2 = 'test_file_name2'
        if not os.path.exists(filedirname1):
            with open(filedirname1, 'w') as f:
                f.write('\n')
        if os.path.exists(filedirname2):
            os.remove(filedirname2)
        if os.path.exists(filedirname1) and not os.path.exists(filedirname2):
            file_dir_copy(filedirname1, filedirname2)
            assert filedirname2 in os.listdir(os.getcwd()), f'Error with copying "{filedirname1}" in "{filedirname2}"'
    except:
        if os.path.exists(filedirname2):
            shutil.rmtree(filedirname2)


def test_show_dirs():
    filedirname1 = 'test_dir_name1'
    if not os.path.exists(filedirname1):
        os.mkdir(filedirname1)
    assert filedirname1 in os.listdir(os.getcwd()) and os.path.isdir(filedirname1), f'Error with function "show_dirs()"'


def test_show_files():
    filedirname1 = 'test_file_name1'
    if not os.path.exists(filedirname1):
        with open(filedirname1, 'w') as f:
            f.write('\n')
    assert filedirname1 in os.listdir(os.getcwd()) and not os.path.isdir(
        filedirname1), f'Error with function "show_files()"'


if __name__ == '__main__':
    pass
