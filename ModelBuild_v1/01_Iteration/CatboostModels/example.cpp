#include <iostream>
#include <string>

void catboost_demo() {
    ModelCalcerHandle* modelHandle = ModelCalcerCreate();
    if (!modelHandle) {
        std::cout << "Model handle creation failed: " << GetErrorString() << std::endl;
        return;
    }
    if (!LoadFullModelFromFile(modelHandle, "adult_500.cbm")) {
        std::cout << "Load model failed: " << GetErrorString() << std::endl;
        return;
    }
    std::cout << "Loaded model with " << GetTreeCount(modelHandle) << " trees." << std::endl;
    std::cout << "Model expects " << GetFloatFeaturesCount(modelHandle) << " float features and " << GetCatFeaturesCount(modelHandle) << " categorical features" << std::endl;
    const std::string paramsKey = "params";
    if (CheckModelMetadataHasKey(modelHandle, paramsKey.c_str(), paramsKey.size())) {
        size_t paramsStringLength = GetModelInfoValueSize(modelHandle, paramsKey.c_str(), paramsKey.size());
        std::string params(GetModelInfoValue(modelHandle, paramsKey.c_str(), paramsKey.size()), paramsStringLength);
        std::cout << "Applying model trained with params: " << params << std::endl;
    }
    const size_t docCount = 3;
    const size_t floatFeaturesCount = 6;
    const float floatFeatures[docCount ][floatFeaturesCount ] = {
        {28.0, 120135.0, 11.0, 0.0, 0.0, 40.0},
        {49.0, 57665.0, 13.0, 0.0, 0.0, 40.0},
        {34.0, 355700.0, 9.0, 0.0, 0.0, 20.0}
    };
    const float* floatFeaturesPtrs[docCount] = {
        floatFeatures[0],
        floatFeatures[1],
        floatFeatures[2]
    };
    const size_t catFeaturesCount = 8;
    const char* catFeatures[docCount][8] = {
        {"Private", "Assoc-voc", "Never-married", "Sales", "Not-in-family", "White", "Female", "United-States"},
        {"?", "Bachelors", "Divorced", "?", "Own-child", "White", "Female", "United-States"},
        {"State-gov", "HS-grad", "Separated", "Adm-clerical", "Unmarried", "White", "Female", "United-States"}
    };
    const char** catFeaturesPtrs[docCount] = {
        catFeatures[0],
        catFeatures[1],
        catFeatures[2]
    };
    double result[3] = { 0 };
    if (!CalcModelPrediction(
        modelHandle,
        docCount,
        floatFeaturesPtrs, floatFeaturesCount,
        catFeaturesPtrs, catFeaturesCount,
        result, docCount)
    ) {
        std::cout << "Prediction failed: " << GetErrorString() << std::endl;
        return;
    }
    std::cout << "Results: ";
    for (size_t i = 0; i < 3; ++i) {
        std::cout << result[i] << " ";
    }
    std::cout << std::endl;
    /* Sometimes you need to evaluate model on single object.
       We provide special method for this case which is prettier and is little faster than calling batch evaluation for single object
    */
    double singleResult = 0.0;
    if (!CalcModelPredictionSingle(
        modelHandle,
        floatFeatures[0], floatFeaturesCount,
        catFeatures[0], catFeaturesCount,
        &singleResult, 1)
    ) {
        std::cout << "Single prediction failed: " << GetErrorString() << std::endl;
        return;
    }
    std::cout << "Single prediction: " << singleResult << std::endl;
}
