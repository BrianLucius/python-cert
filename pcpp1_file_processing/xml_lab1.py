import xml.etree.ElementTree as et

class TemperatureConverter:
    def convert_c_to_f(self, c):
        return (9/5 * c) + 32
    
    def convert_f_to_c(self, f):
        return (f - 32) / (9/5)

class ForecastXmlParser:
    def parse(self):
        temp_c = TemperatureConverter()
        tree = et.parse('/Users/brian/Repositories/python-cert/pcpp1_file_processing/forecast.xml')
        forecast = tree.getroot()
        for day in forecast:
            print(day[0].text, ":\t", day[1].text, 'Celsius,', round(temp_c.convert_c_to_f(int(day[1].text)), 1), 'Fahrenheit')

forecast = ForecastXmlParser()
forecast.parse()