import os
import shutil
import pathlib

class Os_Dir():

    def __init__(self):
        self.WorkPath=os.getcwd()+'/'

# ----------------------------------------------------------------------------------------------

    #刪除該位址資尿夾
    def Delete_Dir(self,Dir_Path):
        try:
            shutil.rmtree(Dir_Path)
        except OSError as Err:
            print(Err)
        else:
            print(Dir_Path,"The directory is deleted successfully",sep=' ')

# ----------------------------------------------------------------------------------------------
    def Create_Dir(self,Dir_Path):
        if not os.path.isdir(Dir_Path):
            os.mkdir(Dir_Path)
# ----------------------------------------------------------------------------------------------
    def Check_Dir(self,Dir_Path):
        Dir_Path = Dir_Path
        File = pathlib.Path(Dir_Path)
        return File.is_dir()
# ----------------------------------------------------------------------------------------------