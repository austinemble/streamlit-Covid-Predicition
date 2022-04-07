import pandas as pd;

df = pd.read_csv("Datasets/covid-variants.csv")
def dataSeperate():
    for countryName in df:
        print("Country Name: "+countryName)
        data =df[df['location']==countryName]
        data.to_csv("Datasets/By Country/"+countryName+'--CovidData.csv')
        variantsAll = df.variant.unique()
    for variantName in df:
        print("Variant Name: "+variantName)
        data =df[df['variant']==variantName]
        print("DATA!!\n",data)
        data.to_csv("Datasets/By Variant/"+variantName+'--CovidData.csv')

dataSeperate();