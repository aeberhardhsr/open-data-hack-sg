import configparser
import gmplot

config = configparser.ConfigParser()
config.read('google_api.conf')

# API KEY from config file
apikey = config['APIKey']['apikey']


latitude_list = [47.4268991755, 47.4151264537, 47.4133813496, 47.4226367328, 47.4048725228 ]
longitude_list = [ 9.383057054, 9.34173656537, 9.34717463867, 9.34185926089, 9.30853184166 ]
  
gmap3 = gmplot.GoogleMapPlotter(47.4, 9.3, 13, apikey=apikey)
  
# scatter method of map object 
# scatter points on the google map
gmap3.scatter( latitude_list, longitude_list, '#FF0000', size = 40, marker = False )
  
# Plot method Draw a line in
# between given coordinates
#gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width = 2.5)
  
gmap3.draw("map.html")
