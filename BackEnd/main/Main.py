from Clustering import Clustering as clst
from Utility import Utility as util

class Main:
    print("This is main class")

    def __init__(self) -> None:
        self.clst = clst()
    
if __name__ == "__main__":
    print("This is the main execution block")
    # dirLoc = "DATA\\Test\\DistrictWiseData"
    dirLoc = "DATA\\Test\\StateWiseData"
    
    # clst.formCluster(dirLoc)
    util.saveDendrogram()