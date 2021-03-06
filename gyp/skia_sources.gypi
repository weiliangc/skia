# Copyright 2015 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# Include this gypi to include all 'utils' files
# The parent gyp/gypi file must define
#       'skia_src_path'     e.g. skia/trunk/src
#       'skia_include_path' e.g. skia/trunk/include
#
# The skia build defines these in common_variables.gypi
#
{
  'utils_sources': [
    '../include/utils/SkBoundaryPatch.h',
    '../include/utils/SkFrontBufferedStream.h',
    '../include/utils/SkCamera.h',
    '../include/utils/SkCanvasStateUtils.h',
    '../include/utils/SkDumpCanvas.h',
    '../include/utils/SkEventTracer.h',
    '../include/utils/SkInterpolator.h',
    '../include/utils/SkLayer.h',
    '../include/utils/SkMeshUtils.h',
    '../include/utils/SkNoSaveLayerCanvas.h',
    '../include/utils/SkNWayCanvas.h',
    '../include/utils/SkNullCanvas.h',
    '../include/utils/SkPaintFilterCanvas.h',
    '../include/utils/SkParse.h',
    '../include/utils/SkParsePath.h',
    '../include/utils/SkPictureUtils.h',
    '../include/utils/SkRandom.h',
    '../include/utils/SkTextBox.h',

    '../src/utils/SkBase64.cpp',
    '../src/utils/SkBase64.h',
    '../src/utils/SkBitmapSourceDeserializer.cpp',
    '../src/utils/SkBitmapSourceDeserializer.h',
    '../src/utils/SkBitSet.h',
    '../src/utils/SkBoundaryPatch.cpp',
    '../src/utils/SkFrontBufferedStream.cpp',
    '../src/utils/SkCamera.cpp',
    '../src/utils/SkCanvasStack.h',
    '../src/utils/SkCanvasStack.cpp',
    '../src/utils/SkCanvasStateUtils.cpp',
    '../src/utils/SkCurveMeasure.cpp',
    '../src/utils/SkCurveMeasure.h',
    '../src/utils/SkDashPath.cpp',
    '../src/utils/SkDashPathPriv.h',
    '../src/utils/SkDeferredCanvas.cpp',
    '../src/utils/SkDumpCanvas.cpp',
    '../src/utils/SkEventTracer.cpp',
    '../src/utils/SkFloatUtils.h',
    '../src/utils/SkInterpolator.cpp',
    '../src/utils/SkLayer.cpp',
    '../src/utils/SkMatrix22.cpp',
    '../src/utils/SkMatrix22.h',
    '../src/utils/SkMeshUtils.cpp',
    '../src/utils/SkMultiPictureDocument.cpp',
    '../src/utils/SkNWayCanvas.cpp',
    '../src/utils/SkNullCanvas.cpp',
    '../src/utils/SkOSFile.cpp',
    '../src/utils/SkPaintFilterCanvas.cpp',
    '../src/utils/SkParse.cpp',
    '../src/utils/SkParseColor.cpp',
    '../src/utils/SkParsePath.cpp',
    '../src/utils/SkPatchGrid.cpp',
    '../src/utils/SkPatchGrid.h',
    '../src/utils/SkPatchUtils.cpp',
    '../src/utils/SkPatchUtils.h',
    '../src/utils/SkRGBAToYUV.cpp',
    '../src/utils/SkRGBAToYUV.h',
    '../src/utils/SkShadowPaintFilterCanvas.cpp',
    '../src/utils/SkShadowPaintFilterCanvas.h',
    '../src/utils/SkTextBox.cpp',
    '../src/utils/SkTextureCompressor.cpp',
    '../src/utils/SkTextureCompressor.h',
    '../src/utils/SkTextureCompressor_Utils.h',
    '../src/utils/SkTextureCompressor_ASTC.cpp',
    '../src/utils/SkTextureCompressor_ASTC.h',
    '../src/utils/SkTextureCompressor_Blitter.h',
    '../src/utils/SkTextureCompressor_R11EAC.cpp',
    '../src/utils/SkTextureCompressor_R11EAC.h',
    '../src/utils/SkTextureCompressor_LATC.cpp',
    '../src/utils/SkTextureCompressor_LATC.h',
    '../src/utils/SkThreadUtils.h',
    '../src/utils/SkThreadUtils_pthread.cpp',
    '../src/utils/SkThreadUtils_pthread.h',
    '../src/utils/SkThreadUtils_win.cpp',
    '../src/utils/SkThreadUtils_win.h',
    '../src/utils/SkWhitelistTypefaces.cpp',

    #mac
    '../include/utils/mac/SkCGUtils.h',
    '../src/utils/mac/SkCreateCGImageRef.cpp',

    #windows
    '../src/utils/win/SkAutoCoInitialize.h',
    '../src/utils/win/SkAutoCoInitialize.cpp',
    '../src/utils/win/SkDWrite.h',
    '../src/utils/win/SkDWrite.cpp',
    '../src/utils/win/SkDWriteFontFileStream.cpp',
    '../src/utils/win/SkDWriteFontFileStream.h',
    '../src/utils/win/SkDWriteGeometrySink.cpp',
    '../src/utils/win/SkDWriteGeometrySink.h',
    '../src/utils/win/SkHRESULT.h',
    '../src/utils/win/SkHRESULT.cpp',
    '../src/utils/win/SkIStream.h',
    '../src/utils/win/SkIStream.cpp',
    '../src/utils/win/SkTScopedComPtr.h',
    '../src/utils/win/SkWGL.h',
    '../src/utils/win/SkWGL_win.cpp',

    #testing
    '../src/fonts/SkGScalerContext.cpp',
    '../src/fonts/SkGScalerContext.h',
    '../src/fonts/SkRandomScalerContext.cpp',
    '../src/fonts/SkRandomScalerContext.h',
    '../src/fonts/SkTestScalerContext.cpp',
    '../src/fonts/SkTestScalerContext.h',
  ],
  'sksl_include_dirs': [
    '../include/config',
    '../include/core',
    '../include/private',
    '../src/sksl',
  ],
  'sksl_sources': [
    '../src/sksl/SkSLCFGGenerator.cpp',
    '../src/sksl/SkSLCompiler.cpp',
    '../src/sksl/SkSLIRGenerator.cpp',
    '../src/sksl/SkSLParser.cpp',
    '../src/sksl/SkSLGLSLCodeGenerator.cpp',
    '../src/sksl/SkSLSPIRVCodeGenerator.cpp',
    '../src/sksl/SkSLUtil.cpp',
    '../src/sksl/ir/SkSLSymbolTable.cpp',
    '../src/sksl/ir/SkSLType.cpp',
  ],
}
