# -*- coding: utf-8 -*-

"""
/***************************************************************************
 EcoValuator
                                 A QGIS plugin
 Calculate ecosystem service values for a given area
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2018-04-02
        copyright            : (C) 2018 by Key-Log Economics
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Key-Log Economics'
__date__ = '2018-04-02'
__copyright__ = '(C) 2018 by Key-Log Economics'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import csv
import processing

from PyQt5.QtCore import (QCoreApplication,
                          QFileInfo
                          )

from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterFeatureSink,
                       QgsFields,
                       QgsField,
                       QgsFeature,
                       QgsFeatureSink,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterString,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingOutputLayerDefinition,
                       QgsRasterLayer,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterRasterDestination
                       )

from .parser import HTMLTableParser

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))



class CreatePrintLayoutAndExportMap(QgsProcessingAlgorithm):
    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.
    INPUT_VECTOR = 'INPUT_VECTOR'
    INPUT_TITLE = 'INPUT_TITLE'
    INPUT_SUBTITLE = 'INPUT_SUBTITLE'
    INPUT_CREDIT_TEXT = 'INPUT_CREDIT_TEXT'
    
    
    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm
        """
        #Add Raster Layer as input
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.INPUT_VECTOR,
                self.tr('Input original vector layer of study area used in Step 1'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        
        #Add String as input
        self.addParameter(
            QgsProcessingParameterString(
                self.INPUT_TITLE,
                self.tr('Input title string (Optional)')
            )
        )

#        #Add String as input
#        self.addParameter(
#            QgsProcessingParameterString(
#                self.INPUT_SUBTITLE,
#                self.tr('Input Subtitle (this should be returned from the ESV choice in step 2)(Optional)')
#            )
#        )
#
#        #Add String as input
#        self.addParameter(
#            QgsProcessingParameterString(
#                self.INPUT_CREDIT_TEXT,
#                self.tr('Input Credits Text (Optional)')
#            )
#        )

	
    def processAlgorithm(self, parameters, context, feedback):
        """This actually does the processing for creating the print layout and exporting as .pdf"""
        #needs all the arguments (self, parameters, context, feedback)
        
        
        log = feedback.setProgressText
        
        input_vector = self.parameterAsVectorLayer(parameters, self.INPUT_VECTOR, context)
        input_title = self.parameterAsString(parameters, self.INPUT_TITLE, context)
        
        log(input_title.name())
#        input_vector_crs = input_vector.crs().authid()
#        if input_vector_crs == "EPSG:102003":
#            log("correct input vector crs")
        

            



    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Step 3: Create Print Layout and Export as .pdf'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'EcoValuator'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("This step takes an output raster layer from step 2 as input and automatically produces a finished map output as a .pdf. The output will contain the map (zoomed to the extent of your current screen) and a legend which contains the active layers in the project (***NEEDS WORK***)")

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def helpUrl(self):
        """
        Returns the location of the help file for this algorithm. This is the
        location that will be followed when the user clicks the Help button
        in the algorithm's UI.
        """
        return "http://keylogeconomics.com/ecovaluator-help/"

    def createInstance(self):
        return CreatePrintLayoutAndExportMap()
