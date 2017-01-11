import pandas as pd




def TbgCsvReader(pathToCsv=None,outputPath):
	if pathToCsv==None:
		print "Please provide path to csv"
	else:
		data = pd.read_csv(pathToCsv, index_col=2, parse_dates=True,sep=';',decimal=',')
		data.drop(data.columns[[0,1]], axis=1, inplace=True)
		data = data.reindex(data.index.rename('Date Time'))
 		data.to_csv(outputPath)