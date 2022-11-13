def train(this, input, targetOutput, spec):

    import numpy as np
    from collections import defaultdict

    group_by_feature_name = this.technique.groupBy
    data = c3.Dataset.toPandas(dataset=input)
    feature_columns = list(data.columns)
    feature_columns.remove(group_by_feature_name)
    values_to_impute = defaultdict(dict)

    for name, group in data.groupby(group_by_feature_name):
        for col in feature_columns:
            values_to_impute[name][col] = np.nanmean(group[col])

    this.trainedModel = c3.MLTrainedModelArtifact(model=c3.PythonSerialization.serialize(obj=values_to_impute))
    return this

def process(this, input):

    import numpy as np
    from collections import defaultdict

    data = c3.Dataset.toPandas(dataset=input)
    values_to_impute = c3.PythonSerialization.deserialize(serialized=this.trainedModel.model)
    group_by_feature_name = this.technique.groupBy

    for group_name, values in values_to_impute.items():
        for feature_name, average_value in values.items():
            flag1 = data[feature_name].isnull()
            flag2 = data[group_by_feature_name] == group_name
            data[feature_name].loc[flag1 & flag2] = average_value

    return c3.Dataset.fromPython(pythonData=data)


