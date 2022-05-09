from flask import render_template, request
from . import importation_bp
import pandas as pd

@importation_bp.route('/', methods=['get', 'post'])
def index():
        message = ''

        if request.method == 'POST':
                excelfile = request.form.get('excelfile')

                file = request.files['excelfile']
                fileName = file.filename
                # print(fileName)

                data_excel = pd.read_excel(file)

                data_types = data_excel.dtypes

                exist_null_Desde = pd.isnull(data_excel['Desde']).values.any()
                print(exist_null_Desde)

                # print('\ntypes columns')
                # print(data_types)
                
                # print('\ncolumns name')
                # for col in data_excel.columns:
                #         print(col)

        return render_template('importation/index.html', message = message)
