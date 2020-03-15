#ifndef GRADIENT_OPERATORS_CV_H
#define GRADIENT_OPERATORS_CV_H

#include <opencv/cv.h>
#include <opencv/cxcore.h>

namespace stag {

/// Compute color image gradient
void ComputeGradientMapByPrewitt(IplImage *smoothImg, short *gradImg, unsigned char *dirImg, int GRADIENT_THRESH);

} // namespace stag

#endif