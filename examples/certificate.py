from certificator import CSVCertificator

certificator = CSVCertificator(data_path='./data.csv', meta_path='./meta.json', template_path='.', filename_format='minicurso-{name}.pdf')
certificator.generate()
