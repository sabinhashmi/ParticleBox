#include "catboost/libs/model_interface/wrapped_calcer.h"
double ApplyCatboostModel(const std::vector<float>& floatFeatures, const std::vector<std::string>& catFeatures) {
    ModelCalcerWrapper calcer("model.cbm");
    return calcer.Calc(floatFeatures, catFeatures);
}