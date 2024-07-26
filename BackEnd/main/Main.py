from Clustering import Clustering as clst

class Main:
    print("This is main class")

    def __init__(self) -> None:
        self.clst = clst()
    
if __name__ == "__main__":
    print("This is the main execution block")
    # dirLoc = "DATA\\Test\\DistrictWiseData"
    dirLoc = "DATA\\Test\\StateWiseData"
    # clst.formClusterWhole("DATA\Test\stateWiseData\states.csv", "states.csv")
    clst.formClusterStateWise()
    # clst.formCluster(dirLoc)
    # clst.prepareStateData()
    # clst.formClusterStateWise()
    # clst.formClusterStateWise()
    # clst.formClusterWhole()