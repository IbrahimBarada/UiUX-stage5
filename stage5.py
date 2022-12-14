import matplotlib.pyplot as plt
import numpy


def statistical_analysis(data):
    median = numpy.median(data)
    standard_deviation = numpy.std(data)
    mean = numpy.mean(data)
    max = numpy.max(data)
    min = numpy.min(data)
    quartiles = numpy.percentile(data, [25, 50, 75])
    return median, standard_deviation, mean, max, min, quartiles


def barplot(data, title):
    keys = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    # creating the bar plot
    plt.bar(keys, values, color='black',
            width=0.4)

    plt.xlabel("Participant")
    plt.ylabel("Number of clicks")
    plt.title(title)
    plt.show()


Registration_and_Login = {'Marwa': 13, 'Tom': 11, 'Harry': 9, 'Jordan': 8, 'Sara': 12}
search_and_filter = {'Marwa': 11, 'Tom': 14, 'Harry': 6, 'Jordan': 5, 'Sara': 10}
booking_management = {'Marwa': 18, 'Tom': 21, 'Harry': 12, 'Jordan': 24, 'Sara': 13}
review = {'Marwa': 12, 'Tom': 8, 'Harry': 12, 'Jordan': 24, 'Sara': 13}
barplot(Registration_and_Login, 'Number of clicks for the Registration and Login feature')
barplot(search_and_filter, 'Number of clicks for the Search and Filter feature')
barplot(booking_management, 'Number of clicks for the Booking Management feature')
barplot(review, 'Number of clicks for the Review feature')

time_Registration_and_Login = {'Marwa': 2.5, 'Tom': 4, 'Harry': 2.5, 'Jordan': 5, 'Sara': 4}
time_search_and_filter = {'Marwa': 3, 'Tom': 3.5, 'Harry': 4, 'Jordan': 14, 'Sara': 4}
time_booking_management = {'Marwa': 5, 'Tom': 7, 'Harry': 8, 'Jordan': 6, 'Sara': 3}
time_review = {'Marwa': 2, 'Tom': 5, 'Harry': 6, 'Jordan': 6, 'Sara': 3}

barplot(time_Registration_and_Login, 'Time spent on the Registration and Login feature')
barplot(time_search_and_filter, 'Time spent on Search and Filter feature')
barplot(time_booking_management, 'Time spent on the Booking Management feature')
barplot(time_review, 'Time spent on the Review feature')


statistical_analysis(Registration_and_Login)
statistical_analysis(search_and_filter)
statistical_analysis(booking_management)
statistical_analysis(review)
statistical_analysis(time_Registration_and_Login)
statistical_analysis(time_search_and_filter)
statistical_analysis(time_booking_management)
statistical_analysis(time_review)
