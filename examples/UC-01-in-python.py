"""
Metview Python framework

UC-01. The Analyst produces plots and files for the Product user

--------------------------------------------------------------------------------
1. Analyst creates plots and files thanks to his Python applications and scripts
   that benefits from the underlying tools of the framework
--------------------------------------------------------------------------------

Analyst reads data from a GRIB file and derives another quantity from it. Then,
Analyst saves his data as a GRIB file and creates a plot in PNG format. 
"""

import mpy.metview as mpy


mydata = mpy.read('tests/test.grib')

derived = mydata * 2 + 5

mpy.write('derived_data.grib', derived)

grid_shade = mpy.mcont({
    'legend': True,
    'contour': False,
    'contour_highlight': True,
    'contour_shade': True,
    'contour_shade_technique': 'grid_shading',
    'contour_shade_max_level_colour': 'red',
    'contour_shade_min_level_colour': 'blue',
    'contour_shade_colour_direction': 'clockwise',
})

# Macro-like PNG creation:
png = mpy.png_output({'output_width': 1200, 'output_name': './examples/myplot'})

mpy.plot(png, derived, grid_shade)


# Using a different notation:
png_output = {
    'output_type': 'png',
    'output_width': 1200,
    'output_name': './examples/myplot'
}

mpy.plot(derived, grid_shade, **png_output)
