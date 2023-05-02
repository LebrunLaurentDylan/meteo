**METEO is a wheather info extracting program that i conceved myself for training on API and data treatment.**

To run this project you'll need anaconda installed and an IDE (i'm using PYCHARM).
you'll also need some packages installed on your envs like "datetime", "request", "os.path". 
the API is open and free, so you don't need any KEY to run it. 

the goal of this program is to gather infos about temperature on a specific city ( french cities for now) it's using a cleaned-up json-file (via algorithmes located inside "location_data_manager" using "clean_location.json") of all the cities in france to be able to extract the "latitude" and "longitude" data contained in the json-file.
then the program is using the today.date() to ask you how many days ahead of predictions you want, and use this number to had to today's date to figure out the end date.  
The URL is then assembled with the information of the city, start date and end date.  
then call the API to "requests" the information and put it on display on a "scatter" graph. 

the goal was to train on API requests, gathering and cleaning the data I could find, using the API documentation, and in this case, the location data being long and lat instead of just a city name, figure out a way to make a city name again for the final user because entering latitude and longitude by hand would have been to much to ask. 
on the second part the idea was to train on channeling the data I wanted and visualizing it as clear as possible. 

note: plt.show is not new to me but i still don't master it enough to have the data displayed exactly how i wanted them. I didn't focused on debugging(like : what if you enter a number and not a city name, or what if it is in full MAJ instead of lower case etc.) because that wasn't the point of the exercise. maybe on a another version of this program.