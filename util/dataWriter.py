import numpy as np
import os
import xarray as xr

class DataWriter:
    def __init__(self, outputPath):
        self.outputPath = outputPath        
        self.checkExistOrCreate(self.outputPath)

    def checkExistOrCreate(self, outputPath):
        if not os.path.exists(outputPath): 
            print("Path is not exist, created")
            os.makedirs(outputPath)
        else:
            print("Path exists")

    def toNC(self, fname, data, coords, dims, varName):
        xrData = xr.DataArray(data, 
                              coords = coords,
                              dims = dims,
                              name = varName)
        xrData.to_netcdf(self.outputPath + fname)
        
    def toNPY(self, fname, data):
        np.save(self.outputPath + fname, data)
