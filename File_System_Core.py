from Os_Dir import Os_Dir
from Os_File import Os_File
from Os_Detail import Os_Detail

class File_System_Core():

    def __init__(self):
        try:
            self.Os_Dir=Os_Dir()
            self.Os_File=Os_File()
            self.Os_Detail=Os_Detail()
        except Exception as Err:
            print(Err)



