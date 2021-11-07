import configparser
import gmplot

config = configparser.ConfigParser()
config.read('google_api.conf')

# API KEY from config file
apikey = config['APIKey']['apikey']


latitude_list = [47.4268991755, 47.4151264537, 47.4133813496, 47.4226367328, 47.4048725228 ]
longitude_list = [ 9.383057054, 9.34173656537, 9.34717463867, 9.34185926089, 9.30853184166 ]

def geomap_yearly_overview(list_latitude, list_longitude, circle_size, circle_color):
    gmap3 = gmplot.GoogleMapPlotter(47.4, 9.3, 13, apikey=apikey)
    gmap3.scatter( list_latitude, list_longitude, circle_color, size = circle_size, marker = False )
    #gmap3.draw("map.html")
    html_map = gmap3.get()
    return html_map
    

if __name__ == "__main__":
    geomap_yearly_overview(latitude_list, longitude_list, 50, "yellow")
    