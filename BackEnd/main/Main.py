from clustering import Clustering as clst

class Main:
    print("This is main class")

    def __init__(self) -> None:
        self.clst = clst()
    
if __name__ == "__main__":
    print("This is the main execution block")
    clst.formCluster()
    # clst.formClusterWhole()