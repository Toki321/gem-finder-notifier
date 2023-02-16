import os.path

def readIds():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../idsToTrack.txt")

    with open(file_path, "r") as f:
        lines = f.readlines()
        toTrackIdList = [line.split()[-1] for line in lines]
        return toTrackIdList


