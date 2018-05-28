# Buying tickets to cinema


class Cinema(object):
    consumer_count = 0

    def __init__(self, consumer, consumer_age, movie,
                 movie_rating, movie_date, cinema_hall, cinema_seat, price,
                 status='initial'):
        self.consumer = consumer
        self.consumer_age = consumer_age
        self.movie = movie
        self.movie_rating = movie_rating
        self.movie_date = movie_date
        self.cinema_hall = cinema_hall
        self.cinema_seat = cinema_seat
        self.price = price
        self.status = status
        Cinema.consumer_count += 1

    def displayCount(self):
        print('Tickets submitted: %d' % Cinema.consumer_count)

    def CheckConsumerAge(self):
        if self.movie_rating <= self.consumer_age:
            self.status = 'approved'
        else:
            self.status = 'not approved'

    def __str__(self):
        return '[Cinema: %s, %d, %s, %d, %s, %d, %s, %d, %s]' \
               % (self.consumer, self.consumer_age, self.movie,
                  self.movie_rating, self.movie_date, self.cinema_hall,
                  self.cinema_seat, self.price, self.status)

    def displayTicketInfo(self):
        print('Buyer Name Surname: ', self.consumer)
        print('Buyer Total Age: ', self.consumer_age)
        print('Movie: ', self.movie)
        print('Movie Rating: ', self.movie_rating)
        print('Date: ', self.movie_date)
        print('Hall: ', self.cinema_hall)
        print('Seat: ', self.cinema_seat)
        print('Price: ', self.price)
        print('Status: ', self.status)


consumer1 = Cinema('Jack Black', 36, 'Avengers: Infinity War', 18,
                   '24-05-2018', 1, '2-12', 9.0)
print(consumer1)
consumer1.CheckConsumerAge()
consumer1.displayTicketInfo()

consumer2 = Cinema('Sam Gans', 16, 'Avengers: Infinity War', 18, '27-05-2018',
                   1, '2-11', 9.0)
print(consumer2)
consumer2.CheckConsumerAge()
consumer2.displayTicketInfo()

consumer3 = Cinema('Sam Gans', 9, 'Solo: A star Wars Story', 18, '28-05-2018',
                   1, '1-9', 12.0)
print(consumer3)
consumer3.CheckConsumerAge()
consumer3.displayTicketInfo()

print('Tickets submitted: %d' % Cinema.consumer_count)
